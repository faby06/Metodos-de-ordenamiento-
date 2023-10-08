#Metodo HeapSort
def heapSort(lista):
    n = len(lista)  

    # Construye un heap maximo
    for i in range(n // 2 - 1, -1, -1):
        ajustar(lista, n, i)

    # Extrae elementos uno por uno desde ajustar
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Intercambia el elemento maximo con el ultimo
        ajustar(lista, i, 0)

def ajustar(lista, n, i):
    mayor = i  # Inicializa el nodo raiz como el mas grande
    izquierda = 2 * i + 1  # Indice del hijo izquierdo
    derecha = 2 * i + 2  # Indice del hijo derecho

    # Compara el nodo raiz con el hijo izquierdo y el hijo derecho, si existen
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda

    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha

    # Si el nodo raiz no es el mas grande intercambia con el mas grande
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]  # Intercambia los valores
        ajustar(lista, n, mayor)  

lista = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista)
heapSort(lista)
print("Lista ordenada:", lista)
