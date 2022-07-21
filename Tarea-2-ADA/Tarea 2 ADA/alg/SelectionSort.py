from time import time
import random
import sys

def selectionSort(arr):
    
    n = len(arr)
 
    for i in range(n - 1):
        menor = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[menor]:
                menor = j
 
        arr[i], arr[menor] = arr[menor], arr[i]