def func1(n):
    r = 0
    cont = 0
    for i in range(n+1):
        r += i
        cont += 1
    return r,cont

def func2(n):
    r = 0
    cont = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            r += 1
            cont += 1
    return r,cont

def func3(n):
    r = 0
    cont = 0
    for i in range(1,n+1):
        for j in range(i,n+1):
            r += 1
            cont += 1
    return r,cont

def func4(n):
    r = 0
    cont = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            r += j
            cont += 1
    return r,cont

print("Func1: " , format(func1(3)))
print("Func2: " , format(func2(3)))
print("Func3: " , format(func3(3)))
print("Func4: " , format(func4(3)))