def narcissistic(value):
    digits = len(str(value))
    string = str(value)
    lista = []
    lista_inteiros = []
    resultado = 0
    for x in range(digits):
        lista.append(string[x])
        lista_inteiros.append(int(lista[x]))
    for x in range(digits):
        resultado += lista_inteiros[x] ** digits

    narcisita = resultado == value
    return narcisita


print(narcissistic(153))
