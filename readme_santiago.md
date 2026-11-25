# Registro de Entregas y Sustentaciones · Santiago García

**Estudiante:** Santiago García (`Garabatoz`)  
**Curso:** Introducción a la Programación Científica — Periodo 2026-2  
**Profesor:** Alejandro Salgar  
**Repositorio:** `introduction-cientific-programming`

---

## Índice General
1. [Parcial 4 · Taller de Grafos: Transbordos y Minutos](#parcial-4--taller-de-grafos-transbordos-y-minutos)
   - [Enlaces y Entregables](#enlaces-y-entregables-parcial-4)
   - [Planteamiento y Pregunta Orientadora](#planteamiento-y-pregunta-orientadora)
   - [Estructura del Grafo](#estructura-del-grafo)
   - [Comparación BFS vs. Dijkstra](#comparación-bfs-vs-dijkstra)
   - [Guion y Notas del Video (4 a 6 minutos)](#guion-y-notas-del-video-parcial-4)
2. [Parcial 5 · Reparación, Gráficos y Modelo Predictivo](#parcial-5--reparación-gráficos-y-modelo-predictivo)
   - [Enlaces y Entregables](#enlaces-y-entregables-parcial-5)
   - [Pregunta Orientadora](#pregunta-orientadora-parcial-5)
   - [2.1 Reparación de Datos](#21-reparación-de-datos)
   - [2.2 Análisis Gráfico](#22-análisis-gráfico)
   - [2.3 Modelo de Predicción Supervisado](#23-modelo-de-predicción-supervisado)
   - [Guion y Notas del Video (6 a 10 minutos)](#guion-y-notas-del-video-parcial-5)
   - [Preguntas Frecuentes y Conceptos Clave](#preguntas-frecuentes-y-conceptos-clave)

---

# Parcial 4 · Taller de Grafos: Transbordos y Minutos

### Enlaces y Entregables (Parcial 4)
- **Enlace del Video de Sustentación:** [Ver Video en Google Drive](https://drive.google.com/file/d/1QBdeKbHiS4opKbF9_Kyu7pOqPSLvcHbr/view?usp=drive_link)
- **Diapositivas y Laboratorio Interactivo:** [`transbordos_y_minutos-SantiagoGarcia.html`](transbordos_y_minutos-SantiagoGarcia.html) (o [`grafos/index.html`](grafos/index.html))
- **Código Python y Modelado:** Implementación formal con `collections.deque` y `heapq`.

---

### Planteamiento y Pregunta Orientadora

> **La Pregunta en una sola oración:**  
> **«¿Qué ruta realiza el menor número de transbordos y qué ruta tarda el menor tiempo en minutos desde Terminal Norte hasta Hospital Universitario, y por qué difieren?»**

Una red de transporte metropolitano intermodal donde las estaciones son los vértices y cada tramo es una arista con una duración real en minutos ($w > 0$). Se contrastan dos criterios de optimización:
1. **Minimizar transbordos (saltos):** Resuelto mediante búsqueda en anchura (**BFS**).
2. **Minimizar tiempo de viaje (minutos):** Resuelto mediante el algoritmo de caminos mínimos de **Dijkstra**.

---

### Estructura del Grafo

Grafo propio con **8 estaciones** y **13 conexiones bidireccionales**, combinando tres tecnologías con velocidades operativas muy disímiles:
- **Línea Troncal de Metro (Férreo - Alta velocidad):** $3$ a $4$ min por tramo.
- **Línea de Metrocable (Ladera montañosa - Baja velocidad):** $11$ a $18$ min por tramo.
- **Red de Tranvía y Enlaces Secundarios:** $5$ a $10$ min por tramo.

#### Vértices
- **A:** Terminal Norte (Origen)
- **B:** Cable Mirador
- **C:** Parque Universidad
- **D:** Estación Central
- **E:** Distrito Tecnológico
- **F:** Portal Occidente
- **G:** Bulevar Comercial
- **H:** Hospital Universitario (Destino)

#### Tiempos y Conexiones (Minutos)
```text
A (Terminal Norte)         -> B (18 min, Cable), C (3 min, Metro), F (6 min, Tranvía)
B (Cable Mirador)          -> A (18 min, Cable), D (11 min, Cable), H (17 min, Cable)
C (Parque Universidad)     -> A (3 min, Metro), D (4 min, Metro), F (5 min, Tranvía)
D (Estación Central)       -> B (11 min, Cable), C (4 min, Metro), E (3 min, Metro), G (5 min, Tranvía)
E (Distrito Tecnológico)   -> D (3 min, Metro), G (7 min, Tranvía), H (4 min, Metro)
F (Portal Occidente)       -> A (6 min, Tranvía), C (5 min, Tranvía), G (8 min, Tranvía)
G (Bulevar Comercial)      -> D (5 min, Tranvía), E (7 min, Tranvía), F (8 min, Tranvía), H (10 min, Tranvía)
H (Hospital Universitario) -> B (17 min, Cable), E (4 min, Metro), G (10 min, Tranvía)
```

---

### Comparación BFS vs. Dijkstra

| Criterio | BFS (Menos Transbordos) | Dijkstra (Menor Tiempo Real) |
| :--- | :--- | :--- |
| **Estructura Interna** | Cola FIFO (`collections.deque`) | Cola de Prioridad / Min-Heap (`heapq`) |
| **Peso considerado** | Ignora pesos: asume costo $1$ salto por tramo | Considera el peso exacto en minutos ($w$) |
| **Ruta Óptima elegida** | `A → B → H` | `A → C → D → E → H` |
| **Tramos (aristas)** | **2 tramos** (1 transbordo intermedio) | **4 tramos** (3 transbordos intermedios) |
| **Tiempo Total** | $18 + 17 =$ **35 minutos** | $3 + 4 + 3 + 4 =$ **14 minutos** |
| **Diferencia Técnica** | La ruta por cable tiene solo 2 saltos pero es muy lenta por ser cabina de montaña. | Pasa por 4 tramos pero al ser tren subterráneo/férreo veloz ahorra **21 minutos** (60% más rápido). |

---

### Guion y Notas del Video (Parcial 4)

* **0:00 – 1:00 (Introducción):** Saludo, nombre Santiago García, planteamiento del problema de transporte intermodal y lectura textual de la pregunta orientadora.
* **1:00 – 2:00 (El Grafo):** Explicación de los 8 nodos, las 3 tecnologías (Metro, Cable, Tranvía) y cómo se asignaron los minutos positivos.
* **2:00 – 4:00 (Demostración Interactiva):**
  - Activar **BFS**: mostrar cómo la cola FIFO explora por niveles, encolando A hacia B, C, F a 1 salto, y alcanzando H desde B en 2 saltos ($35$ min).
  - Activar **Dijkstra**: mostrar cómo el Min-Heap procesa siempre el nodo con menor tiempo acumulado, confirmando C (3 min), D (7 min), E (10 min) y llegando a H en solo $14$ min.
* **4:00 – 5:15 (Comparación):** Justificar por qué la ruta con menos transbordos dura 35 min y la de más transbordos solo 14 min. Explicar el concepto de ponderación de aristas.
* **5:15 – 6:00 (Cierre y Código):** Mencionar la implementación con deque y heapq en Python, y la conclusión aplicada a sistemas de transporte masivo.

---
---

# Parcial 5 · Reparación, Gráficos y Modelo Predictivo

### Enlaces y Entregables (Parcial 5)
- **Video Principal:** [Ver Video Principal en Google Drive](https://drive.google.com/file/d/1lsN7ffUmFqQ327Ta0wPGi3dacxGMdz7g/view?usp=drive_link)
- **Video Complementario / Respaldo:** [Ver Video Complementario en Google Drive](https://drive.google.com/file/d/154nIEk2JfRPbw8AL-YHy3kwsOvkbRq5e/view?usp=drive_link)
- **Diapositivas HTML Oficiales:** [`quinto_parcial/index.html`](quinto_parcial/index.html) *(abre con doble clic, flechas `←` y `→`, contador de diapositivas en pantalla)*.
- **Cuaderno Base de la Tarea 2:** [`notebooks/tarea2_colab_santiago.ipynb`](notebooks/tarea2_colab_santiago.ipynb) (y [`notebooks/modelo_prediccion_santiago.ipynb`](notebooks/modelo_prediccion_santiago.ipynb)).

---

### Pregunta Orientadora (Parcial 5)

> **«¿Cómo impactó la pandemia de COVID-19 la detección oportuna de VIH en Medellín y qué factores clínicos y sociodemográficos permiten anticipar la hospitalización urgente al momento de la notificación epidemiológica?»**

---

### 2.1 Reparación de Datos

| Etapa | Proceso Realizado | Hallazgo y Decisión Técnica |
| :--- | :--- | :--- |
| **Lectura Controlada** | Formato CSV, encoding `UTF-8`, separador `,`. Identificación temprana de valores centinela: `99999.07`, `-   -`, `Sin Información`. | Se declararon como `na_values` para que pandas los convirtiera a nulos sin contaminar medias ni cálculos numéricos. |
| **Parseo Semántico** | Conversión de cadenas de texto a fechas reales mediante `pd.to_datetime(format='%d/%m/%Y')` y números enteros. | Se detectaron **6.124 fechas de síntomas vacías**. Corresponden a pacientes asintomáticos o que no recordaban cuándo iniciaron síntomas. Se decidió **mantener el hueco** (no imputar) para no inventar historias clínicas. |
| **Auditoría de Calidad** | Búsqueda de registros duplicados e inconsistencias biológicas o cronológicas. | Se identificaron y eliminaron **3 registros duplicados exactos** (pasando de 15.470 a 15.467 pacientes únicos). Se detectaron fechas de síntomas posteriores a la consulta (incoherentes) y se aislaron. Las edades se validaron en el rango biológico real de 0 a 94 años. |
| **Depuración e Imputación** | Comunas y estratos con faltantes (~22%). | **No se eliminaron las filas** para evitar el **sesgo de selección** (eliminar pacientes sin estrato borraría a habitantes de calle o inquilinatos informales). |
| **Preservación de Varianza** | Rechazo total de la media simple. | **Decisión crítica:** La imputación por la media aplasta la varianza y reduce artificialmente la desviación estándar, falseando el riesgo. Se utilizó **muestreo empírico aleatorio** y medianas calculadas en particiones aisladas. |

---

### 2.2 Análisis Gráfico

#### Figura 1: Dinámica Temporal y Choque por COVID-19
- **Pregunta:** *¿Cómo varió el ritmo de notificaciones de VIH en Medellín entre 2012 y 2023 y qué impacto tuvo la pandemia de COVID-19?*
- **Cifra observada:** En el año 2020 se registró una caída drástica del **18.5%** en las notificaciones anuales respecto a la tendencia previa.
- **Límite de la conclusión:** La gráfica no prueba que la transmisión biológica del virus haya disminuido, sino que el colapso hospitalario y los confinamientos impidieron que los pacientes acudieran a diagnóstico oportuno.

#### Figura 2: Retraso Diagnóstico según Régimen de Aseguramiento
- **Pregunta:** *¿Varía el tiempo de retraso diagnóstico entre el inicio de síntomas y la consulta médica según el régimen de salud?*
- **Cifra observada:** La mediana anual de días de retraso en la población **No Asegurada es de 14.2 días**, mientras que en Regímenes Especiales (fuerzas militares, docentes) es de **8.7 días** (una brecha de más de 5.5 días).
- **Límite de la conclusión:** Mide únicamente los días transcurridos entre que el paciente notó malestar y llegó al médico; no alcanza a medir el momento biológico real del contagio inicial.

#### Figura 3: Tasa de Hospitalización por Aseguramiento y Estrato
- **Pregunta:** *¿Qué factores sociodemográficos se asocian con una mayor tasa de hospitalización urgente al momento del diagnóstico?*
- **Cifra observada:** Los pacientes del régimen **Contributivo se hospitalizan en un 18.9%**, mientras que en la población **No Asegurada la hospitalización asciende al 29.1%** (más de 10 puntos porcentuales de diferencia). En el estrato socioeconómico 1 la tasa supera el **24.2%**.
- **Límite de la conclusión:** No demuestra discriminación hospitalaria, sino que las personas sin cobertura formal acuden en fases muy tardías de inmunosupresión con complicaciones oportunistas avanzadas.

---

### 2.3 Modelo de Predicción Supervisado

#### 1. Definición Formal de la Variable Objetivo ($y$)
* **Variable objetivo en una oración:** *Anticipar si un paciente diagnosticado con VIH requerirá hospitalización clínica urgente frente a manejo ambulatorio al momento de su notificación epidemiológica.*
* **Balance de clases:** Clase mayoritaria (Manejo ambulatorio, $y=0$): **79.93%**. Clase minoritaria (Hospitalizado, $y=1$): **20.07%**.

#### 2. Matriz de Entrada ($X$) y Control de Fuga de Información (*Data Leakage*)
* **Predictores incluidos (15 variables legítimas al ingreso):** Edad, sexo biológico, estrato socioeconómico, comuna de residencia, régimen de afiliación en salud, y comorbilidades detectadas al triaje (tuberculosis pulmonar, sarcoma de Kaposi, hepatitis B, hepatitis C, toxoplasmosis, desnutrición severa).
* **Variables estrictamente excluidas para evitar trampa:**
  - `pac_hos_` original (es el objetivo con otro nombre).
  - Condición final del paciente (`con_fin_`: vivo o fallecido).
  - Fecha de defunción (`fec_def_`).
  - Días de estancia hospitalaria (`dias_hosp`).
  *Razón:* Son datos posteriores a la atención que no existen al momento de recibir al paciente en triaje.

#### 3. Partición de Datos (Entrenamiento y Prueba)
* **Entrenamiento (80%):** 12.376 pacientes históricos.
* **Prueba (20%):** 3.094 pacientes nuevos nunca vistos por el modelo, aislados con `random_state=42` y estratificación.

#### 4. Tabla Comparativa: Modelo Nulo vs. Modelo Entrenado

| Métrica de Evaluación | Modelo Nulo (*Dummy Baseline*) | Modelo Supervisado (*Gradient Boosting*) | Ganancia / Veredicto |
| :--- | :---: | :---: | :---: |
| **Estrategia** | Predice siempre la clase mayoritaria ($y=0$, ambulatorio) | Ensamble de árboles de decisión sobre predictores de ingreso | Aprendizaje no lineal con regularización |
| **Exactitud (*Accuracy*)** | 79.93% *(engañosa)* | **84.16%** | **Supera al baseline por +4.23 puntos** |
| **Sensibilidad / Detección (*Recall* $y=1$)** | 0.00% *(ciego ante enfermos graves)* | **46.70%** | **Detecta casi la mitad de los casos críticos** |
| **Precisión en Alertas (*Precision* $y=1$)** | 0.00% | **69.10%** | **7 de cada 10 alertas son ciertas** |
| **Área Bajo la Curva ROC (AUC)** | 0.5000 *(azar puro / moneda al aire)* | **0.8260** | **Excelente capacidad discriminativa (+0.326)** |

#### 5. Factores Determinantes y Límites del Modelo
* **Variables con mayor peso predictivo:**
  1. Tuberculosis pulmonar activa (`tub_pul`).
  2. Otras infecciones oportunistas respiratorias.
  3. Régimen No Asegurado (`tip_ss_ = 'D'`).
  4. Edad avanzada o extrema vulnerabilidad socioeconómica.
* **Límites de lo que NO se puede concluir:**
  1. **Es herramienta de apoyo al triaje:** Ayuda a reservar camas de hospitalización de forma anticipada; no reemplaza el criterio del médico especialista.
  2. **Correlación no implica causalidad:** No tener carné de seguro médico no es la causa biológica de la hospitalización; es un marcador de detección tardía y barreras de acceso.
  3. **Validez local:** El modelo está calibrado específicamente para la red hospitalaria de Medellín; llevarlo a zonas rurales requiere recalibración de variables.

---

### Guion y Notas del Video (Parcial 5)

> **Instrucción de grabación:** Abrir [`quinto_parcial/index.html`](quinto_parcial/index.html) en el navegador, activar pantalla completa (tecla **F11**), verificar que el enlace se lea en pantalla y recorrer las diapositivas con las flechas del teclado.

* **0:00 – 1:00 (Slide 1 · Inicio y Pregunta):** Presentación personal de Santiago García, ficha del SIVIGILA Medellín (15.470 filas y 116 columnas) y lectura de la pregunta orientadora.
* **1:00 – 1:45 (Slide 2 · Lectura y Parseo):** Detección de centinelas (`99999.07`, guiones), conversión a fechas y explicación de las 6.124 fechas de síntomas faltantes (asintomáticos).
* **1:45 – 2:15 (Slide 3 · Auditoría y Depuración):** Eliminación de 3 duplicados exactos (15.467 únicos), control de fechas imposibles y validación de rangos de edad biológicos.
* **2:15 – 3:00 (Slide 4 · Decisiones e Imputación):** Justificación de no borrar filas incompletas (evitar sesgo de selección en estratos vulnerables) y el argumento contra la media simple (destruye la desviación estándar y aplasta la varianza).
* **3:00 – 3:45 (Slide 5 · Figura 1 Dinámica Temporal):** Análisis del choque COVID-19 en 2020 (-18.5%) y aclaración de que refleja colapso de consulta y no menor propagación viral.
* **3:45 – 4:30 (Slide 6 · Figura 2 Retraso Diagnóstico):** Explicación del retraso de 14.2 días en No Asegurados frente a 8.7 días en Regímenes Especiales.
* **4:30 – 5:15 (Slide 7 · Figura 3 Hospitalización):** Contraste del 29.1% de hospitalización en no asegurados vs 18.9% en contributivo, aclarando que no es discriminación médica sino consulta tardía.
* **5:15 – 6:00 (Slide 8 · Formulación del Modelo):** Variable objetivo en una oración, 15 variables de entrada y aislamiento riguroso de fuga de información (exclusión de variables del futuro).
* **6:00 – 6:45 (Slide 9 · Baseline y Métricas):** Explicación de la trampa del modelo nulo (79.93% de acierto pero AUC 0.500 y recall 0%) frente a Gradient Boosting (84.16% de exactitud y AUC 0.826).
* **6:45 – 7:30 (Slide 10 · Veredicto y Límites):** Confirmación contundente de victoria sobre el nulo, importancia de tuberculosis y régimen subsidiado/no asegurado, y los 3 límites éticos y operacionales.
* **7:30 – 8:00 (Slide 11 · Conclusiones y Cierre):** Resumen de reparación responsable, análisis visual y modelo predictivo reproducible.

---

### Preguntas Frecuentes y Conceptos Clave

#### 1. ¿Por qué se rechazó imputar con la media?
Si en una columna con 3.000 vacíos se coloca a todos el valor promedio, la dispersión estadística de los datos se contrae artificialmente. La varianza y la desviación estándar disminuyen, haciendo creer a los algoritmos que la población es homogénea y ocultando a los pacientes con valores extremos y alto riesgo.

#### 2. ¿Qué significa el "Modelo Nulo" o *Dummy Baseline*?
En problemas desbalanceados (donde el 80% no se hospitaliza), un modelo tramposo que siempre responda *"ninguno se va a hospitalizar"* acertará el 80% de las veces sin saber nada de medicina. Ese es el modelo nulo. Para que un modelo sea útil, debe demostrar que detecta a los casos de la clase minoritaria y que su AUC supera holgadamente a 0.500.

#### 3. ¿Qué es la fuga de datos (*Data Leakage*)?
Ocurre cuando entrenamos un modelo con variables que solo se conocen después de que el evento ya ocurrió (por ejemplo, si usamos la variable de si el paciente falleció o los días que estuvo en cama para predecir si debía ser hospitalizado). Al retirarlas, garantizamos que el modelo funcione con lo que ve el médico al recibir al paciente.
