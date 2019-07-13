def evenNumb():
    mini = int(input('Enter your minimum value: '))
    maxi= int(input('Enter your maximum number: '))

    for num in range(mini, maxi+1):
        if(num % 2 == 0):
            print(num)
print(evenNumb())
            
