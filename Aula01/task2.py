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

n = 12

print("Return of R1 correct? " , format( R1(n)==n ))
print("Return of R2 correct? " , format( R2(n)==sum(i if n % 2 == 0 else i+1 for i in range(0,n+1,2)) ))
print("Return of R3 correct? " , format( R3(n)==(2**n -1) ))
print("Return of R4 correct? " , format( R4(n)==(2**n -1) ))

"""
for i in range(1,10):
    print("R3(%d): %d" % (i,R3(i)))
    Retorno final: 2^n - 1

# Ajuda para resolver a formula matematica, basicamente fazemos uma lista comprehension
# para criar uma lista ou de impares ou de pares e depois fazemos o sum dessa lista

return_val = R2(n)
expected = sum(i if n % 2 == 0 else i+1 for i in range(0,n+1,2))

print(return_val)
print(expected)
"""
