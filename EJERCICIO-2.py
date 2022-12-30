import random
def desordena(a, n, i):
    if i<n:
        ra = random.randint(i, n-1)
        a[i],a[ra]= a[ra],a[i]
        desordena(a,len(a),i+1)
lista = [1,2,3,5,7,11,13,17,19]
desordena(lista,len(lista),0)
print(lista)