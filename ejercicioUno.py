#Ejercicio 1

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]


ventas = []
for i in range(5):
    fila = []
    print("Producto", i + 1)
    for j in range(7):
        print("  Ventas del", dias[j])
        cantidad = int(input())
        fila.append(cantidad)
    ventas.append(fila)

#PRECIOS
precios = []
for i in range(5):
    print("Precio del producto", i + 1)
    precio = int(input())
    precios.append(precio)

ingresos = []
for i in range(5):
    fila = []
    for j in range(7):
        fila.append(ventas[i][j] * precios[i])
    ingresos.append(fila)

print("\nMATRIZ DE INGRESOS")
for i in range(5):
    print("Producto", i + 1, ":", ingresos[i])

# Pregunta 1
mayor_producto = 0
producto = 0
for i in range(5):
    suma = 0
    for j in range(7):
        suma = suma + ingresos[i][j]
    print("Ingresos producto", i + 1, ":", suma)
    if suma > mayor_producto:
        mayor_producto = suma
        producto = i

print("\nProducto que genera mas ingresos:", producto + 1, "con", mayor_producto, "pesos")

# Pregunta 2
mayor_dia = 0
dia = 0
for j in range(7):
    suma = 0
    for i in range(5):
        suma = suma + ingresos[i][j]
    print("Ingresos del", dias[j], ":", suma)
    if suma > mayor_dia:
        mayor_dia = suma
        dia = j

print("\nDia con mayor ingresos:", dias[dia], "con", mayor_dia, "pesos")