import random
import time

def bubbleSort(arr):
    n = len(arr)

    # Recorrer todos los elementos del array.
    for i in range(n - 1):
        # range(n) también funciona pero el bucle exterior se repetirá una vez más de lo necesario.

        # Los últimos i elementos ya están en su lugar.
        for j in range(0, n - i - 1):

            # Recorrer el array de 0 a n-i-1.
            # Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]