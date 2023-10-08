#Metodo ShellSort
def shellSort(lista):
    n = len(lista)  # Obtiene la longitud de la lista
    comparador = n // 2  # Inicializa la brecha como la mitad de la longitud del arreglo

    while comparador > 0:
        # El bucle exterior ejecuta el algoritmo hasta que la brecha sea igual a 1

        for i in range(comparador, n):
            # Recorre el arreglo desde la posicion comparador hasta el final

            temp = lista[i]  # Almacena el valor actual en una variable temporal
            j = i  # Inicializa j con el indice actual

            # El bucle interior realiza inserciones de manera similar al algoritmo de insercion
            while j >= comparador and lista[j - comparador] > temp:
                # Compara el valor actual con el valor comparador-posiciones atrás
                # Si es mayor, mueve el valor comparador-posiciones atrás
                lista[j] = lista[j - comparador]
                j -= comparador  # Actualiza j para continuar revisando hacia atras

            lista[j] = temp  # Coloca el valor temporal en su posicion adecuada

        comparador //= 2  # Reduce la brecha a la mitad para la siguiente iteración


lista = [12, 34, 54, 2, 3]
print("Arreglo original:", lista)
shellSort(lista)  
print("Arreglo ordenado:", lista) 
