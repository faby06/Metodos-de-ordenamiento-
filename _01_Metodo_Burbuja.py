 #Metodo Buerbuja              
def burbuja(lista):
    n = len(lista)

    for i in range(n):# Recorre todos los elementos de la lista
        for j in range(0, n - i - 1):#Su proposito es recorrer los elementos de la lista y comparar elementos adyacentes para realizar el intercambio si es necesario.
            if lista[j] > lista[j + 1]:#Aqui se verifica si el elemento que esta en la posicion actual j es mayor que el elemento siguiente(j+1)
                #Donde si la condiciones verdadera se hace la linea de abajo 
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #se intercambian de posicion

#Esta es la lista que va recorrer 
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista Desordenada")
print(lista)
burbuja(lista)
print("Lista ordenada Metodo Burbuja")
print(lista)