import random
import time

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # crear matrices temporales.
    L = [0] * (n1)
    R = [0] * (n2)

    # Copiar los datos a las matrices temporales L[] y R[].
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Combinar las matrices temporales de nuevo en arr[l..r].
    i = 0   # Índice inicial de la primera submatriz.
    j = 0   # Índice inicial de la segunda submatriz.
    k = l   # Índice inicial de la submatriz fusionada.

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si los hay.
    # hay alguno.
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si los hay.
    # hay alguno.
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l es el índice izquierdo y r es el índice derecho de la.
# sub-array de arr a ordenar.
def mergeSort(arr, l, r):
    if l < r:
        # Igual que (l+r)//2, pero evita el desbordamiento para. # grandes l y h.
        # grandes l y h.
        m = (l + (r - 1)) // 2

        # Ordena la primera y la segunda mitad.
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)