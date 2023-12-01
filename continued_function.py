def continued_fractions(a,b):
    #a < b
    arr = []
    arr1 = [0]
    a_phay = 0
    while(a_phay != 1):
        n = b//a
        a_phay = b%a
        b_phay = a 
        tup = [1,n]
        a = a_phay
        b = b_phay
        arr.append(tup)
        if (len(arr) == 1):
            arr1.append(tup)
        else:
            x = arr[len(arr)-1][1]
            y = 1
            for i in range(len(arr)-2,-1,-1):
                t = x 
                x = x * arr[i][1]
                x += y
                y = t
            arr1.append([y,x])        
    n = b//a
    tup = [1,n]
    arr.append(tup)
    x = arr[len(arr)-1][1]
    y = 1
    for i in range(len(arr)-2,-1,-1):
        t = x 
        x = x * arr[i][1]
        x += y
        y = t 
    arr1.append([y,x])
    return arr1
print(continued_fractions(17993,90581))
        
        
        
        
        
