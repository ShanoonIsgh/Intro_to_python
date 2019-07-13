def evens():
    list = [1,2,3,4,5,6,7,8,9]
    
    sum = 0
    for a in list:
        if a % 2 == 0 and a > 0:
           print(' the even numbers are : ' + str(a))
        a += a
    print(' the is sum is:' + str(a))

print(evens())            
            
