import time

def bf1(a,b):
    val = a
    for i in range(1,b):
        val *= a
    return val


def bf2(a,b):
    if b==0:
        return 1
    return a * bf2(a, b-1)
    

def dnc(a,b):
    if b==0:
        return 1
    return dnc(a,b/2) * dnc(a, (b+1)/2 )
    

a = 234115
b = 469

tic = time.time()
bf1(a,b)
toc = time.time()

print("Elapsed time for BF1: %.4fs" % (toc-tic))

# BF2 Attempt

tic = time.time()
bf2(a,b)
toc = time.time()

print("Elapsed time for BF2: %.4fs" % (toc-tic))

# BF2 Attempt

tic = time.time()
dnc(a,b)
toc = time.time()

print("Elapsed time for dnc: %.4fs" % (toc-tic))