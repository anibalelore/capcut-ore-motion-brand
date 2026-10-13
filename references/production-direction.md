# Dirección de producción — versión 1.1.0

Integra las mejoras de dirección suministradas por el usuario: movimiento con intención, timing por encima de efectos y referencia de calidad de motion publicitario/After Effects ejecutada en CapCut. Los valores siguientes son heurísticas de producción, no estándares de plataformas ni capacidades garantizadas.

## Brief y dirección de arte

Identificar marca/producto, promesa verificable, público/país, objetivo, CTA, duración/canal, energía, materiales, idioma, libreto, plataforma/versión de CapCut y fuentes disponibles. Defaults solo si falta información: 9:16, 1080×1920, 30 fps, 30 s, español latinoamericano, tech-editorial. Adaptar a Web/Mobile si se solicita.

Antes de construir una pieza, dejar guion A/V, dirección de arte, storyboard y receta de edición. Analizar referencia por ritmo, jerarquía, trayectorias, paleta, transiciones y pausas, adaptándola de forma original. Mantener una idea focal y un movimiento principal por escena, con detalles secundarios discretos. Compartir grid, radios, sombras, curvas y motivo recurrente. No acumular geometría por llenar espacio.

## Tipografía y layout

Priorizar fuentes de marca, comprobar licencia y carga real en CapCut, incluyendo áéíóúñ¿¡. Como alternativas propuestas, no necesariamente instaladas:

| Dirección | Titulares | Secundario |
|---|---|---|
| Premium tech | Sora SemiBold/Bold | Inter Regular/Medium |
| Editorial contemporánea | Space Grotesk Bold | DM Sans Regular/Medium |
| Minimalista cálida | Manrope Bold | Manrope Regular |
| Comercial contundente | Archivo Black | Inter Medium |
| Editorial sofisticada | Fraunces SemiBold | DM Sans Regular |

Usar normalmente hasta dos familias y dos o tres pesos; justificar excepciones editoriales. Titulares de tres a siete palabras son una heurística, no una obligación. Ajustar saltos, ancho de caja, tracking/kerning e interlineado; evitar viudas, palabras cortadas y mayúsculas largas. No tratar unidades de CapCut como px/pt idénticos.

Como punto de partida vertical, márgenes de diseño de 8–12% del ancho, luego validar overlays reales del placement. No presentarlos como safe zones oficiales. Proteger texto/CTA cerca del borde inferior y derecho. Revisar a tamaño de teléfono. Objetivo editorial de contraste: 4.5:1 para texto regular y 3:1 para texto grande, aplicados al fondo real y sin declarar certificación WCAG del video. Un logo siempre debe respetar su manual y seguir siendo reconocible.

Paletas opcionales para marcas sin sistema: dark #0B1020 con blanco/#E5E7EB y acento #8B5CF6; light #F8FAFC con #111827 y acento #7C3AED. No usar estos acentos en texto pequeño sin medir contraste ni sustituir una marca existente.

## Narrativa y sonido

Distribución orientativa 30 s: hook 0–3; contexto 3–9; mecanismo 9–18; beneficios 18–25; resolución/CTA 25–30. Priorizar libreto, música e historia reales por encima de esta distribución. Mostrar dos o tres ventajas verificadas; no inventar precios, cifras, garantías o liderazgo. El texto visible puede resumir la voz sin repetirla entera; no reescribir locución exacta.

Marcar beats, subbeats y reposos antes de decorar. Sincronizar cortes con cambio narrativo, inflexión, acción UI o acento musical. Whooshes/clicks puntúan acciones, nunca tapan voz. Evitar strobe y flashes repetitivos. Mantener planos estables durante lectura.

## Timing y recetas

La intención determina preparación, recorrido, velocidad y asentamiento. Anticipación prepara una acción; overshoot sobrepasa discretamente el destino y asienta; follow-through prolonga una parte secundaria; overlapping retrasa elementos relacionados; arcos evitan trayectorias mecánicas. Elegir solo los principios que explican el plano, sin aplicarlos a todo.

| Acción | Tiempo inicial | A 30 fps aprox. |
|---|---|---|
| Entrada titular | 0.25–0.45 s | 8–14 cuadros |
| Entrada UI | 0.35–0.60 s | 11–18 cuadros |
| Stagger | 0.06–0.14 s | 2–4 cuadros |
| Cambio de foco | 0.40–0.80 s | 12–24 cuadros |
| Salida secundaria | 0.16–0.30 s | 5–9 cuadros |
| Hero reveal | 0.60–1.10 s | 18–33 cuadros |

Convertir por segundos al cambiar fps. Redondear a cuadros reales y adaptar a lectura/ritmo.

| Receta | Operación CapCut | Fallback comprobable |
|---|---|---|
| Slide + fade | Posición Y desde +4–7% del alto, alpha 0; destino/100% en 10–14 cuadros y reposo | Keyframes intermedios de posición/alpha si no hay easing |
| Pop de UI | Escala 94–97% → 101–102% → 100%, alpha 0 → 100% | Escala uniforme probada; sin overshoot si deforma el activo |
| Reveal | Máscara animada que descubre texto/UI | Capas y oclusor sólido para fondo uniforme; overlay pre-renderizado solo si autorizado y compatible |
| Match de producto | Igualar posición, dirección y escala en dos clips | Corte por correspondencia sin transición de biblioteca |
| Kinetic emphasis | Una palabra clave gana 4–8% de escala o acento y asienta | Separar palabra en texto editable; respetar tracking y baseline |
| Arco/seguimiento | Posiciones X/Y intermedias y elemento secundario retrasado | Muestrear recorrido y verificar a 1×; no prometer path editor |

No confundir speed curve (retiming del clip) con easing de transformaciones. Verificar controles en el clip/versión concreta. Usar motion blur moderado solo en desplazamientos rápidos, con nitidez recuperada en reposo; omitirlo si no está disponible. Máscaras, gráficos y efectos Free/Pro varían: declarar restricciones y alternativas, no inventar botones/API.

## Salidas y evaluación

Seis apartados: brief; dirección de arte; tabla A/V/storyboard; receta CapCut; export/deliverables; auditoría. Ver [plantilla por plano](capcut-shot-template.md) y [ejemplo 30 s](../examples/spot-30s-example.md). MP4/H.264 1080×1920/30 fps es un punto inicial de compatibilidad, no un requisito de todos los canales.

| Dimensión interna | Puntos |
|---|---:|
| Narrativa, hook y claridad | 20 |
| Tipografía y legibilidad | 20 |
| Composición y marca | 20 |
| Timing y continuidad | 20 |
| Audio/sincronía/técnica | 10 |
| Accesibilidad/zonas/licencias | 10 |

Umbral interno del usuario: ≥90/100 y cero críticos; no acreditación externa. Si falta evidencia, marcar «no evaluado», no sumar puntos imaginarios. Fallos críticos: logo alterado, texto ilegible/error visible, promesa no verificada, recurso sin permiso/licencia aplicable, UI tapando contenido esencial, flashes peligrosos, audio inaudible, negros accidentales o export incorrecto. Reparar o entregar como borrador con pendientes claros.

Antes de declarar terminado: revisar todo a 1×, primer segundo/primeros tres/último segundo, cada titular al tamaño mínimo objetivo, frame más cargado por escena, logos/tildes/números/UI/CTA, audio con auriculares y altavoz y MP4 exportado. Indicar «propuesta», «verificado en editor» o «verificado tras exportar» según evidencia real. No declarar pruebas de móvil/escucha que no se hicieron.
