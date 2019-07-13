def evens():
    input_string = input("Enter a list element separated by space ")
    list  = input_string.split()
    
    print("Find the even numbers in the list")
    for a in list:
        even = a
        if(even % 2 == 0):
            print(even)
   
        
    print("Calculating sum of element of input list")
    sum = 0
    for num in list:
        sum += int (num)
    print("Sum is = ",sum)
print(evens())
    
