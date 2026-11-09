#Ejercicio 5 - Super Reduced String

def superReducedString(s):
    pila = []
    for letra in s:
        if len(pila) > 0 and pila[-1] == letra:
            pila.pop()
        else:
            pila.append(letra)

    resultado = ""
    for letra in pila:
        resultado = resultado + letra

    if resultado == "":
        return "Empty String"
    else:
        return resultado


s = input("Digite la cadena: ")
print(superReducedString(s))