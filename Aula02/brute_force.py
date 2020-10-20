import time

def bf1(a,b):

    assert(type(b) == int) and (b>=0), "Wrong exponent!"
    assert(a != 0 or b != 0), "Cannot compute 0**0"

    val = 1
    for i in range(1,b+1):
        val *= a
    return val


def bf2(a,b):

    assert(type(b) == int) and (b>=0), "Wrong exponent!"
    assert(a != 0 or b != 0), "Cannot compute 0**0"

    if b==0:
        return 1
    return a * bf2(a, b-1)
    

def div_n_conq(a,b):

    assert(type(b) == int) and (b>=0), "Wrong exponent!"
    assert(a != 0 or b != 0), "Cannot compute 0**0"

    if b==0:
        return 1
    if b==1:
        return a
    return div_n_conq(a,b//2) * div_n_conq(a, (b+1)//2 )

def dec_n_conq(a,b):

    assert(type(b) == int) and (b>=0), "Wrong exponent!"
    assert(a != 0 or b != 0), "Cannot compute 0**0"
    
    if b==0:
        return 1

    sol = dec_n_conq(a, b//2)
    
    if sol%2:
        return sol * sol;

    return a * sol * sol
    

a = 234115
b = 469

tic = time.time()
bf1(a,b)
toc = time.time()

print("Elapsed time for BF1: %.6fs" % (toc-tic))

# BF2 Attempt

tic = time.time()
bf2(a,b)
toc = time.time()

print("Elapsed time for BF2: %.6fs" % (toc-tic))

# BF2 Attempt

tic = time.time()
div_n_conq(a,b)
toc = time.time()

print("Elapsed time for div_n_conq: %.6fs" % (toc-tic))

#Dec_n_conquer

tic = time.time()
dec_n_conq(a,b)
toc = time.time()

print("Elapsed time for dec_n_conq: %.6fs" % (toc-tic))