#  Explicación detallada de la divergencia KL (Kullback-Leibler)

-  a menudo llamada “distancia KL”, aunque **no es una métrica verdadera**

---

# 1) Qué mide la divergencia KL

Supongamos que tenemos dos distribuciones de probabilidad sobre el mismo espacio $->->\mathcal{X}$:

- $ P(x) $: la distribución **verdadera** o de referencia  
- $ Q(x) $: una **aproximación** a $P(x)$

La **divergencia KL de $Q$ con respecto a $P$** responde a la pregunta:

> ¿Cuánta “información extra” o “sorpresa adicional” introduzco si uso $Q$ en lugar de $P$?

Se escribe comúnmente como:

$$
D_{\mathrm{KL}}(P\;\|\;Q)
$$

y se lee: “divergencia KL de $Q$ con respecto a $P$”.

---

# 2) Definición (caso discreto)

Si $P$ y $Q$ son distribuciones discretas sobre resultados $x \in ->->\mathcal{X}$, entonces:

$$
\boxed{
D_{\mathrm{KL}}(P\;\|\;Q)
=
\sum_{x \in ->->\mathcal{X}} P(x)\,\log \frac{P(x)}{Q(x)}
}
$$

### Convenciones importantes:
- La base del logaritmo determina las unidades:
  - Base 2 -> **bits**
  - Base $e$ -> **nats**
- Se asume que:
  - Si $P(x) = 0$, el término aporta $0$ (por continuidad del límite).
  - Si $P(x) > 0$ pero $Q(x) = 0$, entonces $D_{\mathrm{KL}} = \infty$.

---

# 3) Definición (caso continuo)

Si $p(x)$ y $q(x)$ son **densidades de probabilidad** (PDFs), entonces:

$$
\boxed{
D_{\mathrm{KL}}(p\;\|\;q)
=
\int p(x)\,\log \frac{p(x)}{q(x)} \, dx
}
$$

Es la misma idea que en el caso discreto, pero con integrales en lugar de sumas.

---

# 4) Derivación desde la razón de verosimilitudes logarítmica

Partimos del logaritmo de la razón:

$$
\log \frac{P(x)}{Q(x)} = \log P(x) - \log Q(x)
$$

Tomamos la esperanza bajo $P(x)$:

$$
D_{\mathrm{KL}}(P\;\|\;Q)
= ->\mathcal{E}_{x \sim P} \left[ \log \frac{P(x)}{Q(x)} \right]
$$

Expandiendo:

$$
D_{\mathrm{KL}}(P\;\|\;Q)
= ->\mathcal{E}_{P}[\log P(x)] - ->\mathcal{E}_{P}[\log Q(x)]
$$

Esta forma es extremadamente útil en teoría de la información y aprendizaje automático.

---

# 5) Conexión con entropía y entropía cruzada

## (a) Entropía de $P$

La entropía de Shannon de $P$ es:

$$
H(P) = - \sum_x P(x)\log P(x)
$$

O en forma de esperanza:

$$
H(P) = - ->\mathcal{E}_{P}[\log P(x)]
$$

---

## (b) Entropía cruzada $H(P,Q)$

Definimos la **entropía cruzada** entre $P$ y $Q$ como:

$$
H(P,Q) = - ->\mathcal{E}_{P}[\log Q(x)]
= - \sum_x P(x)\log Q(x)
$$

---

## (c) KL como “Entropía cruzada menos entropía”

Sustituyendo en la expresión anterior:

$$
\begin{aligned}
D_{\mathrm{KL}}(P\;\|\;Q)
&= ->\mathcal{E}_{P}[\log P(x)] - ->\mathcal{E}_{P}[\log Q(x)] \\
&= -H(P) + H(P,Q)
\end{aligned}
$$

$$
\boxed{
D_{\mathrm{KL}}(P\;\|\;Q)
= H(P,Q) - H(P)
}
$$

### Interpretación:
- $H(P)$: incertidumbre intrínseca de la distribución verdadera  
- $H(P,Q)$: incertidumbre si “fingimos” que los datos provienen de $Q$  
- Su diferencia es el **costo por usar $Q$ en lugar de $P$**.

---

# 6) No negatividad (teorema clave)

$$
\boxed{
D_{\mathrm{KL}}(P\;\|\;Q) \ge 0
}
$$

con igualdad **si y solo si** $P(x) = Q(x)$ para todo $x$.

## Demostración (bosquejo con Jensen)

Escribimos:

$$
D_{\mathrm{KL}}(P\;\|\;Q)
= \sum_x P(x)\log \frac{P(x)}{Q(x)}
= - \sum_x P(x)\log \frac{Q(x)}{P(x)}
$$

Definimos $r(x) = \frac{Q(x)}{P(x)}$. Entonces:

$$
D_{\mathrm{KL}} = - ->\mathcal{E}_{P}[\log r(x)]
$$

Como $\log$ es una función cóncava, por la desigualdad de Jensen:

$$
->\mathcal{E}_{P}[\log r(x)] \le \log ->\mathcal{E}_{P}[r(x)]
$$

Pero:

$$
->\mathcal{E}_{P}[r(x)] = \sum_x P(x)\frac{Q(x)}{P(x)} = \sum_x Q(x) = 1
$$

Luego:

$$
->\mathcal{E}_{P}[\log r(x)] \le \log 1 = 0
$$

Por lo tanto:

$$
D_{\mathrm{KL}} = - ->\mathcal{E}_{P}[\log r(x)] \ge 0
$$

---

# 7) Asimetría (por qué KL no es una distancia)

En general:

$$
D_{\mathrm{KL}}(P\;\|\;Q) \ne D_{\mathrm{KL}}(Q\;\|\;P)
$$

### Intuición:
- $D_{\mathrm{KL}}(P\;\|\;Q)$: costo de aproximar $P$ **con** $Q$
- $D_{\mathrm{KL}}(Q\;\|\;P)$: costo de aproximar $Q$ **con** $P$

Son preguntas diferentes.

---

# 8) Ejemplo: dos distribuciones Bernoulli

Sea:

$$
P = \text{Bernoulli}(p), \quad Q = \text{Bernoulli}(q)
$$

Entonces:

$$
D_{\mathrm{KL}}(P\;\|\;Q)
=
p \log \frac{p}{q}
+
(1-p) \log \frac{1-p}{1-q}
$$

Esto proviene directamente de aplicar la definición discreta de KL sobre $x \in \{0,1\}$.

---

# 9) KL entre dos distribuciones normales (caso clave)

Sea:

$$
P = ->->\mathcal{N}(\mu_1, \sigma_1^2), \quad
Q = ->->\mathcal{N}(\mu_2, \sigma_2^2)
$$

Entonces:

$$
\boxed{
D_{\mathrm{KL}}(P\;\|\;Q)
=
\frac{1}{2}
\left[
\frac{\sigma_1^2}{\sigma_2^2}
+ \frac{(\mu_2 - \mu_1)^2}{\sigma_2^2}
- 1
+ \log \frac{\sigma_2^2}{\sigma_1^2}
\right]
}
$$

Esta expresión es fundamental en **Autoencoders Variacionales (VAEs)**.

---

# 10) Por qué KL aparece en Machine Learning

## (a) Inferencia variacional

Queremos aproximar una posterior intratable $p(z|x)$ con una distribución más simple $q(z)$. Para ello minimizamos:

$$
D_{\mathrm{KL}}(q(z)\;\|\;p(z|x))
$$

---

## (b) Función de pérdida en VAE

El objetivo estándar de un VAE es:

$$
->->\mathcal{L}
=
\underbrace{->\mathcal{E}_{q(z|x)}[\log p(x|z)]}_{\text{Término de reconstrucción}}
-
\underbrace{D_{\mathrm{KL}}(q(z|x)\;\|\;p(z))}_{\text{Término de regularización}}
$$

El término KL obliga a que la distribución latente aprendida sea cercana a un prior (típicamente normal estándar).

---

# 11) Relación con otras divergencias

KL es un caso particular de las **f-divergencias**. Dos medidas relacionadas son:

### (a) Divergencia de Jensen–Shannon (simétrica)

Definimos $M = \tfrac{1}{2}(P+Q)$. Entonces:

$$
\mathrm{JS}(P,Q)
=
\frac{1}{2}D_{\mathrm{KL}}(P\;\|\;M)
+
\frac{1}{2}D_{\mathrm{KL}}(Q\;\|\;M)
$$

JS es simétrica y acotada.

### (b) Distancia de variación total

$$
\mathrm{TV}(P,Q)
=
\frac{1}{2}\sum_x |P(x) - Q(x)|
$$

Es una noción diferente de “distancia”, basada en diferencias absolutas y no en logaritmos.

---

# Cómo se enlaza la divergencia KL con el ELBO

A continuación se presenta la relación entre **KL** y **ELBO** 

---

# 1) Punto de partida: el problema que da origen al ELBO

En inferencia bayesiana queremos el posterior verdadero:

$$
p(z|x) = \frac{p(x,z)}{p(x)}
$$

El problema es que la **evidencia marginal**

$$
p(x) = \int p(x,z)\,dz
$$

suele ser intratable en modelos complejos.

**Idea clave de la inferencia variacional:**  
Aproximamos $p(z|x)$ con una distribución más simple $q_\phi(z|x)$ y ajustamos $q_\phi$ para que sea lo más cercana posible a $p(z|x)$ usando la divergencia KL.

---

# 2) El objetivo variacional: minimizar KL al posterior

Planteamos explícitamente:

$$
\min_{\phi} \; D_{\mathrm{KL}}\!\left(q_\phi(z|x)\;\|\;p(z|x)\right)
$$

Por definición:

$$
D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z|x)\right)
=
->\mathcal{E}_{q(z|x)}\!\left[\log \frac{q(z|x)}{p(z|x)}\right]
$$

Sustituimos $p(z|x) = \frac{p(x,z)}{p(x)}$:

$$
D_{\mathrm{KL}}(q(z|x)\|p(z|x))
=
->\mathcal{E}_{q(z|x)}\!\left[\log q(z|x) - \log p(x,z) + \log p(x)\right]
$$

Como $\log p(x)$ no depende de $z$, sale de la esperanza:

$$
D_{\mathrm{KL}}(q(z|x)\|p(z|x))
=
->\mathcal{E}_{q}[\log q(z|x)] - ->\mathcal{E}_{q}[\log p(x,z)] + \log p(x)
$$

Reordenando:

$$
\log p(x)
=
D_{\mathrm{KL}}(q(z|x)\|p(z|x))
+
\Big(
->\mathcal{E}_{q}[\log p(x,z)] - ->\mathcal{E}_{q}[\log q(z|x)]
\Big)
$$

Definimos el término entre paréntesis como **ELBO**:

$$
\boxed{
\log p(x) = \text{ELBO} + D_{\mathrm{KL}}\!\left(q(z|x)\|p(z|x)\right)
}
$$

---

# 3) Definición formal del ELBO

A partir de la ecuación anterior:

$$
\boxed{
\text{ELBO}(q)
=
->\mathcal{E}_{q(z|x)}[\log p(x,z)]
-
->\mathcal{E}_{q(z|x)}[\log q(z|x)]
}
$$

De forma equivalente:

$$
\boxed{
\text{ELBO}(q)
=
->\mathcal{E}_{q(z|x)}[\log p(x|z)]
-
D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z)\right)
}
$$

---

# 4) Separando el término conjunto $p(x,z)$

Usamos la descomposición bayesiana:

$$
p(x,z) = p(x|z)\,p(z)
$$

Entonces:

$$
->\mathcal{E}_{q}[\log p(x,z)]
=
->\mathcal{E}_{q}[\log p(x|z)] + ->\mathcal{E}_{q}[\log p(z)]
$$

Sustituimos en el ELBO original:

$$
\text{ELBO}
=
->\mathcal{E}_{q}[\log p(x|z)]
+
->\mathcal{E}_{q}[\log p(z)]
-
->\mathcal{E}_{q}[\log q(z|x)]
$$

Agrupamos los dos últimos términos:

$$
->\mathcal{E}_{q}[\log p(z)] - ->\mathcal{E}_{q}[\log q(z|x)]
=
- D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z)\right)
$$

Por lo tanto:

$$
\boxed{
\text{ELBO}
=
\underbrace{->\mathcal{E}_{q(z|x)}[\log p(x|z)]}_{\text{Reconstrucción}}
-
\underbrace{D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z)\right)}_{\text{Regularización KL}}
}
$$

---

# 5) Interpretación conceptual

## (1) Término de reconstrucción  

$$
->\mathcal{E}_{q(z|x)}[\log p(x|z)]
$$

- Mide qué tan bien el modelo generativo $p(x|z)$ puede reconstruir $x$ desde $z$.
- En VAEs:
  - MSE si $p(x|z)$ es gaussiano.
  - Binary Cross-Entropy si $p(x|z)$ es Bernoulli.

Empuja al modelo a reconstruir bien los datos.

---

## (2) Término KL  

$$
D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z)\right)
$$

- Fuerza a que $q(z|x)$ sea cercano al prior $p(z)$ (típicamente $->->\mathcal{N}(0,I)$).
- Actúa como regularización del espacio latente.

Empuja el espacio latente a ser continuo y estructurado.

---

# 6) Conexión final entre KL y ELBO

$$
\boxed{
\log p(x)
=
\text{ELBO}
+
D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z|x)\right)
}
$$

Como $D_{\mathrm{KL}} \ge 0$:

$$
\boxed{
\text{ELBO} \le \log p(x)
}
$$

Por eso se llama **Evidence Lower Bound** (cota inferior de la evidencia).

Maximizar el ELBO es equivalente a minimizar la KL al posterior verdadero:

$$
\max_q \; \text{ELBO}
\quad \Longleftrightarrow \quad
\min_q \; D_{\mathrm{KL}}\!\left(q(z|x)\;\|\;p(z|x)\right)
$$

---

# 7) En el contexto práctico del VAE

En un VAE típico:

- Encoder: $q_\phi(z|x) = ->->\mathcal{N}(\mu_\phi(x), \sigma_\phi(x))$
- Prior: $p(z) = ->->\mathcal{N}(0,I)$
- Decoder: $p_\theta(x|z)$

La pérdida que se **minimiza** en práctica es:

$$
->->\mathcal{L}(\theta,\phi)
=
-\text{ELBO}
=
\underbrace{D_{\mathrm{KL}}\!\left(q_\phi(z|x)\;\|\;p(z)\right)}_{\text{Penalización KL}}
-
\underbrace{->\mathcal{E}_{q_\phi(z|x)}[\log p_\theta(x|z)]}_{\text{Reconstrucción}}
$$

---
