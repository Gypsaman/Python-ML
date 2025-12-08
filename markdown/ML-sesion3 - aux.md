## Importancia de las derivadas en redes neuronales

**Idea clave**

Las derivadas determinan **cómo cambia la salida** de la red cuando cambiamos ligeramente los pesos.  
Sin derivadas no podríamos ajustar los parámetros → la red no podría aprender.

**En cada capa**

Dado:
- $z = Wx + b$
- $a = f(z)$

Las derivadas que necesitamos son:

$$
\frac{\partial a}{\partial z} = f'(z)
\qquad\text{(derivada de la activación)}
$$

$$
\frac{\partial z}{\partial W} = x
\qquad\text{(cómo afecta el peso al valor interno)}
$$

Estas derivadas permiten calcular el gradiente del error respecto a cada parámetro.

### ¿Por qué es crítico?

- Las activaciones determinan **cómo se propaga el gradiente** hacia atrás.  
- Funciones como Sigmoid y Tanh pueden causar **gradientes muy pequeños** (“vanishing gradient”).  
- ReLU, GELU, Swish y ELU mantienen gradientes útiles en la mayor parte del dominio.  
- Sin derivadas bien comportadas, el aprendizaje se vuelve lento o imposible.

### Visualización

\centering
\begin{tikzpicture}[scale=0.8,>=latex]
  % Ejes
  \draw[->] (-3,0) -- (3,0) node[right] {$z$};
  \draw[->] (0,-1) -- (0,2.5) node[above] {$f'(z)$};

  % Derivada de ReLU
  \draw[thick, blue] (-3,0) -- (0,0);
  \draw[thick, blue] (0,1.5) -- (3,1.5) node[right] {\small $f'(z)$ para ReLU};

  % Comment
  \node at (0,-1.2) {\small Derivadas grandes → aprendizaje rápido.};
  \node at (0,-1.8) {\small Derivadas cercanas a 0 → gradientes que desaparecen.};
\end{tikzpicture}
