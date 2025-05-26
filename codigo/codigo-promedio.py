def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    lista (list): Una lista de números (int o float). Puede estar vacía.

    Retorna:
    float: El promedio de los números en la lista. Si la lista está vacía, retorna 0.

    Ejemplo:
    >>> calcular_promedio([7, 10, 12, 15, 8])
    10.4
    """
    if not lista:
        return 0
    return sum(lista) / len(lista)


# Ejemplo de uso
numeros = [7, 10, 12, 15, 8]
print(calcular_promedio(numeros))
