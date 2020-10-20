def sequential(array):
    count = 0
    res = 0
    for i in array:
        if i % 2:
            return 
        count +=1
    
    return res, count

if __name__ == "__main__":
    lista = [1,3,5,7,8]

    result, count = sequential(lista)