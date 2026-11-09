#Ejercicio 3

inventario = []

while True:

    print("""
    MENÚ
    1. Agregar producto
    2. Agregar lote de productos
    3. Eliminar producto del inventario
    4. Eliminar el producto más reciente
    5. Ordenar productos alfabéticamente
    6. Mostrar número total de productos
    7. Salir
    """)

    opcion = int(input("Digite una opcion: "))

    if opcion == 1:
        producto = input("Nombre del producto: ")
        inventario.append(producto)
        print("Producto agregado")

    elif opcion == 2:
        cantidad = int(input("Cuantos productos tiene el lote: "))
        for i in range(cantidad):
            print("Producto", i + 1)
            producto = input()
            inventario.append(producto)
        print("Lote agregado")

    elif opcion == 3:
        producto = input("Producto a eliminar: ")
        if producto in inventario:
            inventario.remove(producto)
            print("Producto eliminado")
        else:
            print("Ese producto no esta en el inventario")

    elif opcion == 4:
        if len(inventario) == 0:
            print("El inventario esta vacio")
        else:
            eliminado = inventario.pop()
            print("Se elimino el producto mas reciente:", eliminado)

    elif opcion == 5:
        inventario.sort()
        print("Productos ordenados:", inventario)

    elif opcion == 6:
        print("Total de productos:", len(inventario))
        print("Inventario:", inventario)

    elif opcion == 7:
        break

    else:
        print("Error digite de nuevo")

print("Gracias por usar el programa")