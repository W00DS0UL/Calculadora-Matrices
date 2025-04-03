## **Guía de Usuario - Calculadora de Matrices (Python)**

Esta calculadora de matrices permite crear, visualizar y operar con matrices directamente desde la consola. Es ideal para estudiantes, profesores o cualquier persona que necesite resolver operaciones con matrices de forma rápida.

### **¿Cómo iniciar la calculadora?**

1. Se debe tener Python instalado.
2. Abrir la terminal y ejecuta el archivo:

```bash
python calcMatrices.py
```

Esto iniciará un menú interactivo.

---

## **Menú principal**

Cuando se ejecuta el programa, se verá este menú:

```
MENÚ DE MATRICES
1. Crear nueva matriz
2. Ver matrices actuales
3. Realizar operación
4. Salir
```

### OPCIÓN 1: Crear nueva matriz

- Ingrese el número de filas y columnas.
- Luego, ingrese los valores de cada fila, separando los números con espacio. Ejemplo:

```
Fila 1 (separada por espacios): 1 2 3
Fila 2 (separada por espacios): 4 5 6
```

La matriz se almacenará y se le asignará un índice (por ejemplo, índice 0).

---

### OPCIÓN 2: Ver matrices actuales

Muestra todas las matrices que se han creado, junto con su índice. Este índice se usará para aplicar operaciones.

---

### OPCIÓN 3: Realizar operación

Muestra un submenú con todas las operaciones disponibles:

```
a. Sumar dos matrices
b. Restar dos matrices
c. Multiplicar dos matrices
d. Multiplicación escalar
e. Determinante
f. Inversa (Adjunción)
g. Inversa (Gauss-Jordan)
h. Eliminación Gauss-Jordan
i. Regla de Cramer
j. Salir del menú de operaciones
```

#### Explicación de cada operación:

| Opción | Descripción | Requiere |
|--------|-------------|----------|
| a | Suma de dos matrices | Índice de dos matrices con mismas dimensiones |
| b | Resta de dos matrices | Índice de dos matrices con mismas dimensiones |
| c | Multiplicación matricial | Índice de dos matrices compatibles |
| d | Multiplicación por escalar | Índice de matriz + valor escalar |
| e | Determinante | Matriz cuadrada |
| f | Inversa usando adjunción | Matriz cuadrada con determinante ≠ 0 |
| g | Inversa con Gauss-Jordan | Matriz cuadrada con determinante ≠ 0 |
| h | Eliminación Gauss-Jordan | Matriz aumentada o cuadrada |
| i | Regla de Cramer | Matriz aumentada de n x (n+1) |

---

## **Notas útiles**

- Si se realiza una operación inválida (por ejemplo, sumar matrices de distinto tamaño), el sistema lanzará un mensaje de error.

---
