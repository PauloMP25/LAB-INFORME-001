import time
def factorial_uno(n):
    if n<=1:
        return 1
    return n*factorial_uno(n-1)
def factorial_dos(n):
    resultado = 1
    for i in range(n):
        resultado*=(i+1)
    return resultado
n = int(input("Ingrese un numero: "))
contador1 = time.perf_counter()
print(f"El factorial de {n} es",factorial_uno(n))
print("Tiempo de la primera funcion",contador1)
contador2 = time.perf_counter()
print(f"El factorial de {n} es",factorial_dos(n))
print("Tiempo de la segunda funcion",contador2)

