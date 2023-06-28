def findSmallest(arr, n): 
    res = 1

    for i in range (n): 
        if arr[i]<res:
            res =res + arr[1]
        else:
            break
        return res 
    List=[1, 1, 1, 1]
    n1= len(List)
    print(findSmallest(List, n1))