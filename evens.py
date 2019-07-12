def evens():
    numb1 = int(input('Enter your first number: '))
    numb2 = int(input('Enter  your second number: '))

    while(numb1 < numb2):
        numb1 += 1

        if numb1 % 2 == 0:
            print(numb1)
print(evens())
