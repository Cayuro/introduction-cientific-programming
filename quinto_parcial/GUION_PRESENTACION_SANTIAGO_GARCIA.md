# Guion de Sustentación Individual · Quinto Parcial
**Expositor único:** Santiago García  
**Asignatura:** Introducción a la Programación Científica — Periodo 2026-2  
**Duración objetivo:** 6 a 8 minutos (dentro del rango exigido de 6 a 10 minutos)  
**Herramienta en pantalla:** [`quinto_parcial/index.html`](index.html) abierta en el navegador.

---

## Recomendaciones Previas a la Grabación
1. Abre [`quinto_parcial/index.html`](index.html) a pantalla completa (F11 en el navegador).
2. Asegúrate de que la barra de direcciones o la ruta local se vea al inicio.
3. Cambia de diapositiva con las flechas `←` y `→` del teclado.
4. Mantén un tono pausado, claro y seguro. Habla fluido sin correr.

---

## Minuto a Minuto de la Exposición

### ⏱️ Minuto 0:00 – 1:00 | Diapositiva 1: Portada y Pregunta Orientadora
* **En pantalla:** Slide 1 (`Inicio`)
* **Qué decir:**
  > *"Buenos días / tardes, profesor. Mi nombre es **Santiago García**, estudiante del curso de Introducción a la Programación Científica, periodo 2026-2.  
  > A continuación presento la sustentación del Quinto Parcial, basada en el análisis y modelado de datos de vigilancia epidemiológica de VIH/SIDA en Medellín para el periodo 2012 a 2023, a partir del registro oficial del SIVIGILA con 15.470 registros y 116 columnas.  
  > La pregunta orientadora de este trabajo en una sola oración es: **¿Cómo impactó la pandemia de COVID-19 la detección oportuna de VIH en Medellín y qué factores clínicos y sociodemográficos permiten anticipar la hospitalización urgente al momento de la notificación?**"*
* *(Presionas flecha `→` para pasar a Slide 2)*

---

### ⏱️ Minuto 1:00 – 2:30 | Diapositivas 2, 3 y 4: Reparación de Datos (2.1)

#### Diapositiva 2: Lectura y Parseo Semántico
* **En pantalla:** Slide 2 (`2.1 Lectura y Parseo`)
* **Qué decir:**
  > *"Iniciamos con la etapa de reparación. En la lectura de entrada controlamos explícitamente la codificación en UTF-8 y delimitador por comas. Para no distorsionar las estadísticas, tratamos desde la lectura los centinelas como faltantes mediante `na_values`, capturando valores como `99999.07`, guiones y la etiqueta 'Sin Información'.  
  > En el parseo semántico, convertimos las fechas con formato día primero. Al parsear la fecha de inicio de síntomas nacieron 6.124 valores `NaT`, correspondientes a pacientes asintomáticos o que no recordaban cuándo empezaron los síntomas."*
* *(Presionas flecha `→` para pasar a Slide 3)*

#### Diapositiva 3: Auditoría de Calidad y Depuración
* **En pantalla:** Slide 3 (`2.1 Auditoría y Depuración`)
* **Qué decir:**
  > *"En la auditoría de calidad encontramos 3 filas duplicadas exactas generadas por doble transmisión electrónica, las cuales eliminamos, quedando 15.467 casos únicos.  
  > Auditamos los imposibles cronológicos, detectando inconsistencias donde la fecha de inicio de síntomas aparecía posterior a la fecha de consulta médica, las cuales se depuraron para el cálculo del retraso diagnóstico. Confirmamos que las edades estuvieran en el rango biológico válido de 0 a 94 años."*
* *(Presionas flecha `→` para pasar a Slide 4)*

#### Diapositiva 4: Decisiones por Variable y Método de Imputación
* **En pantalla:** Slide 4 (`2.1 Imputación y Decisiones`)
* **Qué decir:**
  > *"Variable por variable, decidimos dejar el hueco en el inicio de síntomas porque inventar una fecha falsearía la historia natural del virus. En comuna y estrato, donde había cerca de 22% sin reportar, no eliminamos las filas para evitar un grave **sesgo de selección**, ya que la falta de estrato correlaciona con población en habitanza de calle o inquilinatos.  
  > **Un punto metodológico fundamental:** rechazamos tajantemente imputar con la media simple. Rellenar con el promedio concentra la probabilidad en un punto y **aplasta artificialmente la varianza y la desviación estándar**. Por eso utilizamos muestreo empírico aleatorio (*hot-deck*) y medianas en pipelines aislados para preservar la dispersión real."*
* *(Presionas flecha `→` para pasar a Slide 5)*

---

### ⏱️ Minuto 2:30 – 5:00 | Diapositivas 5, 6 y 7: Gráficos del Notebook (2.2)

#### Diapositiva 5: Figura 1 · Dinámica Temporal y Choque COVID-19
* **En pantalla:** Slide 5 (`2.2 Figura 1 · Pandemia`)
* **Qué decir:**
  > *"Pasamos a la sección de gráficos con la Figura 1.  
  > La pregunta del notebook es: **¿Cómo evolucionó la notificación anual de casos de VIH/SIDA en Medellín entre 2012 y 2023 y cuál fue el impacto del choque sanitario de COVID-19 en 2020?**  
  > **La cifra:** observamos un crecimiento sostenido de 2012 a 2019 de casi 180%, pero en el año 2020 se registra una **caída abrupta del 17.5%**, bajando a 1.494 casos.  
  > **Qué NO alcanza a concluirse:** no se puede concluir que los contagios reales hayan bajado en 2020. Esta caída refleja un severo **subregistro y retraso diagnóstico** derivado del cierre de servicios ambulatorios, cuarentenas y el colapso hospitalario."*
* *(Presionas flecha `→` para pasar a Slide 6)*

#### Diapositiva 6: Figura 2 · Retraso Diagnóstico por Régimen
* **En pantalla:** Slide 6 (`2.2 Figura 2 · Retraso`)
* **Qué decir:**
  > *"En la Figura 2 abordamos la pregunta: **¿Cuál es el tiempo de retraso entre el inicio de síntomas y la consulta médica ($\Delta t$) y cómo varía según el régimen de aseguramiento?**  
  > **La cifra:** la mediana de retraso oscila entre 13 y 19 días, pero la distribución es muy asimétrica hacia la derecha, con medias que llegaron a 143 días en 2019, concentrándose los retrasos extremos de más de 100 días en pacientes del Régimen Subsidiado y No Asegurados.  
  > **Qué NO alcanza a concluirse:** no se puede concluir causalidad directa exclusiva del carné de salud. La brecha está mediada por factores de confusión como informalidad laboral, barreras geográficas en las laderas y estigma social."*
* *(Presionas flecha `→` para pasar a Slide 7)*

#### Diapositiva 7: Figura 3 · Hospitalización por Régimen y Estrato
* **En pantalla:** Slide 7 (`2.2 Figura 3 · Hospitalización`)
* **Qué decir:**
  > *"En la Figura 3 evaluamos: **¿Qué factores sociodemográficos se asocian con una mayor tasa de hospitalización urgente?**  
  > **La cifra:** mientras los pacientes del Régimen Contributivo tienen una tasa de hospitalización del 18.9%, en los **No Asegurados se dispara al 29.1%**, una brecha de más de 10 puntos porcentuales. En estrato 1 supera el 24%.  
  > **Qué NO alcanza a concluirse:** esto no prueba que los hospitales discriminen al no asegurado, sino que esta población suele consultar en estadios clínicos muy avanzados con infecciones oportunistas ya descompensadas."*
* *(Presionas flecha `→` para pasar a Slide 8)*

---

### ⏱️ Minuto 5:00 – 7:30 | Diapositivas 8, 9 y 10: Modelo de Predicción (2.3)

#### Diapositiva 8: Formulación de $y$, Predictores $X$ y Fuga de Datos
* **En pantalla:** Slide 8 (`2.3 Formulación del Modelo`)
* **Qué decir:**
  > *"Entramos a la sección del modelo predictivo.  
  > **La variable objetivo $y$ en una sola oración:** predecir si un paciente diagnosticado con VIH/SIDA requerirá hospitalización clínica urgente ($y = 1$) frente a manejo ambulatorio ($y = 0$) al momento de su notificación epidemiológica en el SIVIGILA. Presenta un desbalance de 20% hospitalizados frente a 80% ambulatorios.  
  > **En $X$ entran 15 predictores legítimos:** edad, sexo, estrato, comuna, régimen y comorbilidades conocidas al ingreso como tuberculosis, sarcoma de Kaposi o neumonía.  
  > **Control de fuga de datos (*Data Leakage*):** dejamos estrictamente por fuera la variable origen `pac_hos_`, la condición final de vivo o muerto (`con_fin_`), la fecha de defunción y los días de estancia, porque son desenlaces futuros que no existen en el momento del triaje."*
* *(Presionas flecha `→` para pasar a Slide 9)*

#### Diapositiva 9: Partición, Baseline Nulo y Comparación de Métricas
* **En pantalla:** Slide 9 (`2.3 Baseline y Métricas`)
* **Qué decir:**
  > *"Aplicamos una partición estratificada 80/20 con 12.376 pacientes en entrenamiento y 3.094 en prueba no vista.  
  > **El Baseline Nulo obligatorio:** predice siempre la clase mayoritaria (ambulatorio). Obtiene un Accuracy engañoso de **79.93%**, pero su Sensibilidad es de **0.00%** (es incapaz de detectar a ningún hospitalizado) y su ROC-AUC es de **0.5000**, equivalente al azar.  
  > **Al evaluar nuestro modelo de Gradient Boosting en prueba:** logramos un Accuracy del **84.16%**, una Precisión del **69.10%** y un **ROC-AUC sobresaliente de 0.8260**. Además, en PR-AUC alcanzamos **0.6021**, triplicando la precisión promedio del nulo que era de 0.2007."*
* *(Presionas flecha `→` para pasar a Slide 10)*

#### Diapositiva 10: Veredicto Frente al Nulo y Límites Críticos
* **En pantalla:** Slide 10 (`2.3 Diagnóstico y Límites`)
* **Qué decir:**
  > *"¿El modelo le gana al nulo? **Sí, contundentemente.** No solo supera el Accuracy base, sino que donde realmente gana es en discriminación: un ROC-AUC de 0.8260 frente a 0.5000. La gráfica de importancia demuestra que la presencia de tuberculosis pulmonar, neumonía oportunista y no tener aseguramiento son los predictores determinantes de riesgo.  
  > **Límites críticos de lo que NO se puede concluir:**  
  > 1. El modelo no sustituye la evaluación médica: es un triaje probabilístico para priorizar camas.  
  > 2. Correlación no es causalidad: tener o no seguro no causa la enfermedad, marca tiempos de consulta tardía.  
  > 3. El modelo es específico para el contexto urbano de Medellín entre 2012 y 2023; requiere calibración si se lleva a zonas rurales."*
* *(Presionas flecha `→` para pasar a Slide 11)*

---

### ⏱️ Minuto 7:30 – 8:15 | Diapositiva 11: Conclusiones y Cierre
* **En pantalla:** Slide 11 (`Conclusiones`)
* **Qué decir:**
  > *"Para concluir este Quinto Parcial:  
  > 1. Demostramos que una reparación honesta preserva la varianza sin sesgar la muestra eliminando filas con datos faltantes.  
  > 2. El análisis gráfico reveló cómo choques externos como el COVID-19 alteran la vigilancia epidemiológica generando falsas caídas en la incidencia.  
  > 3. Construimos un modelo supervisado reproducible sin fuga de datos que supera al nulo en ROC-AUC (0.8260 vs 0.5000) y sirve como herramienta cuantitativa de apoyo en salud pública.  
  > Muchas gracias por su atención."*

---

¡Y listo! Con esto cubres el 100% de los criterios de la rúbrica en un tiempo exacto y cómodo de entre 7 y 8 minutos.
