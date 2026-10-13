"""Read-only structural hints for a saved CapCut draft; not visual/audio QA."""
import argparse
import json
import re
from pathlib import Path


def audit(draft, base):
    issues = []
    materials = {}

    def issue(code, item, detail):
        issues.append({'code': code, 'item': item, 'detail': detail})

    def exists(value):
        # Some CapCut versions persist doubled separators in Windows paths.
        value = re.sub(r'^##_draftpath_placeholder_[^/\\]+_##[/\\]?', '', value)
        path = Path(value.replace('\\\\', '\\'))
        return path.is_file() or (not path.is_absolute() and (base / path).is_file())

    for category, entries in draft.get('materials', {}).items():
        for entry in entries if isinstance(entries, list) else []:
            if not isinstance(entry, dict):
                continue
            mid = entry.get('id')
            if mid:
                materials[mid] = entry
            if category in ('videos', 'audios'):
                path = entry.get('path', '')
                if not path or not exists(path):
                    issue('media_unresolved', mid, path or 'No local path declared')
            if category == 'audios' and entry.get('type') == 'extract_music':
                issue('extraction_classification', mid, 'Check whether this is extracted audio or an imported local file; do not change license flags.')
            if category == 'texts':
                try:
                    content = json.loads(entry.get('content', '{}'))
                except (ValueError, TypeError):
                    issue('invalid_text_content', mid, 'Text content is not valid JSON')
                    continue
                fonts = [entry.get('font_path', '')]
                fonts += [style.get('font', {}).get('path', '') for style in content.get('styles', [])]
                declared = {p for p in fonts if p}
                if not declared:
                    issue('font_runtime_check', mid, 'No local font path; verify actual family and weight inside CapCut')
                for path in declared:
                    if not exists(path):
                        issue('font_unresolved', mid, path)

    for track in draft.get('tracks', []):
        for segment in track.get('segments', []):
            sid = segment.get('id')
            if segment.get('material_id') not in materials:
                issue('material_unresolved', sid, segment.get('material_id'))
            duration = segment.get('target_timerange', {}).get('duration', 0)
            properties = set()
            scales = set()
            for channel in segment.get('common_keyframes', []):
                prop = channel.get('property_type')
                if prop in properties:
                    issue('duplicate_channel', sid, prop)
                properties.add(prop)
                if prop in ('KFTypeScaleX', 'KFTypeScaleY'):
                    scales.add(prop)
                for frame in channel.get('keyframe_list', []):
                    time = frame.get('time_offset', 0)
                    if time < 0 or time > duration:
                        issue('keyframe_outside_segment', sid, {'property': prop, 'time': time, 'duration': duration})
            material = materials.get(segment.get('material_id'), {})
            if material.get('type') == 'photo' and len(scales) == 2:
                issue('photo_scale_visual_check', sid, 'Both scale channels present; inspect original proportions at animated frames')
    return {'read_only': True, 'visual_audio_review_required': True,
            'duration_us': draft.get('duration'), 'fps': draft.get('fps'),
            'canvas': draft.get('canvas_config'), 'track_count': len(draft.get('tracks', [])),
            'issues': issues}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('draft', type=Path)
    args = parser.parse_args()
    draft = json.loads(args.draft.read_text(encoding='utf-8-sig'))
    print(json.dumps(audit(draft, args.draft.parent), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
