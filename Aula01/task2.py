def R1(n):
    if (n==0):
        return 0
    return 1 + R1(n-1)

def R2(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    return n + R2(n-2)

def R3(n):
    if (n==0):
        return 0
    return 1 + 2 * R3(n-1)

def R4(n):
    if (n==0):
        return 0
    return 1 + R4(n-1) + R4(n-1)

"""
print("R1: " , format(R1(3)))
print("R2: " , format(R2(3)))
print("R4: " , format(R4(3)))
"""
for i in range(1,5):
    print("R3(%d): %d" % (i,R3(i)))
