# Operación nativa y fallos observados

## Preparación y guardado

Localizar CapCutKit por el proyecto/configuración existente; leer README y AGENTS. No fijar rutas del equipo del autor en una skill distribuida. La adaptación Windows usada anteriormente se probó con CapCut 9.3.0: verificar compatibilidad del formato interno en otras versiones.

Usar el backend que realiza cierre normal, respaldo e invalidación de cachés antes de escribir. Nunca modificar JSON mientras CapCut posee el proyecto. Si el usuario está trabajando en la interfaz, preservar su sesión y no reconstruir el proyecto para preparar una copia.

Para interfaz Windows usar computer-use y sus APIs soportadas. Los identificadores/coordenadas macOS no son portables. Observar la ventana antes de cada acción y refrescar después; no actuar sobre una captura anterior.

## Medidas, tipografía y proporciones

En un borrador 9:16 probado, posiciones se comportaron como coordenadas relativas a la mitad del lienzo: x=(cx-W/2)/(W/2), y=(H/2-cy)/(H/2). Es una observación de esa versión/schema, no una garantía. Calibrar con un elemento de tamaño/posición conocidos; no multiplicar medidas a ciegas.

Los tamaños de texto no equivalían a píxeles. Medir ancho con la fuente ayuda a prever desbordes, pero verificar la fuente real, peso, acentos, interlineado y saltos dentro de CapCut.

Dos canales ScaleX/ScaleY añadidos por el generador deformaron logos aunque la escala base fuera uniforme. Usar canales que la versión interprete correctamente o conservar escala estática y animar posición/opacidad/rotación. No corregirlo deformando la imagen fuente.

No duplicar canales del mismo property_type. Mantener keyframes dentro de la duración local del segmento. La integridad del JSON no demuestra movimiento visual correcto.

## Audio y exportación

Importar WAV/MP3 ya generados como audio local por interfaz o schema local comprobado. No heredar `extract_music` ni referencias de extracción de un segmento ajeno: pueden activar requisitos Pro que no corresponden al material importado. No alterar flags de licencia ni saltar barreras de pago; quitar o reemplazar operaciones Pro si no están autorizadas.

Exportar al disco; evitar sincronización/subida no solicitada y publicación TikTok/YouTube/Share. Si aparece otra pantalla, observar de nuevo antes de pulsar.

Comprobar duración, dimensiones, fps, códecs y audio esperado con ffprobe. Decodificar para detectar errores. Si se convierte a H.264 por compatibilidad, conservar master y declarar la conversión.

Respaldar proyecto y Resources. Las rutas absolutas/fuentes pueden requerir revinculación en otro equipo. No llamar portable a un ZIP solo porque contiene draft_content.json.
