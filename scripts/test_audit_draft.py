"""Exercise read-only auditing against isolated files, not an open editor."""
import json
import tempfile
import unittest
from pathlib import Path
from audit_draft import audit


class DraftAuditTests(unittest.TestCase):
    def test_placeholder_resources_resolve_and_remain_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / 'Resources').mkdir()
            font = base / 'Resources/font.ttf'
            font.write_bytes(b'font-fixture')
            draft = {'materials': {'texts': [{'id': 't', 'content': json.dumps({
                'text': 'Hola', 'styles': [{'font': {'path': '##_draftpath_placeholder_ABC_##/Resources/font.ttf'}}]})}]},
                'tracks': [{'segments': [{'id': 's', 'material_id': 't', 'target_timerange': {'duration': 100}}]}]}
            before = json.dumps(draft, sort_keys=True)
            self.assertEqual(audit(draft, base)['issues'], [])
            self.assertEqual(json.dumps(draft, sort_keys=True), before)
            self.assertEqual(font.read_bytes(), b'font-fixture')

    def test_missing_media_duplicate_and_outside_keyframes(self):
        with tempfile.TemporaryDirectory() as temp:
            draft = {'materials': {'videos': [{'id': 'v', 'type': 'photo', 'path': 'missing.png'}]},
                'tracks': [{'segments': [{'id': 's', 'material_id': 'v', 'target_timerange': {'duration': 100},
                    'common_keyframes': [{'property_type': 'KFTypeAlpha', 'keyframe_list': [{'time_offset': 101}]},
                                         {'property_type': 'KFTypeAlpha', 'keyframe_list': []}]}]}]}
            codes = {issue['code'] for issue in audit(draft, Path(temp))['issues']}
            self.assertEqual(codes, {'media_unresolved', 'duplicate_channel', 'keyframe_outside_segment'})


if __name__ == '__main__':
    unittest.main()
