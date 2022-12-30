import time
def seleccion_orden(s,n):
    for posicion in range(n):
        pequeño = s[posicion]
        posterior = posicion
        for i in range(posicion+1,n):
            if s[i]<pequeño:
                pequeño=s[i]
                posterior = i
        s[posicion],s[posterior] = s[posterior],s[posicion]

lista = [10,11,12,13,14,15,16,17,18,19,20,2,3,4,5,6,7,8,9,1,50,60,54,32]
listaNueva = lista
contador1 = time.perf_counter()
seleccion_orden(listaNueva,len(listaNueva))
contador2 = time.perf_counter()
print("El tiempo de demora es: ",contador2-contador1)
print("La lista ordenada es: ",listaNueva)
