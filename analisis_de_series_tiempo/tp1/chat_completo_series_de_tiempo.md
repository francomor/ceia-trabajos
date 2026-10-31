# Transcripción de la conversación — Primer TP de Análisis de Series de Tiempo

**Fecha:** 31 de octubre de 2026  
**Tema:** Resolución guiada de los ejercicios 1, 2 y 3.  
**Formato:** Mensajes ordenados cronológicamente. Las expresiones matemáticas están en LaTeX para facilitar su visualización en Markdown.

> **Nota sobre adjuntos:** En la conversación original se compartieron capturas de los enunciados y los archivos `PrimerTP_AST_1_MIA_4Co2026-a2533.pdf`, `Análisis_de_Series_de_Tiempo_2025_Clases_1_2.pdf`, `Analisis-de-Series-de-Tiempo-I-fundamentos-estadisticos.pdf` y una copia de las clases. Los enunciados de las imágenes se transcriben aquí. Un esquema gráfico mostrado por el asistente se describe en texto.

---

## Ejercicio 1 — Distribución normal de un proceso trigonométrico

### Usuario

**[Imagen adjunta: enunciado del ejercicio 1]**

> **1. (4 puntos) Sea:**
>
> $$Y_t=R\cos(2\pi(ft+\Phi))$$
>
> una serie de tiempo, donde $R$ y $\Phi$ son variables aleatorias independientes y $f$ es una frecuencia fija. La fase $\Phi$ se distribuye uniforme sobre el intervalo $(0,1)$, mientras que la amplitud $R$ tiene una distribución de Rayleigh con densidad $f(r)=re^{-r^2/2}$ para $r>0$. Muestre que, para todo $t$, $Y_t$ tiene una distribución normal.
>
> Pista: Defina $X=R(2\pi(ft+\Phi))$ y $X=R\cos(2\pi(ft+\Phi))$ y utilice la relación $X^2+Y^2=R^2$ para calcular la densidad conjunta de $(X,Y)$ a partir de la densidad conjunta de $(R,\Phi)$.

ayudame a resolver el primer ejecricio no quiero que lo resuleves sino que me guies, como puedo arrancar? adjunto esta el material de las clases

### Asistente

Vamos a resolverlo paso a paso, sin adelantarnos a la solución. La idea es que vos vayas haciendo las cuentas y yo te vaya guiando.

Revisé el material que adjuntaste. En la **página 10 de *Análisis de Series de Tiempo I*** aparece un proceso trigonométrico muy parecido al de este ejercicio.

## Paso 1. Entender qué nos están pidiendo

Tenemos:

$$Y_t=R\cos(2\pi(ft+\Phi))$$

Donde:

- $R$ es una variable aleatoria con distribución de Rayleigh.
- $\Phi$ es una variable aleatoria uniforme en $(0,1)$.
- $R$ y $\Phi$ son independientes.
- $f$ es una constante.

Nos piden demostrar que **para cualquier instante $t$, la variable $Y_t$ sigue una distribución normal**.

Esto significa que queremos llegar a una densidad de la forma:

$$f_{Y_t}(y)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(y-\mu)^2}{2\sigma^2}}$$

## Paso 2. ¿Por dónde arrancamos?

El ejercicio nos da una pista: utilizar una transformación de variables.

La idea es interpretar $R$ como un radio y $2\pi(ft+\Phi)$ como un ángulo.

**[Esquema en el chat original: coordenadas polares, con radio $R$, ángulo $\theta$, componente horizontal $R\cos\theta$ y componente vertical $R\sin\theta$.]**

La pista del enunciado parece tener un error tipográfico. Podemos definir:

$$\begin{aligned}
X&=R\sin(2\pi(ft+\Phi))\\
Y&=R\cos(2\pi(ft+\Phi))
\end{aligned}$$

Así se cumple:

$$X^2+Y^2=R^2$$

Nuestra estrategia será obtener primero la densidad conjunta $f_{X,Y}(x,y)$ y después encontrar la densidad marginal de $Y$.

## Paso 3. Tu primera cuenta

Antes de transformar las variables, necesitamos conocer la **densidad conjunta de $R$ y $\Phi$**.

Recordá que, si dos variables aleatorias son independientes:

$$\boxed{f_{R,\Phi}(r,\phi)=f_R(r)\cdot f_\Phi(\phi)}$$

El enunciado ya nos dice que:

$$f_R(r)=re^{-r^2/2},\qquad r>0$$

**Ahora te toca a vos:**

Si $\Phi\sim U(0,1)$, ¿cuánto vale $f_\Phi(\phi)$ dentro del intervalo $(0,1)$?

Y, usando eso, ¿cómo te quedaría la densidad conjunta $f_{R,\Phi}(r,\phi)$?

Respondeme esas dos cosas y seguimos con el cambio de variables y el jacobiano, que es la parte central del ejercicio.

### Usuario

es 1 la de la uniforme. entonces quedaria solo la de r para todo r > 0 y thihta entre 0<thihta<1

### Asistente

¡Exactamente! Está perfecto.

Como $R$ y $\Phi$ son independientes, la densidad conjunta queda:

$$f_{R,\Phi}(r,\phi)=
\begin{cases}
re^{-r^2/2} & r>0,\quad 0<\phi<1\\
0 & \text{en otro caso}
\end{cases}$$

## Paso 4. Cambio de variables

Ahora tenemos que pasar de las variables $(R,\Phi)$ a $(X,Y)$.

Recordemos que definimos:

$$X=R\sin(2\pi(ft+\Phi))$$

$$Y=R\cos(2\pi(ft+\Phi))$$

Para calcular la densidad conjunta $f_{X,Y}(x,y)$, podemos utilizar la fórmula de transformación de variables:

$$\boxed{
f_{X,Y}(x,y)=f_{R,\Phi}(r(x,y),\phi(x,y))
\left|\det J\right|
}$$

Donde $J$ es el jacobiano de la transformación inversa, es decir:

$$J=
\begin{pmatrix}
\frac{\partial r}{\partial x} & \frac{\partial r}{\partial y}\\[6pt]
\frac{\partial \phi}{\partial x} & \frac{\partial \phi}{\partial y}
\end{pmatrix}$$

### Vamos con una cuenta a la vez

Primero necesitamos expresar $r$ en función de $x$ e $y$.

Sabemos que:

$$X^2+Y^2=R^2$$

**Pregunta:** ¿Cómo despejarías $R$ a partir de esa igualdad?

Y algo importante: ¿por qué podemos elegir la raíz positiva y no la negativa?

Con eso avanzamos al jacobiano.

### Usuario

con raiz, elejimos la positiva porque la reganiva no tiene sentido porque tenemos que r>0

### Asistente

¡Correcto! Como $R>0$ por definición de la distribución de Rayleigh, nos quedamos con la raíz positiva:

$$\boxed{r=\sqrt{x^2+y^2}}$$

Ya tenemos la primera parte de la transformación inversa.

## Paso 5. Encontrar el jacobiano

Para calcularlo, necesitamos las derivadas de $r$ y de $\phi$ respecto de $x$ e $y$.

Pero vamos de a una.

Partimos de:

$$r(x,y)=\sqrt{x^2+y^2}=(x^2+y^2)^{1/2}$$

Aplicando la regla de la cadena:

$$\frac{\partial r}{\partial x}
=\frac12(x^2+y^2)^{-1/2}\cdot 2x$$

**Ahora te toca:** simplificá esa expresión y calculá también:

$$\frac{\partial r}{\partial y}$$

¿Cómo te quedan las dos derivadas?

Después seguimos con $\phi$, que es la parte un poco más interesante del cambio de coordenadas.

### Usuario

$$\frac{\partial r}{\partial x}
=\frac12(x^2+y^2)^{-1/2}\cdot 2y$$

### Asistente

¡Bien! Estás aplicando correctamente la regla de la cadena, pero hay un pequeño error en la notación.

La expresión que escribiste corresponde a la **derivada respecto de $y$**, no de $x$:

$$\frac{\partial r}{\partial y}
=\frac12(x^2+y^2)^{-1/2}\cdot 2y$$

Simplificando:

$$\boxed{\frac{\partial r}{\partial y}=\frac{y}{\sqrt{x^2+y^2}}}$$

Y, de manera análoga:

$$\boxed{\frac{\partial r}{\partial x}=\frac{x}{\sqrt{x^2+y^2}}}$$

## Siguiente paso: encontrar $\phi$

Recordá que tenemos:

$$x=r\sin(2\pi(ft+\phi))$$

$$y=r\cos(2\pi(ft+\phi))$$

**Te propongo lo siguiente:** dividí la primera ecuación por la segunda.

¿Qué expresión obtenés para $\frac{x}{y}$?

La idea es usar esa relación para despejar $\phi$ y después calcular sus derivadas.

### Usuario

porque queda -1/2? en la derivada

### Asistente

Porque estamos aplicando la **regla de la potencia** y después la **regla de la cadena**.

Partimos de:

$$r=\sqrt{x^2+y^2}$$

### 1. Convertimos la raíz en potencia

Recordá que:

$$\sqrt{a}=a^{1/2}$$

Entonces:

$$r=(x^2+y^2)^{1/2}$$

### 2. Aplicamos la regla de la potencia

La regla dice:

$$\frac{d}{dx}u^n=nu^{n-1}\frac{du}{dx}$$

En nuestro caso, $n=\frac12$.

Por lo tanto, al restarle 1 al exponente:

$$\frac12-1=-\frac12$$

**De ahí sale el exponente negativo.**

### 3. Aplicamos la regla de la cadena

Como estamos derivando respecto de $x$, tratamos $y$ como una constante:

$$\frac{\partial r}{\partial x}
=\frac12(x^2+y^2)^{-1/2}\cdot 2x$$

Y recordá que un exponente negativo significa que pasa al denominador:

$$a^{-1/2}=\frac{1}{\sqrt a}$$

Entonces:

$$\boxed{\frac{\partial r}{\partial x}=\frac{x}{\sqrt{x^2+y^2}}}$$

---

**Para comprobar que se entendió:** ¿qué exponente te quedaría si, en lugar de una raíz cuadrada, tuviéramos que derivar $(x^2+y^2)^{3/2}$?

Aplicá solamente la resta $n-1$.

### Usuario

Si se entendio. ahora si dividimos x/y nos queda como resultado thetha = tan -1 (x/y) / 2 pi - ft

### Asistente

¡Muy bien! El despeje es correcto, con un pequeño detalle que después vamos a tener en cuenta.

Partimos de:

$$\frac{x}{y}=\frac{r\sin(2\pi(ft+\phi))}{r\cos(2\pi(ft+\phi))}$$

Simplificando:

$$\frac{x}{y}=\tan(2\pi(ft+\phi))$$

Aplicando la inversa de la tangente:

$$\arctan\left(\frac{x}{y}\right)=2\pi(ft+\phi)$$

Y despejando, como hiciste:

$$\boxed{\phi=\frac{1}{2\pi}\arctan\left(\frac{x}{y}\right)-ft}$$

**Una observación:** la tangente tiene período $\pi$, por lo que este despeje tiene una ambigüedad de cuadrante. Para la transformación completa necesitaremos `atan2(x,y)` y considerar la fase módulo 1. Por ahora podemos avanzar con tu expresión para calcular las derivadas.

## Paso 6. Derivar $\phi$

Ya tenemos:

$$\phi(x,y)=\frac{1}{2\pi}\arctan\left(\frac{x}{y}\right)-ft$$

Necesitamos calcular:

$$\frac{\partial\phi}{\partial x}
\qquad \text{y} \qquad
\frac{\partial\phi}{\partial y}$$

Recordá la regla:

$$\frac{d}{dx}\arctan(u)=\frac{1}{1+u^2}\frac{du}{dx}$$

**Te toca:** empecemos por $\frac{\partial\phi}{\partial x}$.

Tené en cuenta que:

- $y$ es constante al derivar respecto de $x$.
- $ft$ también es constante.
- El factor $\frac{1}{2\pi}$ queda multiplicando.

¿Cómo te queda esa derivada antes de simplificar?

### Usuario

Una observación: la tangente tiene período \\(\\pi\\), por lo que este despeje tiene una ambigüedad de cuadrante. Para la transformación completa necesitaremos `atan2(x,y)` y considerar la fase módulo 1. Por ahora podemos avanzar con tu expresión para calcular las derivadas como seria esto?

### Asistente

La idea es que **$\arctan(x/y)$ no alcanza para determinar el ángulo correctamente en todos los cuadrantes**. Te muestro por qué.

## 1. ¿Cuál es el problema con la arcotangente?

Nosotros tenemos:

$$\frac{x}{y}=\tan(2\pi(ft+\phi))$$

Definamos temporalmente:

$$\theta=2\pi(ft+\phi)$$

Entonces:

$$\frac{x}{y}=\tan(\theta)$$

El problema es que la tangente es periódica con período $\pi$:

$$\tan(\theta)=\tan(\theta+\pi)$$

Por ejemplo:

$$\tan(45^\circ)=\tan(225^\circ)=1$$

Es decir, si conocemos solamente $x/y=1$, no podemos distinguir entre esos dos ángulos.

## 2. ¿Cómo lo soluciona atan2?

**[Esquema en el chat original: dos puntos opuestos del plano, $(1,1)$ y $(-1,-1)$, con el mismo cociente $x/y$, pero ángulos $45^\circ$ y $225^\circ$.]**

La función `atan2` recibe las dos coordenadas y utiliza sus signos para identificar el cuadrante.

Como en nuestro ejercicio definimos $x=r\sin\theta$ e $y=r\cos\theta$, usamos:

$$\theta=\operatorname{atan2}(x,y)$$

*Ojo:* habitualmente `atan2` recibe primero la coordenada vertical y después la horizontal. Acá el orden parece invertido porque definimos $x$ con seno e $y$ con coseno.

## 3. ¿Y qué significa módulo 1?

Recordemos:

$$\theta=2\pi(ft+\phi)$$

Como $\Phi$ está entre 0 y 1, representa una vuelta completa cuando la multiplicamos por $2\pi$.

Entonces podemos escribir:

$$\boxed{
\phi=\left(
\frac{\operatorname{atan2}(x,y)}{2\pi}-ft
\right)\bmod 1
}$$

El módulo 1 hace que el resultado quede en el intervalo $[0,1)$.

Por ejemplo:

$$1.25\bmod 1=0.25$$

Esto representa que una vuelta completa más un cuarto de vuelta equivale, angularmente, a un cuarto de vuelta.

---

## 4. ¿Necesitamos preocuparnos por esto en el ejercicio?

Para calcular el jacobiano, **podemos seguir usando tu expresión original de la arcotangente**, siempre que trabajemos localmente dentro de un cuadrante.

Las distintas ramas del ángulo solo agregan constantes a $\phi$, y sus derivadas son iguales fuera de los puntos de corte.

Así que volvamos a tu expresión:

$$\phi=\frac{1}{2\pi}\arctan\left(\frac{x}{y}\right)-ft$$

Y a la derivada que queremos calcular:

$$\frac{\partial\phi}{\partial x}$$

**Pregunta:** si aplicás la regla de la cadena a $\arctan(x/y)$, ¿cuánto vale la derivada interna $\frac{\partial}{\partial x}(x/y)$, considerando $y$ constante?

Esa es la siguiente cuenta que necesitamos.

### Usuario

las derivadas quedan dx = 1/2pi . [y/(x2+y2)] y dy = 1/2pi . [-x/(x2+y2)]

### Asistente

¡Excelente! **Las dos derivadas están correctas.**

Tenemos:

$$\boxed{\frac{\partial\phi}{\partial x}=\frac{1}{2\pi}\frac{y}{x^2+y^2}}$$

$$\boxed{\frac{\partial\phi}{\partial y}=-\frac{1}{2\pi}\frac{x}{x^2+y^2}}$$

## Paso 7. Construir el jacobiano

Ya tenemos las cuatro derivadas necesarias:

$$J=
\begin{pmatrix}
\frac{\partial r}{\partial x} & \frac{\partial r}{\partial y}\\[8pt]
\frac{\partial\phi}{\partial x} & \frac{\partial\phi}{\partial y}
\end{pmatrix}$$

Sustituyendo:

$$J=
\begin{pmatrix}
\frac{x}{\sqrt{x^2+y^2}} & \frac{y}{\sqrt{x^2+y^2}}\\[10pt]
\frac{y}{2\pi(x^2+y^2)} & -\frac{x}{2\pi(x^2+y^2)}
\end{pmatrix}$$

Ahora necesitamos calcular su determinante.

Recordá que para una matriz de $2\times2$:

$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$$

**Tu siguiente paso:** calculá $\det(J)$ y después su valor absoluto $|\det(J)|$.

Una pista: cuando hagas la resta y saques denominador común, vas a encontrar un $x^2+y^2$ en el numerador que se puede simplificar.

Pasame cuánto te da y seguimos con la densidad conjunta $f_{X,Y}(x,y)$.

### Usuario

1/(2pi . raiz(x2+y2))

### Asistente

¡Exactamente! **El valor absoluto del determinante es correcto.**

El determinante es negativo, pero como necesitamos su valor absoluto:

$$\boxed{|J|=\frac{1}{2\pi\sqrt{x^2+y^2}}}$$

## Paso 8. Calcular la densidad conjunta de $(X,Y)$

Ahora usamos la fórmula de cambio de variables:

$$f_{X,Y}(x,y)=f_{R,\Phi}(r(x,y),\phi(x,y))\cdot |J|$$

Recordemos que:

$$f_{R,\Phi}(r,\phi)=re^{-r^2/2}$$

Y sabemos que:

$$r=\sqrt{x^2+y^2}$$

Entonces, **primero sustituí $r$** en la densidad original:

$$f_{R,\Phi}(r(x,y),\phi(x,y))=\;?$$

Después multiplicá el resultado por:

$$|J|=\frac{1}{2\pi\sqrt{x^2+y^2}}$$

**Tu turno:** ¿cómo te queda $f_{X,Y}(x,y)$ después de hacer las sustituciones y simplificar?

Una pista: vas a poder cancelar una raíz del numerador con otra del denominador.

Ya estamos cerca de la parte más interesante: obtener la densidad marginal de $Y$ para demostrar que es normal.

### Usuario

$f_{R,\Phi}(r(x,y),\phi(x,y))= \sqrt{x^2+y^2} e^{-\sqrt{x^2+y^2}^2/2}$.

### Asistente

¡Perfecto! La sustitución está correcta. Solo vamos a simplificar el exponente.

Tenés:

$$f_{R,\Phi}(r(x,y),\phi(x,y))=\sqrt{x^2+y^2}\;e^{-\frac{(\sqrt{x^2+y^2})^2}{2}}$$

Recordá que:

$$(\sqrt{x^2+y^2})^2=x^2+y^2$$

Por lo tanto:

$$\boxed{f_{R,\Phi}(r(x,y),\phi(x,y))=\sqrt{x^2+y^2}\;e^{-\frac{x^2+y^2}{2}}}$$

## Ahora multiplicamos por el jacobiano

$$f_{X,Y}(x,y)=
\underbrace{\sqrt{x^2+y^2}\;e^{-\frac{x^2+y^2}{2}}}_{\text{Densidad transformada}}
\cdot
\underbrace{\frac{1}{2\pi\sqrt{x^2+y^2}}}_{|J|}$$

**Tu turno:** simplificá esta multiplicación.

¿Qué expresión final te queda para $f_{X,Y}(x,y)$?

Después vamos a obtener la densidad marginal $f_Y(y)$, que es lo último que necesitamos para demostrar que $Y_t$ tiene distribución normal.

### Usuario

fX,Y(x,y) = 1/2pi . e -(x2+y2)/2

### Asistente

¡Excelente! **Está completamente correcto.**

Llegamos a la densidad conjunta:

$$\boxed{f_{X,Y}(x,y)=\frac{1}{2\pi}e^{-\frac{x^2+y^2}{2}}}$$

## Paso 9. Obtener la densidad marginal de $Y$

Recordemos qué nos pide el ejercicio: demostrar que $Y_t$ tiene una distribución normal.

Hasta ahora encontramos la distribución **conjunta** de $X$ e $Y$, pero necesitamos la distribución de $Y$ solamente.

Para obtenerla, usamos la marginalización:

$$\boxed{f_Y(y)=\int_{-\infty}^{+\infty}f_{X,Y}(x,y)\,dx}$$

Reemplazando nuestra densidad:

$$f_Y(y)=\int_{-\infty}^{+\infty}\frac{1}{2\pi}e^{-\frac{x^2+y^2}{2}}\,dx$$

### Tu siguiente paso

Recordá esta propiedad de los exponentes:

$$e^{a+b}=e^a\cdot e^b$$

**Pregunta:** ¿podés separar $e^{-(x^2+y^2)/2}$ en dos exponenciales y sacar fuera de la integral todo lo que no depende de $x$?

Intentá escribir cómo te queda la integral después de hacerlo.

Con eso vamos a poder identificar la distribución normal sin necesidad de resolver una integral complicada.

### Usuario

fY(y) = 1/2pi . e(-y2/2) . integral(-inf,inf)[e(-x2/2)dx]

### Asistente

¡Perfecto! **La separación que hiciste es exactamente correcta.**

Tenemos:

$$f_Y(y)=\frac{1}{2\pi}e^{-y^2/2}
\underbrace{\int_{-\infty}^{+\infty}e^{-x^2/2}\,dx}_{\text{Nos falta calcular esto}}$$

## Paso 10. Identificar la integral gaussiana

Acá hay un truco importante: no necesitamos resolver esa integral desde cero.

Recordá la función de densidad de una distribución normal estándar $N(0,1)$:

$$f_X(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$$

Sabemos que **toda función de densidad de probabilidad integra 1 sobre su dominio**.

Por lo tanto:

$$\int_{-\infty}^{+\infty}
\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\,dx=1$$

### Ahora te toca

Si multiplicás ambos lados por $\sqrt{2\pi}$:

$$\int_{-\infty}^{+\infty}e^{-x^2/2}\,dx=\;?$$

¿Cuánto vale esa integral?

Después sustituimos ese valor en tu expresión de $f_Y(y)$ y comparamos con la densidad normal.

### Usuario

que 2pi?

### Asistente

Casi, pero te faltó la raíz cuadrada.

Partimos de:

$$\int_{-\infty}^{+\infty}
\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\,dx=1$$

Multiplicando ambos lados por $\sqrt{2\pi}$:

$$\boxed{\int_{-\infty}^{+\infty}e^{-x^2/2}\,dx=\sqrt{2\pi}}$$

Ahora volvamos a tu expresión:

$$f_Y(y)=\frac{1}{2\pi}e^{-y^2/2}
\int_{-\infty}^{+\infty}e^{-x^2/2}\,dx$$

**Última pregunta:** si reemplazás la integral por $\sqrt{2\pi}$, ¿cómo te queda $f_Y(y)$ después de simplificar?

Fijate especialmente en cómo se simplifica:

$$\frac{\sqrt{2\pi}}{2\pi}$$

Con eso ya podés identificar qué distribución tiene $Y_t$.

### Usuario

1/raiz(2pi) e-(y2/2) que es normal

### Asistente

¡Exactamente! 🎯 **Llegaste a la demostración correcta.**

Obtuvimos:

$$\boxed{f_Y(y)=\frac{1}{\sqrt{2\pi}}e^{-y^2/2}}$$

Comparémosla con la densidad de una distribución normal:

$$f(y)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(y-\mu)^2}{2\sigma^2}}$$

De acá podemos identificar:

- **Media:** $\mu=0$
- **Varianza:** $\sigma^2=1$

Por lo tanto:

$$\boxed{Y_t\sim\mathcal N(0,1)}$$

Y como el razonamiento vale para cualquier $t$ fijo, queda demostrado lo que pide el ejercicio.

### Algo importante para entender el resultado

Aunque $Y_t$ se construye usando un coseno, una amplitud Rayleigh y una fase uniforme, su distribución en cada instante es normal.

Esto **no significa que los valores $Y_t$ sean independientes entre distintos instantes**. Solo demostramos su distribución marginal.

¿Querés que sigamos con el ejercicio 2 del TP de la misma manera, paso a paso y sin darte la solución?

---

## Ejercicio 2 — Varianza de un promedio con ruido blanco

### Usuario

**[Imagen adjunta: enunciado del ejercicio 2]**

> **2. (3 puntos) Sea:**
>
> $$Y_t=\mu+\varepsilon_t+\varepsilon_{t-1}$$
>
> donde $\varepsilon_t$ es un ruido blanco de media 0.
>
> Sea
>
> $$\bar Y=\frac{1}{n}\sum_{i=1}^{n}Y_i$$
>
> Encuentre $\operatorname{Var}(\bar Y)$.

vamos con el punto dos

### Asistente

¡Vamos con el punto 2! Seguimos igual que antes: **vos hacés las cuentas y yo te voy guiando**, sin adelantarte la solución.

## Paso 1. Entender qué nos piden

Tenemos el proceso:

$$Y_t=\mu+\varepsilon_t+\varepsilon_{t-1}$$

Donde $\varepsilon_t$ es ruido blanco de media cero.

Recordá que, para un ruido blanco:

$$\begin{aligned}
E[\varepsilon_t]&=0\\
\operatorname{Var}(\varepsilon_t)&=\sigma^2\\
\operatorname{Cov}(\varepsilon_t,\varepsilon_s)&=0,\quad t\neq s
\end{aligned}$$

También nos dan el promedio muestral:

$$\bar Y=\frac1n\sum_{t=1}^n Y_t$$

Y nos piden calcular:

$$\boxed{\operatorname{Var}(\bar Y)}$$

## Paso 2. Expandir el promedio

Lo primero que vamos a hacer es reemplazar $Y_t$ por su definición:

$$\bar Y=\frac1n\sum_{t=1}^n(\mu+\varepsilon_t+\varepsilon_{t-1})$$

Podemos separar la sumatoria:

$$\bar Y=
\frac1n\left[
\sum_{t=1}^n\mu+
\sum_{t=1}^n\varepsilon_t+
\sum_{t=1}^n\varepsilon_{t-1}
\right]$$

### Primera pregunta

Como $\mu$ es constante, ¿cuánto vale esta sumatoria?

$$\sum_{t=1}^n\mu=\;?$$

Y una vez que la reemplaces, ¿cómo te queda la expresión de $\bar Y$?

Después vamos a trabajar con la varianza y ver por qué los términos $\varepsilon_t$ y $\varepsilon_{t-1}$ requieren especial atención.

### Usuario

es n

### Asistente

¡Casi! Como $\mu$ es una constante que se suma $n$ veces, el resultado es **$n\mu$**, no solamente $n$.

$$\sum_{t=1}^{n}\mu=n\mu$$

Entonces:

$$\bar Y=\frac{1}{n}\left(n\mu+\sum_{t=1}^{n}\varepsilon_t+\sum_{t=1}^{n}\varepsilon_{t-1}\right)$$

Simplificando:

$$\boxed{\bar Y=\mu+\frac{1}{n}\left(\sum_{t=1}^{n}\varepsilon_t+\sum_{t=1}^{n}\varepsilon_{t-1}\right)}$$

## Paso 3. Calcular la varianza

Ahora queremos:

$$\operatorname{Var}(\bar Y)$$

Recordá estas dos propiedades:

$$\operatorname{Var}(X+c)=\operatorname{Var}(X)$$

$$\operatorname{Var}(aX)=a^2\operatorname{Var}(X)$$

**Te toca:** aplicando esas propiedades, ¿cómo escribirías la varianza de $\bar Y$?

Por ahora no desarrolles las sumatorias. Solo queremos sacar la constante $\mu$ y el factor $1/n$.

### Usuario

1/n2 . var(sum et, sum et+1)

### Asistente

¡Muy bien! Aplicaste correctamente las propiedades de la varianza. Solo un detalle: el segundo término es $\varepsilon_{t-1}$, no $\varepsilon_{t+1}$.

Entonces tenemos:

$$\boxed{
\operatorname{Var}(\bar Y)=\frac{1}{n^2}
\operatorname{Var}\left(
\sum_{t=1}^{n}\varepsilon_t+
\sum_{t=1}^{n}\varepsilon_{t-1}
\right)
}$$

## Paso 4. Desarrollar la varianza de una suma

Recordá esta propiedad:

$$\operatorname{Var}(A+B)=
\operatorname{Var}(A)+
\operatorname{Var}(B)+
2\operatorname{Cov}(A,B)$$

En nuestro caso:

$$A=\sum_{t=1}^{n}\varepsilon_t
\qquad
B=\sum_{t=1}^{n}\varepsilon_{t-1}$$

**Acá hay algo importante:** aunque $\varepsilon_t$ es ruido blanco y sus valores en distintos instantes no están correlacionados, las dos sumatorias comparten varios términos.

Por ejemplo, si $n=3$:

$$A=\varepsilon_1+\varepsilon_2+\varepsilon_3$$

$$B=\varepsilon_0+\varepsilon_1+\varepsilon_2$$

Fijate que $\varepsilon_1$ y $\varepsilon_2$ aparecen en ambas sumatorias.

Por eso, no podemos asumir que $\operatorname{Cov}(A,B)=0$.

### Tu siguiente paso

Empecemos por calcular solamente:

$$\operatorname{Var}\left(\sum_{t=1}^{n}\varepsilon_t\right)$$

Sabemos que cada $\varepsilon_t$ tiene varianza $\sigma^2$ y que están incorrelacionados entre distintos instantes.

**¿Cuánto te da la varianza de esa sumatoria de $n$ términos?**

### Usuario

$n\sigma^2$

### Asistente

¡Exactamente! ✅

Como los términos del ruido blanco están incorrelacionados entre sí:

$$\boxed{\operatorname{Var}\left(\sum_{t=1}^{n}\varepsilon_t\right)=n\sigma^2}$$

Y para la segunda sumatoria ocurre lo mismo:

$$\operatorname{Var}\left(\sum_{t=1}^{n}\varepsilon_{t-1}\right)=n\sigma^2$$

## Paso 5. Calcular la covarianza

Ahora viene la parte más interesante del ejercicio.

Tenemos:

$$A=\varepsilon_1+\varepsilon_2+\cdots+\varepsilon_n$$

$$B=\varepsilon_0+\varepsilon_1+\cdots+\varepsilon_{n-1}$$

Queremos calcular:

$$\operatorname{Cov}(A,B)$$

Recordá que:

$$\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=
\begin{cases}
\sigma^2 & i=j\\
0 & i\neq j
\end{cases}$$

Esto significa que solamente contribuyen a la covarianza los términos que aparecen en **ambas sumatorias**.

Por ejemplo, para $n=4$:

$$\begin{aligned}
A&=\varepsilon_1+\varepsilon_2+\varepsilon_3+\varepsilon_4\\
B&=\varepsilon_0+\varepsilon_1+\varepsilon_2+\varepsilon_3
\end{aligned}$$

**Tu turno:** ¿cuántos términos comparten las dos sumatorias cuando tenemos un $n$ cualquiera?

Y, a partir de eso, ¿cuánto pensás que vale $\operatorname{Cov}(A,B)$?

No te preocupes todavía por reemplazarlo en la fórmula de la varianza.

### Usuario

comparten todos menos el primero de B y el ultimo de A, entonces comparten n-1 terminos. por lo que vale cov(a,b) = (n-1) sigma^2

### Asistente

¡Exactamente! ✅ Tu razonamiento es correcto.

Las sumatorias comparten $n-1$ términos y, como los distintos valores del ruido blanco están incorrelacionados:

$$\boxed{\operatorname{Cov}(A,B)=(n-1)\sigma^2}$$

## Paso 6. Calcular la varianza final

Recordemos dónde habíamos quedado:

$$\operatorname{Var}(\bar Y)=\frac{1}{n^2}\left[
\operatorname{Var}(A)+\operatorname{Var}(B)+2\operatorname{Cov}(A,B)
\right]$$

Ya calculaste las tres componentes:

$$\begin{aligned}
\operatorname{Var}(A)&=n\sigma^2\\
\operatorname{Var}(B)&=n\sigma^2\\
\operatorname{Cov}(A,B)&=(n-1)\sigma^2
\end{aligned}$$

Por lo tanto:

$$\operatorname{Var}(\bar Y)=\frac{1}{n^2}
\left[n\sigma^2+n\sigma^2+2(n-1)\sigma^2\right]$$

**Último paso, te toca:** sacá $\sigma^2$ como factor común y simplificá la expresión.

¿A qué fórmula llegás para $\operatorname{Var}(\bar Y)$ en función de $n$ y $\sigma^2$?

### Usuario

4n-1/n2 . sigma2

### Asistente

¡Casi perfecto! Hay un pequeño error al distribuir el 2.

Partimos de:

$$\operatorname{Var}(\bar Y)=\frac{\sigma^2}{n^2}\left[n+n+2(n-1)\right]$$

Aplicamos la distributiva:

$$2(n-1)=2n-2$$

Por lo tanto:

$$\operatorname{Var}(\bar Y)=\frac{\sigma^2}{n^2}\left[n+n+2n-2\right]$$

**Ahora sí, ¿cuánto te queda dentro del paréntesis?**

Con esa simplificación terminamos el ejercicio 2.

### Usuario

4n-2/n2 . sigma2

### Asistente

¡Exactamente! ✅ **Terminaste correctamente el ejercicio 2.**

El resultado final es:

$$\boxed{
\operatorname{Var}(\bar Y)=\frac{4n-2}{n^2}\sigma^2
}$$

También podemos expresarlo como:

$$\operatorname{Var}(\bar Y)=\left(\frac4n-\frac{2}{n^2}\right)\sigma^2$$

### Una observación interesante

Si $n$ crece mucho:

$$\operatorname{Var}(\bar Y)\approx\frac{4\sigma^2}{n}$$

Es decir, **la varianza del promedio tiende a cero a medida que aumenta el número de observaciones**, aunque exista dependencia temporal entre ellas.

Esto es importante en series de tiempo: no podemos calcular la varianza del promedio ignorando las autocovarianzas.

Ya resolviste los ejercicios 1 y 2. ¿Seguimos con el 3, calculando la función de autocorrelación paso a paso?

---

## Ejercicio 3 — Función de autocorrelación

### Usuario

**[Imagen adjunta: enunciado del ejercicio 3]**

> **3. (3 puntos) Sea:**
>
> $$Y_t=-10+(0)\varepsilon_t+(-7)\varepsilon_{t-1}+(-8)\varepsilon_{t-2}$$
>
> Encuentre la función de autocorrelación de $Y_t$.

dale

### Asistente

¡Vamos con el ejercicio 3! Seguimos como antes: **vos hacés las cuentas y yo te voy guiando**, sin darte la solución de entrada.

## Paso 1. Identificar el proceso

Tenemos:

$$Y_t=-10+0\varepsilon_t-7\varepsilon_{t-1}-8\varepsilon_{t-2}$$

Como el coeficiente de $\varepsilon_t$ es cero, podemos simplificar:

$$\boxed{Y_t=-10-7\varepsilon_{t-1}-8\varepsilon_{t-2}}$$

Este proceso es una media móvil de orden 2, o **MA(2)**, aunque el término de ruido contemporáneo tenga coeficiente cero.

Nos piden encontrar su **función de autocorrelación (ACF)**:

$$\boxed{\rho(h)=\frac{\gamma(h)}{\gamma(0)}}$$

Donde:

- $\gamma(h)=\operatorname{Cov}(Y_t,Y_{t-h})$ es la autocovarianza para el rezago $h$.
- $\gamma(0)=\operatorname{Var}(Y_t)$ es la varianza del proceso.

Para resolverlo, vamos a calcular primero la varianza y después las autocovarianzas para distintos rezagos.

## Paso 2. Calcular la media

Antes de calcular las autocovarianzas, encontremos la media:

$$E[Y_t]=E[-10-7\varepsilon_{t-1}-8\varepsilon_{t-2}]$$

Recordá que el ruido blanco tiene media cero:

$$E[\varepsilon_t]=0$$

**Primera pregunta:** aplicando la linealidad de la esperanza, ¿cuánto te da $E[Y_t]$?

Después seguimos con $\gamma(0)$, la varianza, usando las mismas propiedades que aplicaste en el ejercicio 2.

### Usuario

-10

### Asistente

¡Correcto! ✅

Como el ruido blanco tiene media cero:

$$E[Y_t]=-10-7(0)-8(0)$$

Por lo tanto:

$$\boxed{E[Y_t]=-10}$$

## Paso 3. Calcular la autocovarianza $\gamma(0)$

Recordá que la autocovarianza en el rezago cero es simplemente la varianza:

$$\gamma(0)=\operatorname{Var}(Y_t)$$

Reemplazamos:

$$\gamma(0)=\operatorname{Var}(-10-7\varepsilon_{t-1}-8\varepsilon_{t-2})$$

Tenemos dos propiedades importantes:

$$\operatorname{Var}(aX)=a^2\operatorname{Var}(X)$$

$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$$

Como $\varepsilon_t$ es ruido blanco, las perturbaciones de distintos instantes tienen covarianza cero.

**Ahora te toca:** ¿cuánto vale

$$\operatorname{Var}(-10-7\varepsilon_{t-1}-8\varepsilon_{t-2})$$

en función de $\sigma^2$?

Pista: la constante $-10$ no afecta la varianza, y tenés que elevar al cuadrado los coeficientes $-7$ y $-8$.

### Usuario

113 sigma2?

### Asistente

¡Exactamente! ✅

Como $\varepsilon_{t-1}$ y $\varepsilon_{t-2}$ están incorrelacionados:

$$\gamma(0)=(-7)^2\sigma^2+(-8)^2\sigma^2$$

$$\boxed{\gamma(0)=113\sigma^2}$$

## Paso 4. Calcular la autocovarianza $\gamma(1)$

Ahora queremos conocer la relación entre $Y_t$ y $Y_{t-1}$:

$$\gamma(1)=\operatorname{Cov}(Y_t,Y_{t-1})$$

Sabemos que:

$$Y_t=-10-7\varepsilon_{t-1}-8\varepsilon_{t-2}$$

Para encontrar $Y_{t-1}$, tenemos que reemplazar $t$ por $t-1$ en toda la expresión.

**Te toca:** ¿cómo queda $Y_{t-1}$?

Después vamos a comparar ambos procesos para identificar qué términos de ruido blanco tienen en común, igual que hicimos en el ejercicio 2.

### Usuario

Yt-1 = -10 - 7 e t-2 - 8 e t-3

### Asistente

¡Perfecto! ✅ Está correctamente desplazado un período.

Tenemos:

$$Y_t=-10-7\varepsilon_{t-1}-8\varepsilon_{t-2}$$

$$Y_{t-1}=-10-7\varepsilon_{t-2}-8\varepsilon_{t-3}$$

## Paso 5. Identificar los términos comunes

Queremos calcular:

$$\gamma(1)=\operatorname{Cov}(Y_t,Y_{t-1})$$

Recordá que, al calcular la covarianza, las constantes no influyen y los términos del ruido blanco en distintos instantes tienen covarianza cero.

Observá qué términos aparecen en ambos procesos:

**[Representación visual original, transcrita:]**

- $Y_t$: $-7\varepsilon_{t-1}\ \color{green}{-8\varepsilon_{t-2}}$
- $Y_{t-1}$: $\color{green}{-7\varepsilon_{t-2}}\ -8\varepsilon_{t-3}$

El término compartido es $\varepsilon_{t-2}$, aunque aparece con distintos coeficientes.

Por lo tanto, para calcular $\gamma(1)$, solo necesitamos considerar:

$$\gamma(1)=\operatorname{Cov}(-8\varepsilon_{t-2},-7\varepsilon_{t-2})$$

Recordá la propiedad:

$$\operatorname{Cov}(aX,bY)=ab\operatorname{Cov}(X,Y)$$

**Tu turno:** ¿cuánto te da $\gamma(1)$ en función de $\sigma^2$?

Después calculamos $\gamma(2)$ y empezamos a construir la función de autocorrelación.

### Usuario

56 sigma 2?

### Asistente

¡Exactamente! ✅

Aplicamos la propiedad de la covarianza:

$$\gamma(1)=(-8)(-7)\operatorname{Var}(\varepsilon_{t-2})$$

Por lo tanto:

$$\boxed{\gamma(1)=56\sigma^2}$$

## Paso 6. Calcular $\gamma(2)$

Ahora queremos calcular la autocovarianza con un rezago de 2:

$$\gamma(2)=\operatorname{Cov}(Y_t,Y_{t-2})$$

Sabemos que:

$$Y_t=-10-7\varepsilon_{t-1}-8\varepsilon_{t-2}$$

**Tu turno:** escribí la expresión de $Y_{t-2}$, reemplazando $t$ por $t-2$.

Después compará ambas expresiones y respondé:

¿Comparten algún término $\varepsilon$ con el mismo índice?

Con eso vamos a poder calcular $\gamma(2)$ y terminar de construir la función de autocorrelación.

### Usuario

Yt-1 = -10 - 7 e t-3 - 8 e t-4, no comparten por lo que la covianza es 0, y de aca en adelante ninguna ocmparte

### Asistente

¡Exactamente! ✅ Tu razonamiento es correcto. Solo un detalle de notación: escribiste $Y_{t-1}$, pero corresponde a $Y_{t-2}$.

Tenemos:

$$Y_t=-10-7\varepsilon_{t-1}-8\varepsilon_{t-2}$$

$$Y_{t-2}=-10-7\varepsilon_{t-3}-8\varepsilon_{t-4}$$

Como no comparten ningún término de ruido blanco:

$$\boxed{\gamma(2)=0}$$

Y, como bien dedujiste, para cualquier rezago $h\geq 2$, tampoco comparten términos:

$$\boxed{\gamma(h)=0,\quad h\geq 2}$$

## Paso 7. Construir la función de autocorrelación

Ya calculaste todas las autocovarianzas necesarias:

$$\begin{aligned}
\gamma(0)&=113\sigma^2\\
\gamma(1)&=56\sigma^2\\
\gamma(h)&=0,\quad h\geq 2
\end{aligned}$$

Recordemos que la función de autocorrelación es:

$$\boxed{\rho(h)=\frac{\gamma(h)}{\gamma(0)}}$$

**Última pregunta:** usando esa fórmula, ¿cuánto valen $\rho(0)$, $\rho(1)$ y $\rho(2)$?

Con esos tres valores ya podés escribir la ACF completa del proceso.

### Usuario

p(0) = 1, p(1) = 113/56, p(2) = 0

### Asistente

¡Casi perfecto! ✅ Tenés bien $\rho(0)$ y $\rho(2)$, pero en $\rho(1)$ invertiste el numerador y el denominador.

Recordá:

$$\rho(h)=\frac{\gamma(h)}{\gamma(0)}$$

Entonces:

$$\rho(0)=\frac{113\sigma^2}{113\sigma^2}=1$$

$$\rho(1)=\frac{56\sigma^2}{113\sigma^2}=\boxed{\frac{56}{113}\approx0.496}$$

$$\rho(2)=0$$

Una propiedad importante: **la autocorrelación siempre está entre $-1$ y $1$**. Por eso, $113/56$ no podía ser correcto.

## Último paso

Ya podemos escribir la ACF completa:

$$\boxed{
\rho(h)=
\begin{cases}
1 & h=0\\[4pt]
\frac{56}{113} & |h|=1\\[4pt]
0 & |h|\geq2
\end{cases}
}$$

Incluimos los rezagos negativos porque la autocorrelación es simétrica: $\rho(-h)=\rho(h)$.

**Con esto terminaste los tres ejercicios del TP.** Además, en este último identificaste correctamente lo más importante: qué términos de ruido blanco comparten los procesos desplazados y cómo eso determina la autocorrelación.

---

## Solicitud de exportación

### Usuario

generar un md con todo el chat para descargar

---

*Fin de la transcripción hasta la solicitud de exportación.*
