def pasosRobot(n):
    if n==1 or n==2:
        return n
    elif n == 3:
        return n+1
    return pasosRobot(n-1)+ pasosRobot(n-2)+pasosRobot(n-3)
paso = int(input("Ingrese cuantos pasos el robot avanzara: "))
for i in range(1, paso+1):
    print(pasosRobot(i))