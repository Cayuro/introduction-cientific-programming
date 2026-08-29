# Introducción a la Programación Científica — Evaluación 1

**Periodo:** 2026-2  
**Proyecto:** Vigilancia Epidemiológica y Análisis de Dinámica Temporal y Factores Sociodemográficos del VIH/SIDA en Medellín (2012–2023)  
**Dataset:** SIVIGILA — Sistema de Vigilancia en Salud Pública (Alcaldía de Medellín / Datos Abiertos)

---

## 1. Definición del Problema (Plantilla Oficial del Proyecto)

- **Problema:**  
  El Virus de la Inmunodeficiencia Humana (VIH) y el Síndrome de Inmunodeficiencia Adquirida (SIDA) constituyen un reto prioritario de salud pública global y local. A pesar de los avances en diagnóstico y tratamiento antirretroviral, persisten disparidades significativas en la notificación oportuna, el acceso al sistema de salud según el régimen de afiliación y las fluctuaciones temporales causadas por eventos disruptivos (como la pandemia de COVID-19 en 2020). Comprender los factores epidemiológicos, los retrasos en la consulta y los perfiles sociodemográficos en Medellín es fundamental para diseñar políticas públicas efectivas y fundamentadas en evidencia.

- **Objetivos:**
  - **Objetivo General:** Desarrollar un pipeline reproducible de ciencia de datos para auditar, depurar, imputar y analizar los registros epidemiológicos de VIH/SIDA en Medellín notificados al SIVIGILA entre 2012 y 2023.
  - **Objetivos Específicos:**
    1. Implementar un flujo metodológico riguroso (Lectura controlada $\rightarrow$ Parseo semántico $\rightarrow$ Depuración por reglas de dominio $\rightarrow$ Imputación empírica preservadora de la distribución).
    2. Cuantificar la **dinámica temporal multianual** y evaluar el **efecto de la pandemia por COVID-19 (2020)** sobre el ritmo de notificaciones y la detección oportuna.
    3. Medir el **tiempo de retraso diagnóstico** (intervalo entre el inicio de síntomas y la consulta médica) y su asociación con variables de aseguramiento en salud (`tip_ss_`).
    4. Identificar la distribución por ciclos de vida, sexo biológico, comorbilidades e infecciones oportunistas asociadas.

- **Alcance (qué entra y qué no):**
  - *Incluye:* Todos los eventos de notificación de VIH/SIDA registrados en Medellín en el periodo 2012–2023 con validación de consistencia temporal, demográfica y territorial.
  - *Excluye:* Modelos predictivos de aprendizaje automático complejo (fuera del alcance de la Evaluación 1, enfocado en depuración rigurosa y análisis descriptivo reproducible). No se extrapolan conclusiones a municipios fuera del área metropolitana del Valle de Aburrá.

- **Dataset:**
  - **Nombre:** Casos de VIH/SIDA SIVIGILA Medellín (2012–2023).
  - **Fuente:** Portal de Datos Abiertos de la Alcaldía de Medellín / Instituto Nacional de Salud (INS).
  - **Dimensiones:** 15.470 filas y 116 columnas.
  - **Licencia:** Datos Abiertos de Gobierno de Colombia (Uso público).

- **Variable(s) de interés:**
  - `fec_not`, `fec_con_`, `ini_sin_`, `fecha_nto_` (Fechas de notificación, consulta, inicio de síntomas y nacimiento).
  - `año`, `mes_caso`, `semana`, `periodo_epid` (Coordenadas temporales y epidemiológicas).
  - `edad_`, `sexo_`, `ide_genero`, `grupo_edad_ciclo`, `grupo_edad_quinque`, `estrato_` (Perfil sociodemográfico).
  - `tip_ss_` (Régimen de seguridad social: Contributivo, Subsidiado, No asegurado, Especial).
  - `nombre_comuna`, `nombre_barrio` (Ubicación territorial).
  - `pac_hos_`, `con_fin_`, `tub_pul`, `sar_kap`, `hep_b`, `hep_c` (Gravedad clínica y comorbilidades).

- **Limitaciones conocidas del dato:**
  - **Subregistro y retraso de notificación:** Especialmente durante 2020 debido a las restricciones sanitarias de la pandemia.
  - **Campos no informados:** El 21.8% de los registros presenta `nombre_comuna` como `"Sin Información"`.
  - **Centinelas:** Presencia de valores centinela (`99999.07`, `-   -`, `Sin Información`) que requieren recodificación explícita a faltantes.

---

## 2. Flujo Metodológico de Datos

Siguiendo las directrices del curso, el tratamiento de los datos respeta estrictamente las cuatro etapas secuenciales:

```text
Leer (I/O)  ──>  Parsear (Tipos)  ──>  Depurar (Dominio)  ──>  Imputar / Preservar Distribución
```

1. **Lectura Controlada:**
   - Detección explícita de encoding (`latin-1`/`utf-8`), separador (`,`) y lista de centinelas para `na_values`.
2. **Parseo Semántico:**
   - Conversión de cadenas a fechas (`pd.to_datetime` con `dayfirst=True`), enteros/flotantes para edad y estrato, y booleanos para indicadores dicotómicos ($1=\text{Sí}, 2=\text{No}$).
   - Auditoría de pérdidas generadas durante el parseo (`perdidos_en_parseo`).
3. **Auditoría y Depuración:**
   - Matriz de calidad de datos con conteo de nulos, porcentajes y cardinalidad única.
   - Aplicación de reglas de coherencia temporal ($Fecha\_Notificación \ge Fecha\_Consulta \ge Fecha\_Inicio\_Síntomas \ge Fecha\_Nacimiento$).
4. **Imputación Científicamente Defendible:**
   - Se evita la imputación por media/mediana global para no distorsionar la varianza ni crear picos artificiales.
   - Aplicación de **muestreo empírico aleatorio (*hot-deck*)** con semilla (`np.random.default_rng`) e imputación agrupada.
   - Evaluación comparativa **Antes vs. Después** mediante estadísticos descriptivos (`.describe()`).

---

## 3. Estructura del Proyecto

```text
introduction-cientific-programming/
├── README.md                   # Documentación principal y ficha técnica de la Evaluación 1
├── requirements.txt            # Dependencias del entorno en Python
├── data/
│   ├── sivigila_vih.csv        # Dataset crudo original (15.470 registros, 116 columnas)
│   └── resultados_vih_santiago.xlsx
└── notebooks/
    ├── analisis_dinamica_temporal_juanes.ipynb  # Pipeline completo + Dinámica Temporal y Efecto Pandemia
    ├── analisis_santiago.ipynb                  # Análisis sociodemográfico general
    └── analisis_descriptivo.ipynb
```

---

## 4. Notebooks y Análisis

### [`analisis_dinamica_temporal_juanes.ipynb`](notebooks/analisis_dinamica_temporal_juanes.ipynb)
- **Autor:** Juanes
- **Enfoque:**
  - Implementación exhaustiva de las 4 etapas del flujo de datos con auditoría y muestreo empírico.
  - **Dinámica temporal multianual (2012–2023):** Análisis de tendencias anuales y comportamiento estacional por período epidemiológico.
  - **Cuantificación del Efecto Pandemia (COVID-19):** Diagnóstico del choque en 2020 y la dinámica de recuperación en 2021–2022.
  - **Retraso Diagnóstico:** Cálculo del tiempo transcurrido entre la aparición de síntomas y la atención médica ($\Delta t = \text{Fecha Consulta} - \text{Fecha Inicio Síntomas}$) según régimen de salud.

### [`analisis_santiago.ipynb`](notebooks/analisis_santiago.ipynb)
- **Autor:** Santiago
- **Enfoque:** Exploración inicial de proporciones por sexo, distribución por edades y principales comunas con mayor volumen de casos.

---

## 5. Instalación y Uso

1. Clonar el repositorio y acceder a la carpeta:
   ```bash
   git clone https://github.com/tu-usuario/introduction-cientific-programming.git
   cd introduction-cientific-programming
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar las dependencias exactas:
   ```bash
   pip install -r requirements.txt
   ```

4. Iniciar Jupyter Notebook para reproducir los análisis:
   ```bash
   jupyter notebook
   ```

---

## 6. Autores

- **Juanes** ([`analisis_dinamica_temporal_juanes.ipynb`](notebooks/analisis_dinamica_temporal_juanes.ipynb))
- **Santiago** ([`analisis_santiago.ipynb`](notebooks/analisis_santiago.ipynb))
- **Equipo de Introducción a la Programación Científica — 2026-2**
