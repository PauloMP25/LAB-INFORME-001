import random
def desordena(a,n):
    for posicion in range(n):
        numero = random.randint(posicion, n-1)
        a[posicion],a[numero] = a[numero],a[posicion]
lista = [1,2,3,5,7,11,13,17,19]
desordena(lista,len(lista))
print(lista)
