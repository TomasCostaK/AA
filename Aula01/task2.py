def func1(n):
    if (n==0):
        return 0
    return 1 + func1(n-1)

def func2(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    return n + func2(n-2)

def func3(n):
    if (n==0):
        return 0
    return 1 + 2 * func3(n-1)

def func4(n):
    if (n==0):
        return 0
    return 1 + func4(n-1) * func4(n-1)

print("Func1: " , format(func1(3)))
print("Func2: " , format(func2(3)))
print("Func3: " , format(func3(3)))
print("Func4: " , format(func4(3)))