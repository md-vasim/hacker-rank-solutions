arr = [1,2,3,4,3,2,1] 

def lonelyint(arr): 
    ndict = dict()
    for num in arr:
        if num in ndict:
            ndict[num] += 1
        else:
            ndict[num] = 1 

    odict = {num: arr.count(num) for num in arr}
    
    unique = [num for num in arr if arr.count(num) == 1]
    
    return unique[0]


print(lonelyint(arr))