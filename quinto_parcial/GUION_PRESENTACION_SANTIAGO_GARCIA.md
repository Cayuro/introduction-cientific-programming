# Guion de Sustentación Individual · Quinto Parcial
**Expositor único:** Santiago García  
**Asignatura:** Introducción a la Programación Científica — Periodo 2026-2  
**Duración objetivo:** 6 a 8 minutos (dentro del rango exigido de 6 a 10 minutos)  
**Herramienta en pantalla:** [`quinto_parcial/index.html`](index.html) abierta en el navegador a pantalla completa.

---

## Consejos Rápidos para Grabar
1. Abre [`quinto_parcial/index.html`](index.html) y presiona **F11** para pantalla completa.
2. Asegúrate de que el micrófono esté bien conectado y habla tranquilo, como si le estuvieras explicando a un compañero.
3. Cambia de diapositiva con las flechas `←` y `→` del teclado.
4. Las diapositivas ahora tienen nombres en español claro (sin fórmulas raras) para que puedas leerlas y explicarlas con total naturalidad.

---

## Guion Minuto a Minuto

### ⏱️ Minuto 0:00 – 1:00 | Diapositiva 1: Portada y Pregunta Orientadora
* **En pantalla:** Diapositiva 1 (`Inicio`)
* **Qué decir:**
  > *"Buenos días / tardes, profesor. Mi nombre es **Santiago García**, estudiante del curso de Introducción a la Programación Científica, periodo 2026-2.  
  > A continuación presento la sustentación individual del Quinto Parcial, basada en el análisis y modelado de datos de vigilancia epidemiológica de VIH/SIDA en Medellín entre 2012 y 2023, a partir del registro oficial del SIVIGILA con 15.470 registros y 116 columnas.  
  > La pregunta orientadora de este trabajo en una sola oración es: **¿Cómo impactó la pandemia de COVID-19 la detección oportuna de VIH en Medellín y qué factores clínicos y sociodemográficos permiten anticipar la hospitalización urgente al momento de la notificación?**"*
* *(Presionas flecha `→` para pasar a Slide 2)*

---

### ⏱️ Minuto 1:00 – 2:30 | Diapositivas 2, 3 y 4: Reparación de Datos (Sección 2.1)

#### Diapositiva 2: Lectura Controlada y Conversión de Tipos
* **En pantalla:** Diapositiva 2 (`2.1 Lectura y Parseo`)
* **Qué decir:**
  > *"Iniciamos con la etapa de reparación. En la lectura de entrada controlamos la codificación UTF-8 y el separador por comas. Para no distorsionar los cálculos, detectamos desde el inicio los textos centinela que venían en el archivo, como el número ficticio `99999.07`, guiones y la etiqueta 'Sin Información', tratándolos directamente como valores vacíos o faltantes.  
  > Al convertir los textos a fechas reales con formato día primero, encontramos 6.124 fechas de síntomas vacías, que corresponden a pacientes que eran asintomáticos o que no recordaban con precisión cuándo empezaron sus primeros malestares."*
* *(Presionas flecha `→` para pasar a Slide 3)*

#### Diapositiva 3: Auditoría de Calidad y Depuración
* **En pantalla:** Diapositiva 3 (`2.1 Auditoría y Depuración`)
* **Qué decir:**
  > *"En la auditoría de calidad rastreamos duplicados y encontramos 3 pacientes que estaban repetidos exactamente por un doble reporte electrónico; los eliminamos, quedando una base limpia de 15.467 pacientes únicos.  
  > También auditamos registros imposibles: detectamos casos donde la fecha de síntomas aparecía como si hubiera ocurrido después de la consulta médica, los cuales se apartaron para no distorsionar el cálculo de días de retraso. Y confirmamos que todas las edades estuvieran en un rango biológico real de 0 a 94 años."*
* *(Presionas flecha `→` para pasar a Slide 4)*

#### Diapositiva 4: Decisiones por Variable y Método de Imputación
* **En pantalla:** Diapositiva 4 (`2.1 Imputación y Decisiones`)
* **Qué decir:**
  > *"Variable por variable, decidimos dejar el hueco en la fecha de inicio de síntomas porque inventar una fecha sería falsear la historia clínica del paciente. En la comuna y el estrato socioeconómico, donde faltaba cerca de un 22% de reportes, no eliminamos a los pacientes para evitar un grave **sesgo de selección**, ya que la falta de estrato suele indicar personas en situación de calle o inquilinatos informales.  
  > **Un punto metodológico fundamental:** rechazamos tajantemente rellenar los vacíos con el promedio simple (la media). Si tú rellenas miles de datos con un único número promedio, **aplastas la variabilidad natural y destruyes la desviación estándar**, haciendo que el modelo subestime el riesgo. Por eso usamos muestreo empírico aleatorio y medianas calculadas en bloques aislados."*
* *(Presionas flecha `→` para pasar a Slide 5)*

---

### ⏱️ Minuto 2:30 – 5:00 | Diapositivas 5, 6 y 7: Gráficos del Estudio (Sección 2.2)

#### Diapositiva 5: Figura 1 · Notificación Anual y Choque de la Pandemia
* **En pantalla:** Diapositiva 5 (`2.2 Figura 1 · Pandemia`)
* **Qué decir:**
  > *"Pasamos a los gráficos del estudio con la Figura 1.  
  > La pregunta es: **¿Cómo evolucionó la notificación anual de casos de VIH/SIDA en Medellín entre 2012 y 2023 y cuál fue el impacto de la pandemia de COVID-19 en 2020?**  
  > **La cifra:** vemos un crecimiento constante de 2012 a 2019 de casi un 180%, pero en el año 2020 de la pandemia se presentó una **caída abrupta del 17.5%**, bajando a 1.494 casos notificados (318 casos menos en un solo año).  
  > **Qué NO alcanza a concluirse:** no se puede concluir que los contagios reales de VIH hayan bajado en 2020. Esa caída refleja un **severo subregistro y retraso diagnóstico** provocado por las cuarentenas obligatorias y la saturación de los hospitales atendiendo la emergencia respiratoria."*
* *(Presionas flecha `→` para pasar a Slide 6)*

#### Diapositiva 6: Figura 2 · Días de Retraso según Régimen de Salud
* **En pantalla:** Diapositiva 6 (`2.2 Figura 2 · Retraso`)
* **Qué decir:**
  > *"En la Figura 2 respondemos: **¿Cuántos días de retraso pasan entre el inicio de síntomas y la consulta médica, y cómo cambia según el régimen de salud?**  
  > **La cifra:** la mediana siempre se mantiene entre 13 y 19 días; es decir, la mitad de los pacientes consulta en unas dos semanas. Sin embargo, el promedio matemático se disparó hasta 143.8 días en 2019 (casi 5 meses), porque los pacientes **No Asegurados y del Régimen Subsidiado** acumulan retrasos extremos de más de 100 días antes de poder ir al médico.  
  > **Qué NO alcanza a concluirse:** no se puede concluir que el tipo de carné de salud sea la causa directa del retraso. La brecha está mediada por vivir en barrios periféricos, falta de dinero para el transporte, trabajo informal y el estigma social."*
* *(Presionas flecha `→` para pasar a Slide 7)*

#### Diapositiva 7: Figura 3 · Hospitalización por Aseguramiento y Estrato
* **En pantalla:** Diapositiva 7 (`2.2 Figura 3 · Hospitalización`)
* **Qué decir:**
  > *"En la Figura 3 evaluamos: **¿Qué factores sociodemográficos se asocian con una mayor tasa de hospitalización urgente?**  
  > **La cifra:** mientras los pacientes con empleo formal y régimen contributivo se hospitalizan en un 18.9%, en los **No Asegurados la hospitalización sube al 29.1%** (más de 10 puntos de diferencia). En el estrato 1 supera el 24.2%.  
  > **Qué NO alcanza a concluirse:** esto no prueba que las clínicas discriminen a los no asegurados, sino que las personas sin seguro médico consultan cuando ya están en fases muy avanzadas con infecciones oportunistas graves."*
* *(Presionas flecha `→` para pasar a Slide 8)*

---

### ⏱️ Minuto 5:00 – 7:30 | Diapositivas 8, 9 y 10: Modelo de Predicción (Sección 2.3)

#### Diapositiva 8: Objetivo a Predecir, Variables y Fuga de Información
* **En pantalla:** Diapositiva 8 (`2.3 Formulación del Modelo`)
* **Qué decir:**
  > *"Entramos a la sección del modelo predictivo.  
  > **La variable a predecir en una sola oración:** anticipar si un paciente con VIH necesitará hospitalización clínica urgente frente a manejo ambulatorio al momento de ser notificado en el SIVIGILA. El dataset tiene un 80% de pacientes ambulatorios y un 20% hospitalizados.  
  > **En las variables de entrada usamos 15 predictores legítimos:** edad, sexo, estrato socioeconómico, comuna de residencia, régimen de salud y comorbilidades detectadas al ingreso como tuberculosis, sarcoma de Kaposi o neumonía.  
  > **Control de trampa o fuga de información:** dejamos estrictamente por fuera la variable de hospitalización de origen, si el paciente vivió o falleció, la fecha de defunción y los días que pasó en el hospital, porque son datos del futuro que no existen cuando el paciente recién llega al triaje."*
* *(Presionas flecha `→` para pasar a Slide 9)*

#### Diapositiva 9: División de Datos, Modelo Nulo y Métricas
* **En pantalla:** Diapositiva 9 (`2.3 Baseline y Métricas`)
* **Qué decir:**
  > *"Separamos los datos en 80% para entrenar (12.376 pacientes) y 20% para evaluar con pacientes no vistos (3.094 casos).  
  > **El Modelo Nulo o Baseline:** es la trampa básica; predice siempre que nadie se va a hospitalizar. Obtiene un acierto engañoso del **79.93%**, pero su capacidad de detectar enfermos reales es **0.00%** y su capacidad de discriminación es de **0.5000**, equivalente al puro azar.  
  > **Al evaluar nuestro modelo de Gradient Boosting:** logramos una exactitud del **84.16%**, una precisión en alertas del **69.10%** y una capacidad de discriminación de **0.8260**, triplicando la precisión en casos positivos frente al modelo nulo."*
* *(Presionas flecha `→` para pasar a Slide 10)*

#### Diapositiva 10: Veredicto Frente al Nulo y Límites Críticos
* **En pantalla:** Diapositiva 10 (`2.3 Diagnóstico y Límites`)
* **Qué decir:**
  > *"¿El modelo le gana al nulo? **Sí, contundentemente.** No solo supera la exactitud base, sino que discrimina con un área bajo la curva de 0.826 frente a 0.500. La gráfica de importancia nos muestra que tener tuberculosis pulmonar, infecciones respiratorias oportunistas y no tener seguro médico son las señales determinantes que encienden la alarma.  
  > **Límites críticos de lo que NO se puede concluir:**  
  > 1. El modelo es una herramienta de apoyo al triaje para organizar camas; no sustituye la valoración clínica del médico.  
  > 2. Correlación no es causa: no tener seguro alerta de consulta tardía, no es la causa biológica de la enfermedad.  
  > 3. Es un modelo específico para Medellín; requiere ajustes si se lleva a zonas rurales."*
* *(Presionas flecha `→` para pasar a Slide 11)*

---

### ⏱️ Minuto 7:30 – 8:15 | Diapositiva 11: Conclusiones y Cierre
* **En pantalla:** Diapositiva 11 (`Conclusiones`)
* **Qué decir:**
  > *"Para concluir esta sustentación del Quinto Parcial:  
  > Primero, demostramos que una reparación rigurosa preserva la variabilidad biológica sin sesgar los datos borrando filas incompletas.  
  > Segundo, el análisis gráfico evidenció el impacto de la pandemia de COVID-19 en la vigilancia epidemiológica.  
  > Y tercero, construimos un modelo supervisado reproducible sin trampas ni fuga de información que supera claramente al modelo nulo y aporta valor real a la gestión de salud pública.  
  > Muchas gracias por su atención."*
