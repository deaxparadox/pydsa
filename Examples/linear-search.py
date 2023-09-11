import random 

arr = [random.randint(100, 1000) for _ in range(10)]

def linear_serach(arr):
    num = arr[6]
    i, j = 0, len(arr)

    while i < j:
        print(arr[i], num, i)
        if arr[i] == num:
            print(i)
        i+=1
        


linear_serach(arr)