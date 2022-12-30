def potencia(a,b):
    if b==1:
        return a
    else:
        if b%2 == 0:
            producto = potencia(a, int(b/a))
            return producto*producto
        else:
            return a* potencia(a, b-1)
n1 = int(input("Ingrese un valor: ")) 
n2 = int(input("Ingrese un valor: ")) 
print("La potencia es : ",potencia(n1,n2))