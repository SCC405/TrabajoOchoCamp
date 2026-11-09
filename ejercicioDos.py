#Ejercicio 2

n = int(input("Digite el tamaño de la matriz: "))


def imprimir(matriz):
    for fila in matriz:
        for valor in fila:
            print(valor, end="\t")
        print()
    print()


# Matriz 1: numeros seguidos por filas
matriz = []
numero = 1
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(numero)
        numero = numero + 1
    matriz.append(fila)
print("Matriz 1")
imprimir(matriz)

# Matriz 2: filas pares de 1 a n, filas impares de n a 1
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i % 2 == 0:
            fila.append(j + 1)
        else:
            fila.append(n - j)
    matriz.append(fila)
print("Matriz 2")
imprimir(matriz)

# Matriz 3: diagonal principal
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print("Matriz 3")
imprimir(matriz)

# Matriz 4: diagonal secundaria
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print("Matriz 4")
imprimir(matriz)

# Matriz 5: triangulo inferior
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if j <= i:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print("Matriz 5")
imprimir(matriz)

# Matriz 6: triangulo superior
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if j >= i:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print("Matriz 6")
imprimir(matriz)

# Matriz 7: numeros seguidos por columnas
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(j * n + i + 1)
    matriz.append(fila)
print("Matriz 7")
imprimir(matriz)

# Matriz 8: triangulo con A y B
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if j <= i:
            if j % 2 == 0:
                fila.append("A")
            else:
                fila.append("B")
        else:
            fila.append(" ")
    matriz.append(fila)
print("Matriz 8")
imprimir(matriz)