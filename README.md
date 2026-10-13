# CapCut ORE Motion Brand

Skill para Codex que guía la creación y revisión de motion graphics de marca en **CapCut**. Complementa herramientas como CapCutKit con dirección tipográfica, protección del logo, composición, movimiento y comprobación de la exportación. Versión **1.1.0**, en español.

No sustituye el editor, no garantiza calidad por estar instalada y no incluye una integración/API de ElevenLabs. Las reglas confirmadas de eQatu están separadas del perfil ORE, cuyo manual debe incorporarse desde el proyecto.

## Instalación en Codex

Pedir a Codex:

> Instala la skill de https://github.com/anibalelore/capcut-ore-motion-brand

O usar el instalador de skills de Codex:

```text
python <skill-installer>/scripts/install-skill-from-github.py --repo anibalelore/capcut-ore-motion-brand --path . --name capcut-ore-motion-brand
```

También se puede copiar este repositorio a `~/.codex/skills/capcut-ore-motion-brand`, conservando `SKILL.md`, `agents`, `references` y `scripts`. Estará disponible en el siguiente turno de Codex. No sobrescribir una instalación existente sin revisar sus cambios.

## Uso

```text
Usa $capcut-ore-motion-brand para corregir este spot en CapCut,
respetar el manual de marca y comprobar fuentes, fondos, logos y exportación.
```

La skill se puede seleccionar automáticamente cuando una tarea relevante lo requiera.

## Contenido

- `SKILL.md`: instrucciones y criterios de entrega.
- `references/brand-profiles.md`: reglas confirmadas y límites de conocimiento por marca.
- `references/native-capcut.md`: guardado seguro, medidas, fuentes, proporciones, audio local y exportación.
- `references/motion-review.md`: dirección visual, voz, mezcla y revisión con evidencia.
- `references/production-direction.md`: brief, sistema tipográfico, timing, recetas nativas y evaluación interna de calidad.
- `references/capcut-shot-template.md`: especificación ejecutable por plano; no es un archivo CapCut importable.
- `references/standards-and-sources.md`: Material Design, Figma, School of Motion, documentación CapCut y referencias WCAG.
- `examples/spot-30s-example.md`: plan orientativo de seis escenas; no representa un video ya ejecutado.
- `scripts/audit_draft.py`: auditoría estructural de solo lectura; Python 3.10+, sin dependencias externas.

```text
python scripts/audit_draft.py <ruta-a-draft_content.json>
python -m unittest discover -s scripts -p test_audit_draft.py -v
```

El auditor reporta recursos/fuentes no resueltos, referencias de material faltantes, canales duplicados y keyframes fuera del segmento. Las rutas internas `##_draftpath_placeholder_..._##` se resuelven contra la carpeta del borrador. Una advertencia no prueba un fallo visual y no tener advertencias no certifica diseño ni sonido.

## Requisitos y límites

CapCut y los activos/manual de la marca deben estar disponibles para producir. Para automatizar Windows, utilizar las capacidades soportadas de computer-use del entorno. Si se usa CapCutKit, seguir las instrucciones de su versión y preservar ediciones manuales. No se incluyen logos, fuentes comerciales, archivos del anuncio, credenciales ni accesos de pago.

Conservar el libreto exacto cuando así lo pida el usuario. Comprobar las condiciones actuales del proveedor de voz para uso comercial. La skill no autoriza compras, publicación o envío a terceros.
