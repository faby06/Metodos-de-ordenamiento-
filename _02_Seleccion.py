#Metodo de Seleccion
def seleccion(lista):
   
    n = len(lista) # Se calcula la longitud de la lista 

    
    for i in range(n):
        # En cada iteración, encuentra el índice del elemento minimo en el subarray no ordenado.
        a = i
        for j in range(i + 1, n):
            # Compara el elemento actual con el elemento minimo encontrado hasta ahora.
            if lista[j] < lista[a]:
                # Si encuentra un elemento menor, actualiza el 'indice_minimo'.
                a = j

        # Intercambia el elemento actual con el elemento mínimo encontrado.
        # Esto coloca el elemento minimo en la posición 'i'.
        lista[i], lista[a] = lista[a], lista[i]


lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada")
print(lista)
seleccion(lista)
print("Lista ordenada")
print(lista)

