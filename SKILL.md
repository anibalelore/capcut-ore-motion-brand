---
name: capcut-ore-motion-brand
description: Crear, corregir y revisar motion graphics publicitarios de marca en CapCut, con tipografía comprobada, logos protegidos y exportaciones verificadas. Usar para ORE, eQatu y otras marcas con reglas suministradas; no sustituye CapCut por otro editor.
---

# CapCut ORE Motion Brand

Producir un proyecto nativo de CapCut con dirección visual coherente y evidencia de que la exportación respeta la marca. Instalar esta skill no garantiza calidad: comprobar el resultado visible y audible.

## Contexto y alcance

- Mantener editor, formato, libreto y revisiones elegidos por el usuario. Una pregunta o petición de recomendaciones no autoriza rehacer el video.
- Reanudar el proyecto existente y preservar ediciones manuales. Usar CapCutKit si está disponible; no instalarlo ni cambiar el entorno por el solo hecho de activar esta skill.
- Leer [marca y perfiles](references/brand-profiles.md) al trabajar con ORE/eQatu o incorporar un manual. Las reglas de eQatu no son reglas de ORE.
- Leer [operación nativa](references/native-capcut.md) antes de escribir borradores o diagnosticar fuentes, proporciones o keyframes. Para calidad visual/audio leer [dirección y revisión](references/motion-review.md).

## Decisiones de diseño

Derivar una especificación breve del manual, activos oficiales y referencia aceptada: familia/peso tipográfico, tamaños por rol, colores por escena, variante del logo, área de protección, tratamiento de imágenes y comportamiento del movimiento. Registrar qué proviene del usuario/manual y qué es una propuesta.

Si falta el manual completo, respetar las reglas confirmadas y avanzar con cambios que no dependan de reglas desconocidas. Pedir solo la información necesaria para una elección pendiente. No afirmar cumplimiento del manual completo sin leerlo.

Diseñar un fotograma final legible antes de animarlo. Comprobar la fuente real dentro de CapCut: escribir una ruta a Poppins en JSON no demuestra que el editor la cargó. Si sustituye la fuente, corregir la carga o elegir una alternativa autorizada, sin presentar la sustitución como equivalente.

Dar a cada escena un foco y una acción que explique el mensaje. Elegir transiciones por continuidad de objeto, forma o posición y sincronizarlas con eventos relevantes de voz/música. Evitar añadir círculos, tarjetas, brillos o rebotes por defecto. Mantener el logo intacto y animar su capa completa solo de la forma permitida por la marca.

## Producción y revisión

1. Inspeccionar proyecto, activos, pistas, formato y duración. Mantener textos, medios y audio editables cuando sean parte del encargo.
2. Resolver y comprobar una escena representativa en CapCut antes de extender un tratamiento nuevo. Respetar las revisiones solicitadas; no crear aprobaciones adicionales para ajustes rutinarios ya autorizados.
3. Verificar entradas, estados de lectura, salidas y empalmes. Examinar logos sin deformación, fondos correctos, fuentes reales, recortes, contraste y zonas seguras de la plataforma.
4. Exportar localmente y revisar el archivo completo con sonido y muestras de cada escena. Abrir el borrador o aprobar un storyboard no valida el anuncio terminado.
5. Corregir errores observados y exportar de nuevo lo necesario. Si voz, ritmo, fuentes o fidelidad de marca siguen sin comprobarse, describir el resultado como borrador y señalar lo pendiente.

`scripts/audit_draft.py <draft_content.json>` audita recursos, fuentes declaradas y keyframes sin modificar archivos. Sus advertencias orientan la inspección; un resultado sin advertencias no certifica apariencia ni audio.

## Entrega

Entregar video verificado y proyecto editable solicitado. Informar duración, dimensiones y fps comprobados, conversiones posteriores y limitaciones de portabilidad de medios/fuentes. No llamar «premium» o «profesional» al resultado como sustituto de evidencia visual. Esta skill no autoriza compras, suscripciones, publicación, envío a terceros ni clonación de voz.
