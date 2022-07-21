import random
import time

def partition(arr, low, high):
    i = (low - 1) # índice de elemento más pequeño
    pivot = arr[high]  # pivote

    for j in range(low, high):

        
        # Si el elemento actual es menor que o igual a pivote
        if arr[j] <= pivot:
            # índice de incremento del elemento más pequeño
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# La función principal que implementa QuickSort
# arr [] -> Matriz a ordenar,
# bajo -> Índice de inicio,
# alto -> Índice final

# Función para hacer una clasificación rápida

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi es índice de partición, arr [p] es ahora
        # en el lugar correcto
        pi = partition(arr, low, high)

        # Ordenar por separado los elementos antes.
        # partición y después de la partición.
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)