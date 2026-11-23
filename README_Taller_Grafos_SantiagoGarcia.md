# Taller de Grafos · Problema 4.3: Transbordos y minutos
**Curso:** Introducción a la Programación Científica — Periodo 2026-2  
**Estudiante:** Santiago García  
**Fecha de entrega:** Miércoles 18 de noviembre de 2026  
**Entregables:**
1. Archivo interactivo autónomo: [`transbordos_y_minutos-SantiagoGarcia.html`](transbordos_y_minutos-SantiagoGarcia.html) (también disponible en [`grafos/index.html`](grafos/index.html)).
2. Video explicativo de 4 a 6 minutos demostrando la ejecución del laboratorio interactivo.

---

## 1. Planteamiento del Problema

### Enunciado formal (Problema 4.3)
> Una red pequeña de bus, metro o cable. Las estaciones son los vértices. Cambiar de línea o tomar un tramo directo es seguir una arista. Cada tramo dura unos minutos, siempre un número positivo.  
> **Pregunta:** ¿Qué ruta hace menos transbordos? ¿Qué ruta tarda menos minutos?  
> **Algoritmos:** BFS para los transbordos. Dijkstra para los minutos.  
> **Qué se ve:** Un par origen–destino en el que la ruta de menos transbordos tarda más. Los dos tiempos quedan expresados en minutos.

### La Pregunta en una oración
> **«¿Qué ruta realiza el menor número de transbordos y qué ruta tarda el menor tiempo en minutos desde Terminal Norte hasta Hospital Universitario, y por qué difieren?»**

---

## 2. Grafo Propio: Red Intermodal de Transporte Urbano

El grafo modela un sistema metropolitano integrado de 8 estaciones ($A$ a $H$) con 13 conexiones bidireccionales clasificadas en tres tipologías de transporte con velocidades de operación muy distintas:
- **Línea de Metro Troncal (Férreo):** Vía exclusiva de alta velocidad ($3$ a $4$ min por tramo).
- **Línea de Metrocable (Ladera montañosa):** Cabinas continuas de baja velocidad sobre pendientes ($11$ a $18$ min por tramo).
- **Red Tranviaria y Alimentadores:** Enlaces secundarios a nivel ($5$ a $10$ min por tramo).

### Vértices (8 Estaciones)
| Vértice | Nombre de la Estación | Rol en la Red | Coordenadas $(X, Y)$ |
| :---: | :--- | :--- | :---: |
| **A** | Terminal Norte | Origen principal de viajes del norte | $(130, 200)$ |
| **B** | Cable Mirador | Estación turística de ladera / montaña | $(480, 90)$ |
| **C** | Parque Universidad | Corredor férreo estudiantil | $(240, 340)$ |
| **D** | Estación Central | Nodo neurálgico de transferencia | $(480, 340)$ |
| **E** | Distrito Tecnológico | Corredor férreo sur innovación | $(720, 340)$ |
| **F** | Portal Occidente | Conexión transversal residencial oeste | $(170, 490)$ |
| **G** | Bulevar Comercial | Zona bancaria y centro de comercio | $(580, 490)$ |
| **H** | Hospital Universitario | Destino médico y terminal sur | $(830, 200)$ |

### Lista de Adyacencia y Tiempos de Viaje (Minutos)
Cada arista tiene un peso estrictamente positivo ($w > 0$):

```text
A (Terminal Norte)        -> B (18 min, Cable), C (3 min, Metro), F (6 min, Tranvía)
B (Cable Mirador)         -> A (18 min, Cable), D (11 min, Cable), H (17 min, Cable)
C (Parque Universidad)    -> A (3 min, Metro), D (4 min, Metro), F (5 min, Tranvía)
D (Estación Central)      -> B (11 min, Cable), C (4 min, Metro), E (3 min, Metro), G (5 min, Tranvía)
E (Distrito Tecnológico)  -> D (3 min, Metro), G (7 min, Tranvía), H (4 min, Metro)
F (Portal Occidente)      -> A (6 min, Tranvía), C (5 min, Tranvía), G (8 min, Tranvía)
G (Bulevar Comercial)     -> D (5 min, Tranvía), E (7 min, Tranvía), F (8 min, Tranvía), H (10 min, Tranvía)
H (Hospital Universitario)-> B (17 min, Cable), E (4 min, Metro), G (10 min, Tranvía)
```

---

## 3. Comparativa de Algoritmos

### BFS (Amplitud) — Optimización de Transbordos
- **Estructura de datos:** Cola FIFO (`collections.deque`).
- **Mecánica:** Explora por capas concéntricas de saltos. Asume implícitamente que cada arista tiene costo 1 (un transbordo/tramo).
- **Ruta encontrada:** `A → B → H`
  - **Tramos (aristas):** **2 tramos** (1 transbordo intermedio).
  - **Tiempo total acumulado:** $18 + 17 =$ **35 minutos**.

### Dijkstra — Optimización de Tiempo Real
- **Estructura de datos:** Cola de prioridad / Min-Heap (`heapq`).
- **Mecánica:** En cada paso extrae el nodo provisional con menor tiempo acumulado en minutos y relaja sus aristas adyacentes.
- **Ruta encontrada:** `A → C → D → E → H`
  - **Tramos (aristas):** **4 tramos** (3 transbordos intermedios).
  - **Tiempo total acumulado:** $3 + 4 + 3 + 4 =$ **14 minutos**.

### ¿Por qué difieren las dos respuestas?
BFS responde estrictamente a la pregunta «¿cuál ruta usa menos aristas?», ignorando por completo el tiempo que toma recorrer cada tramo. La conexión por Cable Mirador une el norte con el sur en solo 2 saltos, pero es un sistema de montaña con velocidad reducida.  
Dijkstra, en cambio, toma en cuenta los pesos en minutos: circular por el tren férreo segregado requiere 4 estaciones, pero a alta velocidad, tardando únicamente **14 minutos contra 35 minutos** de la ruta de menos transbordos (**ahorro neto de 21 minutos, más del 60% más rápido**).

---

## 4. Implementación en Python 3

```python
import heapq
from collections import deque

# Grafo modelado con lista de adyacencia y pesos en minutos
grafo = {
    'A': [('B', 18), ('C', 3), ('F', 6)],
    'B': [('A', 18), ('D', 11), ('H', 17)],
    'C': [('A', 3), ('D', 4), ('F', 5)],
    'D': [('B', 11), ('C', 4), ('E', 3), ('G', 5)],
    'E': [('D', 3), ('G', 7), ('H', 4)],
    'F': [('A', 6), ('C', 5), ('G', 8)],
    'G': [('D', 5), ('E', 7), ('F', 8), ('H', 10)],
    'H': [('B', 17), ('E', 4), ('G', 10)]
}

def bfs_transbordos(grafo, origen, destino):
    """Minimiza número de transbordos/aristas usando cola FIFO."""
    cola = deque([origen])
    visitados = {origen}
    padre = {origen: None}
    while cola:
        u = cola.popleft()
        if u == destino:
            break
        for v, _ in grafo[u]:
            if v not in visitados:
                visitados.add(v)
                padre[v] = u
                cola.append(v)
    ruta, curr = [], destino
    while curr:
        ruta.append(curr); curr = padre.get(curr)
    return ruta[::-1]

def dijkstra_minutos(grafo, origen, destino):
    """Minimiza tiempo de viaje en minutos usando Min-Heap."""
    pq = [(0, origen)]
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0
    padre = {origen: None}
    confirmados = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in confirmados: continue
        confirmados.add(u)
        if u == destino: break
        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                padre[v] = u
                heapq.heappush(pq, (dist[v], v))
    ruta, curr = [], destino
    while curr:
        ruta.append(curr); curr = padre.get(curr)
    return ruta[::-1], dist[destino]

# Ejecución
print("Ruta BFS (Menos transbordos):", bfs_transbordos(grafo, 'A', 'H'))
# -> ['A', 'B', 'H'] (2 tramos, 35 min)

ruta_dij, tiempo = dijkstra_minutos(grafo, 'A', 'H')
print(f"Ruta Dijkstra (Menos minutos): {ruta_dij} en {tiempo} minutos")
# -> ['A', 'C', 'D', 'E', 'H'] en 14 minutos
```

---

## 5. Guion Estructurado para el Video Explicativo (4 a 6 Minutos)

Para grabar el video en pantalla mostrando [`transbordos_y_minutos-SantiagoGarcia.html`](transbordos_y_minutos-SantiagoGarcia.html):

| Tiempo | Sección | Qué mostrar y qué decir |
| :---: | :--- | :--- |
| **0:00 - 1:00** | **Portada y Pregunta** | Mostrar Slide 0 y Slide 1. Decir: *"Buenas tardes, mi nombre es Santiago García, estudiante de Introducción a la Programación Científica. Presento la solución al Problema 4.3: Transbordos y minutos. La pregunta en una oración es: ¿Qué ruta realiza el menor número de transbordos y qué ruta tarda el menor tiempo en minutos desde Terminal Norte hasta Hospital Universitario, y por qué difieren?"* |
| **1:00 - 2:00** | **Grafo y Adyacencia** | Pasar a Slide 2. Explicar los 8 vértices ($A$ a $H$) y las 13 aristas con sus tiempos en minutos. Mostrar la tabla de adyacencia y destacar las tres tecnologías de transporte: Metro férreo (azul), Metrocable (naranja) y Tranvía (verde). Confirmar que todos los pesos son positivos ($w > 0$). |
| **2:00 - 4:00** | **Laboratorio en Vivo** | Pasar a Slide 4 (Laboratorio). Seleccionar origen $A$ y destino $H$.<br>1. **Ejecutar BFS:** Mostrar cómo la cola FIFO procesa nivel a nivel; descubre $B$, $C$ y $F$ a 1 tramo, y desde $B$ salta a $H$ en solo 2 tramos.<br>2. **Cambiar a Dijkstra:** Mostrar la cola de prioridad (`pq`); cómo avanza por los tramos rápidos de metro ($C$ a 3 min, $F$ a 6 min, $D$ a 7 min, $E$ a 10 min) y confirma $H$ en solo 14 minutos antes de que el cable siquiera termine. |
| **4:00 - 5:15** | **Comparación y Respuesta** | Pasar a Slide 5. Mostrar las dos rutas lado a lado en los minimapas.<br>- Ruta BFS: $A \to B \to H$ (**2 tramos, 35 minutos**).<br>- Ruta Dijkstra: $A \to C \to D \to E \to H$ (**4 tramos, 14 minutos**).<br>Explicar la causa matemática: BFS asume pesos iguales (1 por arista), mientras que Dijkstra optimiza el costo ponderado real. |
| **5:15 - 6:00** | **Código Python y Cierre** | Pasar a Slide 6 y 7. Mostrar la implementación en Python con `deque` y `heapq`. Concluir con la lección de ingeniería de transporte: *a veces hacer transbordos en modos veloces ahorra más de la mitad del tiempo de viaje*. |

---

## 6. Verificación de Criterios del Taller

- [x] **Problema:** Uno de los 10 enunciados oficiales (4.3 Transbordos y minutos).
- [x] **Pregunta:** Formulada con exactitud en una sola oración.
- [x] **Grafo:** Propio, de 8 vértices (rango permitido: 6 a 14), con pesos positivos y lista de adyacencia idéntica al dibujo.
- [x] **Algoritmos:** BFS cuenta tramos/transbordos; Dijkstra minimiza minutos continuos reales.
- [x] **Respuesta y comparación:** Ambas rutas calculadas, con unidades exactas (tramos y minutos) y justificación de su divergencia.
- [x] **Archivo HTML:** 100% autónomo, abre con doble clic sin internet ni librerías externas, controles interactivos funcionando.
- [x] **Código Python:** Modelado profesional con `collections.deque` y `heapq`.
