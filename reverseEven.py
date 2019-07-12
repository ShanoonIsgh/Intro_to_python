def reverseEven():
    fNumb = int(input('Enter first number: '))
    sNumb = int(input('Enter second number: '))
    
    while(fNumb < sNumb):
        sNumb -= 1

        if (sNumb % 2 ==0):
            print(sNumb)
print(reverseEven())

        
