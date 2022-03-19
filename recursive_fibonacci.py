def rfibo(n):
    l = [0,1]
    if n ==1:
        return 0
    elif n == 2:
        return 1
    else:
        return rfibo(n-1) + rfibo(n-2)
        
print(rfibo(5))
