# Plan de Actualización: Sesiones 13-14 sobre Transformers

## ✅ COMPLETADO

### **Sesión 14: Transformers II - Arquitectura Completa**
Se ha creado un notebook completamente nuevo (`MLPy-sesion14.ipynb`) con:

1. **Revisión rápida de atención** (scaled dot-product)
2. **Multi-head attention** - Implementación manual desde cero
3. **Positional encoding** - Codificación sinusoidal con visualización
4. **Feedforward network** - Red MLP independiente por token
5. **Layer Normalization** - Con conexiones residuales
6. **Bloque Encoder completo** - Ensambla todo
7. **Máscara causal** - Para decoders autoregresivos
8. **Ejemplo práctico**: Predicción character-level
   - Dataset simple de texto
   - Entrenamiento completo
   - Generación de texto

**Características clave:**
- 📝 Todo implementado manualmente (sin usar `nn.TransformerEncoder`)
- 🎯 Progresión pedagógica clara
- 💻 Código funcional y ejecutable
- 📊 Visualizaciones de máscaras y encoding
- 🚀 Tarea práctica de entrenamiento end-to-end

---

## 🔄 PENDIENTE: Mejoras a Sesión 13

### **Sesión 13: Transformers I - Atención**
El notebook actual está bien, pero se puede mejorar agregando:

#### Adiciones recomendadas:

1. **Sección de Multi-Head Attention (Conceptual)**
   - Mostrar cómo dividir Q, K, V en cabezas
   - Visualizar atención de diferentes cabezas
   - Preparar para Session 14

2. **Positional Encoding (Implementación)**
   - Agregar función sinusoidal
   - Visualizar patrones de encoding
   - Mostrar cómo se suma al embedding

3. **Completar sección de Causal Masking**
   - Ya está iniciada al final
   - Agregar más explicación
   - Comparar atención con/sin máscara

#### Código sugerido para agregar:

```python
## 7) Multi-Head Attention (Conceptual)

def split_into_heads(x, num_heads):
    """Divide embedding dimension into heads"""
    batch_size, seq_len, d_model = x.size()
    d_k = d_model // num_heads
    return x.view(batch_size, seq_len, num_heads, d_k).transpose(1, 2)

# Ejemplo: dividir en 2 cabezas
X_multi = torch.randn(1, 6, 16)
num_heads = 2
X_heads = split_into_heads(X_multi, num_heads)
print(f"Shape original: {X_multi.shape}")
print(f"Shape con cabezas: {X_heads.shape}")  # (batch, num_heads, seq_len, d_k)

# Cada cabeza puede aprender un patrón diferente
```

```python
## 8) Positional Encoding

def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len).unsqueeze(1).float()
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe

# Visualización
pe = get_positional_encoding(20, 16)
plt.imshow(pe.T, aspect='auto', cmap='RdBu')
plt.colorbar()
plt.title('Positional Encoding Pattern')
plt.xlabel('Position')
plt.ylabel('Embedding dimension')
plt.show()

# Agregar a embeddings
X_with_pos = X + pe[:X.size(0), :]
```

---

## 📊 Comparación: Sesión 13 vs 14

| Aspecto | Sesión 13 | Sesión 14 |
|---------|-----------|-----------|
| **Enfoque** | Mecanismo de atención | Arquitectura completa |
| **Nivel** | Conceptual + básico | Implementación completa |
| **Q, K, V** | ✅ Manual | ✅ Con Linear layers |
| **Atención** | ✅ Scaled dot-product | ✅ + Multi-head |
| **Positional Encoding** | ⚠️ Describir (mejorar) | ✅ Implementado + viz |
| **FFN** | ❌ No | ✅ Implementado |
| **LayerNorm** | ❌ No | ✅ Implementado |
| **Residuales** | ❌ No | ✅ Implementado |
| **Máscara causal** | ⚠️ Iniciado | ✅ Completo |
| **Ejemplo práctico** | Visualización | ✅ Entrenamiento completo |

---

## 🎯 Objetivos de aprendizaje

### **Al terminar Sesión 13**, el estudiante debe:
- ✅ Entender Q, K, V
- ✅ Comprender scaled dot-product attention
- ✅ Visualizar matrices de atención
- ✅ Conocer máscaras causales
- 🆕 Entender multi-head (conceptualmente)
- 🆕 Conocer positional encoding

### **Al terminar Sesión 14**, el estudiante debe:
- ✅ Implementar multi-head attention manualmente
- ✅ Construir un transformer encoder completo
- ✅ Entender layer norm + residuales
- ✅ Aplicar máscaras causales
- ✅ Entrenar un modelo transformer real
- ✅ Generar secuencias

---

## 📝 Actualizaciones de slides

### **Sesión 13 (slides actuales):**
Estado: ✅ Bien estructuradas
- Mantener estructura conceptual actual
- Agregar slide sobre multi-head (preparación)
- Agregar slide sobre positional encoding

### **Sesión 14 (slides actuales):**
Estado: ⚠️ Demasiado densos
- **Reducir contenido** por slide
- **Enfocar en diagrams**: Bloque encoder, residuales, etc.
- Agregar slide de "receta del transformer"
- Finalizar con "por qué escalan" (paralelismo)

---

## 🚀 Próximos pasos

1. ✅ **Sesión 14**: Completada
2. ⏳ **Sesión 13**: Agregar secciones sugeridas arriba
3. ⏳ **Slides 13**: Actualizar con nuevos temas
4. ⏳ **Slides 14**: Simplificar y reorganizar

---

## 💡 Notas adicionales

### Dataset para Sesión 14:
- **Character-level**: Texto simple en español
- **Pros**: Fácil de entender, vocabulario pequeño
- **Cons**: No es state-of-the-art
- **Alternativa futura**: Usar tokenizador BPE + dataset real

### Extensiones posibles:
- Agregar **decoder completo** (cross-attention)
- Implementar **attention weights visualization** interactiva
- Mostrar **scaling laws** (parámetros vs performance)
- Comparar con **RNN/LSTM** en misma tarea

---

## 📚 Referencias usadas

- [Attention is All You Need](https://arxiv.org/abs/1706.03762) - Paper original
- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) - Visualizaciones
- [Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) - Implementación didáctica

---

**Estado actual**: ✅ Sesión 14 completada | ⏳ Sesión 13 requiere mejoras menores
