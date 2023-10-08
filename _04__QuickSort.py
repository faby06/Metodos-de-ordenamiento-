#Metodo QuickSort
def quickSort(lista):
    if len(lista) <= 1:
        return lista  # Si la lista tiene 0 o 1 elemento, esta ordenada

    seleccion_num = lista[len(lista) // 2]  # Selecciona un numero (generalmente se elige el elemento del medio)
    #Despues de comparar el pivote divimos la lista en 3 sublistas 
    izq = [x for x in lista if x < seleccion_num]  # Crea una lista de elementos menores que seleccion_num 
    enmedio = [x for x in lista if x == seleccion_num]  # Crea una lista de elementos iguales a seleccion_num
    der = [x for x in lista if x > seleccion_num]  # Crea una lista de elementos mayores que seleccion_num

    return quickSort(izq) + enmedio + quickSort(der)  # Combina las tres listas ordenadas


lista = [3, 6, 8, 10, 1, 2, 1]
print("Arreglo original:", lista)
arreglo= quickSort(lista)
print("Arreglo ordenado:", arreglo)