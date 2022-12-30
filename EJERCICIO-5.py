def fibonacci_recursivo(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
def fibonacci(n):
    if n==0:
        return 0
    else: 
        a = 0
        b = 1
        for i in range(1,n):
            suma = (a+b)
            a = b
            b = suma
        return b

n = int(input("Ingrese un valor: "))  
print("La suma es: ",fibonacci_recursivo(n))
print("La suma es: ",fibonacci(n))