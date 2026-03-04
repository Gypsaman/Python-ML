---
name: informe-de-investigacion
description: 
  Usa esta habilidad cuando el usuario pida investigar un tema y producir un
  informe escrito estructurado, libro blanco, documento de resumen o síntesis
  de literatura. Se activa con frases como: "escribe un informe sobre...",
  "resume la investigación sobre...", "dame un resumen de...", "compila
  hallazgos sobre...". NO usar para preguntas rápidas, búsquedas de un solo
  dato, ni tareas cuyo resultado sea código o una hoja de cálculo.
license: MIT
---

# Habilidad: Informe de Investigación

## Descripción General

Esta habilidad te guía para producir un informe de investigación bien estructurado y con fuentes citadas. Buscarás fuentes, sintetizarás hallazgos y producirás un documento pulido.

---

## Paso 1: Clarificar la Solicitud

Antes de buscar, identifica:

- **Tema**: ¿Cuál es el asunto central?
- **Alcance**: ¿Qué tan amplio o específico?
- **Audiencia**: ¿Experto técnico, directivo, público general?
- **Extensión**: ¿Resumen ejecutivo (1 página) o informe detallado (5–10 páginas)?
- **Formato**: ¿El resultado debe ser `.docx`, `.pdf` o Markdown?

Si alguno de estos puntos es ambiguo, haz al usuario una sola pregunta de aclaración antes de continuar.

---

## Paso 2: Estrategia de Investigación

1. Comienza con 2–3 consultas amplias para mapear el panorama
2. Identifica subtemas clave a partir de los resultados
3. Realiza consultas específicas de seguimiento para cada subtema
4. Obtén páginas completas de las 3–5 fuentes más relevantes (no solo fragmentos)
5. Prioriza: artículos revisados por pares > informes gubernamentales/institucionales > periodismo de calidad > blogs

**Mínimo de fuentes**: 5 para un informe corto, 10+ para uno detallado.

### Niveles de Calidad de Fuentes

| Nivel | Ejemplos | Nivel de Confianza |
|-------|----------|--------------------|
| Primario | PubMed, arXiv, datos gubernamentales | Alto |
| Secundario | Reuters, El País, Nature News | Medio-Alto |
| Terciario | Blogs de industria, artículos de LinkedIn | Usar con precaución |
| Evitar | Foros anónimos, sitios de contenido SEO | No citar |

---

## Paso 3: Reglas de Síntesis

- **Siempre parafrasea** — nunca reproduzcas más de 14 palabras textuales
- **Atribuye cada afirmación** — "Según [Fuente], ..."
- **Triangula**: Si solo una fuente hace una afirmación, márcala como no verificada
- **Muestra el desacuerdo**: Si las fuentes son contradictorias, presenta ambas posturas y señala la tensión

---

## Paso 4: Estructura del Informe

```
1. Resumen Ejecutivo       (150–200 palabras, sin tecnicismos)
2. Antecedentes y Contexto
3. Hallazgos Clave         (3–5 temas principales)
4. Análisis
5. Preguntas Abiertas
6. Conclusión
7. Referencias
```

---

## Paso 5: Lista de Verificación de Calidad

Antes de entregar el informe, verifica:

- [ ] Todas las afirmaciones están atribuidas a una fuente
- [ ] Ninguna sección es copiada textualmente de una fuente
- [ ] El Resumen Ejecutivo puede leerse de forma independiente (sin términos no definidos)
- [ ] La sección de Referencias está completa con URLs donde sea posible
- [ ] La extensión del informe corresponde al alcance solicitado
- [ ] El tono corresponde a la audiencia indicada

---

## Errores Conocidos a Evitar

| Error | Cómo Evitarlo |
|-------|---------------|
| Inventar citas | Solo cita fuentes obtenidas realmente mediante búsqueda |
| Resumir en exceso | Obtén páginas completas, no solo fragmentos |
| Desviarse del tema | Relee la solicitud original del usuario antes de escribir |
| Falso equilibrio | No inventes controversia donde existe consenso |
| Sesgo de actualidad | Revisa fechas de publicación; prefiere fuentes recientes pero señala las fundacionales |

---

## Formato de Salida

- **Markdown** — por defecto
- **`.docx`** — si el usuario menciona "Word", "documento" o "descargable"
- **`.pdf`** — si el usuario menciona "PDF" o "imprimible"

---

## Metadatos

```json
{
  "name": "informe-de-investigacion",
  "version": "1.2.0",
  "tools_required": ["web_search", "web_fetch"],
  "tools_optional": ["file_create"],
  "avg_token_cost": 4000,
  "max_recommended_depth": "10 fuentes",
  "compatible_models": ["claude-sonnet-4-20250514", "claude-opus-4-5"]
}
```
