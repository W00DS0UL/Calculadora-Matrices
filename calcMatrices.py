from fractions import Fraction

def crear_matriz(filas, columnas, datos):
    if len(datos) != filas or any(len(f) != columnas for f in datos):
        raise ValueError("Dimensiones de los datos no coinciden con filas y columnas")
    return [[Fraction(x) for x in fila] for fila in datos]

def imprimir_matriz(matriz):
    return '\n'.join([' '.join(map(str, fila)) for fila in matriz])

def copia_matriz(matriz):
    return [fila[:] for fila in matriz]

def es_cuadrada(matriz):
    return len(matriz) == len(matriz[0])

def eliminacion_gauss_jordan(matriz):
    n, m = len(matriz), len(matriz[0])
    matriz = copia_matriz(matriz)
    pasos = []

    for i in range(n):
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    pasos.append(f"Intercambiar fila {i + 1} con fila {j + 1}")
                    break
            else:
                raise ValueError("No se puede aplicar Gauss-Jordan, pivote cero sin intercambios posibles.")

        pivote = matriz[i][i]
        matriz[i] = [x / pivote for x in matriz[i]]
        pasos.append(f"Dividir fila {i + 1} por {pivote}")

        for j in range(n):
            if i != j:
                factor = matriz[j][i]
                matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(m)]
                pasos.append(f"Restar {factor} veces la fila {i + 1} de la fila {j + 1}")

    pasos.append("Resultado final:")
    pasos.append(imprimir_matriz(matriz))
    print("\n".join(pasos))
    return matriz

def submatriz(matriz, fila, columna):
    return [[matriz[i][j] for j in range(len(matriz)) if j != columna] for i in range(len(matriz)) if i != fila]

def obtener_determinante(matriz):
    if not es_cuadrada(matriz):
        raise ValueError("El determinante solo se puede calcular para matrices cuadradas")

    if len(matriz) == 1:
        return matriz[0][0]

    return sum(
        (-1) ** c * matriz[0][c] * obtener_determinante(submatriz(matriz, 0, c))
        for c in range(len(matriz))
    )

def adjunta_matriz(matriz):
    n = len(matriz)
    return [[
        (-1) ** (i + j) * obtener_determinante(submatriz(matriz, i, j))
        for j in range(n)] for i in range(n)]

def transpuesta(matriz):
    return list(map(list, zip(*matriz)))

def inversa_adjuncion(matriz):
    if not es_cuadrada(matriz):
        raise ValueError("La inversa solo se puede calcular para matrices cuadradas")

    det = obtener_determinante(matriz)
    if det == 0:
        raise ValueError("La matriz no tiene inversa porque su determinante es 0")

    adj = adjunta_matriz(matriz)
    adj_t = transpuesta(adj)
    return [[Fraction(adj_t[i][j], det) for j in range(len(matriz))] for i in range(len(matriz))]

def inversa_gauss_jordan(matriz):
    if not es_cuadrada(matriz):
        raise ValueError("La inversa solo se puede calcular para matrices cuadradas")

    n = len(matriz)
    m_ext = [fila + [Fraction(1) if i == j else Fraction(0) for j in range(n)] for i, fila in enumerate(copia_matriz(matriz))]
    pasos = []

    for i in range(n):
        if m_ext[i][i] == 0:
            for j in range(i + 1, n):
                if m_ext[j][i] != 0:
                    m_ext[i], m_ext[j] = m_ext[j], m_ext[i]
                    pasos.append(f"Intercambiar fila {i + 1} con fila {j + 1}")
                    break
            else:
                raise ValueError("No se puede calcular la inversa con el método de Gauss-Jordan debido a un pivote cero")

        pivote = m_ext[i][i]
        m_ext[i] = [x / pivote for x in m_ext[i]]
        pasos.append(f"Dividir fila {i + 1} por {pivote}")

        for j in range(n):
            if i != j:
                factor = m_ext[j][i]
                m_ext[j] = [m_ext[j][k] - factor * m_ext[i][k] for k in range(2 * n)]
                pasos.append(f"Restar {factor} veces la fila {i + 1} de la fila {j + 1}")

    inversa = [fila[n:] for fila in m_ext]
    pasos.append("Resultado final:")
    pasos.append(imprimir_matriz(inversa))
    print("\n".join(pasos))
    return inversa

def suma_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices deben tener las mismas dimensiones")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def resta_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices deben tener las mismas dimensiones")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("# columnas A debe ser igual al # filas B")
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            total = sum(A[i][k] * B[k][j] for k in range(len(B)))
            fila.append(total)
        resultado.append(fila)
    return resultado

def multiplicacion_escalar(matriz, escalar):
    return [[element * escalar for element in fila] for fila in matriz]

def resolver_cramer(matriz):
    """Resuelve Ax = b usando la regla de Cramer con una matriz aumentada [A | b]"""
    n = len(matriz)
    if any(len(fila) != n + 1 for fila in matriz):
        raise ValueError("La matriz aumentada debe tener n filas y n+1 columnas")

    A = [fila[:-1] for fila in matriz]  # Matriz de coeficientes
    b = [[fila[-1]] for fila in matriz]  # Vector columna

    det_A = obtener_determinante(A)
    if det_A == 0:
        raise ValueError("El sistema no tiene solución única porque el determinante de A es 0")

    soluciones = []
    for i in range(n):
        A_i = copia_matriz(A)
        for fila in range(n):
            A_i[fila][i] = b[fila][0]
        det_A_i = obtener_determinante(A_i)
        x_i = Fraction(det_A_i, det_A)
        soluciones.append([x_i])  # Resultado como vector columna

    return soluciones

def menu_matrices():
    matrices = []
    while True:
        print("\nMENÚ DE MATRICES")
        print("1. Crear nueva matriz")
        print("2. Ver matrices actuales")
        print("3. Realizar operación")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
                datos = []
                for i in range(filas):
                    fila = input(f"Fila {i+1} (separada por espacios): ").split()
                    if len(fila) != columnas:
                        raise ValueError("Número de elementos incorrecto en la fila")
                    datos.append([float(x) for x in fila])
                nueva = crear_matriz(filas, columnas, datos)
                matrices.append(nueva)
                print("Matriz guardada con índice " + str(len(matrices) - 1))
            except Exception as e:
                print(f"Error al crear matriz: {e}")

        elif opcion == '2':
            if not matrices:
                print("No hay matrices almacenadas")
            for i, m in enumerate(matrices):
                print(f"\n{i}:\n{imprimir_matriz(m)}")

        elif opcion == '3':
            while True:
                print("\nOPERACIONES DISPONIBLES")
                print("a. Sumar dos matrices")
                print("b. Restar dos matrices")
                print("c. Multiplicar dos matrices")
                print("d. Multiplicación escalar")
                print("e. Determinante")
                print("f. Inversa (Adjuncion)")
                print("g. Inversa (Gauss-Jordan)")
                print("h. Eliminación Gauss-Jordan")
                print("i. Regla de Cramer")
                print("j. Salir del menú de operaciones")
                oper = input("Seleccione una operación: ").lower()

                if oper == 'j':
                    break

                try:
                    if oper in 'abc':
                        i1 = int(input("Índice de la primera matriz: "))
                        i2 = int(input("Índice de la segunda matriz: "))
                        if oper == 'a':
                            resultado = suma_matrices(matrices[i1], matrices[i2])
                        elif oper == 'b':
                            resultado = resta_matrices(matrices[i1], matrices[i2])
                        else:
                            resultado = multiplicar_matrices(matrices[i1], matrices[i2])
                    elif oper == 'd':
                        i1 = int(input("Índice de la matriz: "))
                        esc = float(input("Escalar: "))
                        resultado = multiplicacion_escalar(matrices[i1], esc)
                    elif oper == 'e':
                        i1 = int(input("Índice de la matriz: "))
                        resultado = obtener_determinante(matrices[i1])
                        print(f"Determinante: {resultado}")
                        continue
                    elif oper == 'f':
                        i1 = int(input("Índice de la matriz: "))
                        resultado = inversa_adjuncion(matrices[i1])
                    elif oper == 'g':
                        i1 = int(input("Índice de la matriz: "))
                        resultado = inversa_gauss_jordan(matrices[i1])
                    elif oper == 'h':
                        i1 = int(input("Índice de la matriz: "))
                        resultado = eliminacion_gauss_jordan(matrices[i1])
                    elif oper == 'i':
                        i1 = int(input("Índice de la matriz: "))
                        resultado = resolver_cramer(matrices[i1])
                        print("Solución del sistema (como vector columna):")
                        print(imprimir_matriz(resultado))
                    else:
                        print("Opción no válida")
                        continue

                    print("\nResultado:")
                    print(imprimir_matriz(resultado) if isinstance(resultado, list) else resultado)
                except Exception as e:
                    print(f"Error: {e}")

        elif opcion == '4':
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_matrices()
