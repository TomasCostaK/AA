import time

def fibbo_dp(end_point):
    fibbo_array = [0,1]
    i = 2
    while i <= end_point:
        res = fibbo_array[i-2]+ fibbo_array[i-1]
        print("Fibbo for n=%d -> %d" % (i,res))
        fibbo_array.append(res)
        i+=1

    return fibbo_array[end_point-1]

def fibbo_3vars(end_point):
    var1 = 0
    var2 = 1
    i = 2
    while i <= end_point:
        var3 = var1 + var2
        print("Fibbo for n=%d -> %d" % (i,var3))

        #change vars
        var1 = var2
        var2 = var3
        i+=1

    return var3

def fibbo(end_point):
    if end_point == 0:
        return 0
    if end_point == 1:
        return 1

    val = fibbo(end_point-2) + fibbo(end_point-1)
    return val

if __name__ == "__main__":
    n = 500

    #res = fibbo(n)
    #print("Fibbo for n=%d -> %d" % (n,res))

    tic = time.time()
    res = fibbo_dp(n)
    toc = time.time()
    print("Finished in %.4f seconds" % (toc-tic))