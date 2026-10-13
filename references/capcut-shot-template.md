# Receta por plano

Es una especificación de edición; NO un borrador CapCut importable. Usar coordenadas relativas de diseño y convertirlas después de calibrar la versión nativa.

```yaml
shot_id: S03
in: '00:09.00'
out: '00:14.00'
message: 'Beneficio principal verificable'
voiceover: 'Libreto exacto aprobado'
on_screen_text: 'Claim breve verificado'
visual: 'Nombre de activo auténtico del proyecto'
layers:
  - id: bg
    kind: solid
    color: '#0B1020' # propuesta; reemplazar con perfil de marca
  - id: title
    kind: editable_text
    font: 'Familia y peso de marca comprobados en CapCut'
    final_position_pct: [12, 32] # indicar anclaje y origen
    anchor: 'superior izquierdo; origen superior izquierdo del lienzo'
    animation:
      property: 'position_y + opacity'
      from: '+5% del alto respecto a destino / 0%'
      to: 'destino / 100%'
      duration_seconds: 0.4
      duration_frames_at_30fps: 12
      easing: 'ease-out si disponible; keyframes intermedios si no'
      hold: 'hasta fin del beat de lectura'
  - id: product
    kind: image_or_video
    asset: 'ruta o ID comprobado'
    preserve_aspect_ratio: true
    animation:
      property: 'uniform_scale + opacity'
      from: '96% / 0%'
      to: '100% / 100%'
      duration_frames_at_30fps: 16
transition_out: 'match cut con posición/dirección del siguiente plano'
sound: 'click puntual; voz prioritaria'
capcut_capabilities: 'controles efectivamente comprobados'
fallback: 'operaciones alternativas sin cambiar editor ni marca'
checks: ['fuente real', 'legibilidad', 'marca', 'proporciones', 'safe zone', 'audio']
status: 'propuesta'
```

Registrar estado inicial, keyframes intermedios/finales, pista/capa, asset, curva, duración, stagger, reposo, salida y fallback. Mantener todas las muestras dentro de la duración del segmento, redondeadas a cuadros reales.
