import time

def robot_dp(end_point):
    robot_array = [1,2,4]
    i = 3
    while i <= end_point:
        res = robot_array[i-2]+ robot_array[i-1] + robot_array[i-3]
        print("robot for n=%d -> %d, ratio_increase: %.3f" % (i,res))
        robot_array.append(res)
        i+=1

    return robot_array[end_point-1]

def robot(end_point):

    if end_point == 1:
        return 1
    if end_point == 2:
        return 2
    if end_point == 3:
        return 4

    val = robot(end_point-3) + robot(end_point-2) + robot(end_point-1)
    return val

if __name__ == "__main__":
    n = 20

    #res = robot(n)
    #print("robot for n=%d -> %d" % (n,res))

    tic = time.time()
    res = robot(n)
    toc = time.time()
    print("Finished in %.4f seconds. ANS: %d" % (toc-tic, res))

    res = robot_dp(n)
