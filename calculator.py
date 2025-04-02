while True:
    print ("Select operation....")
    print ("1. Sum")
    print ("2. Difference")
    print ("3. Product")
    print ("4. Quotient")
    print ("5. Exit")

    selection = input("Enter option, 1/2/3/4/5: ")

    if selection == '5':
        print("GOODBYE")
        break

    if selection in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    
        if selection == '1':
            result = num1 + num2
            print("Result: ", result)
        elif selection == '2':
            result = num1 - num2
            print("Result", result)
        elif selection == '3':
            result = num1 * num2
            print("Result", result)
        elif selection == '4':
            if num2 == 0:
                print("Error, Zero Division")
            else:
                result = num1 / num2
                print("Result", result)

        else:
            print("Invalid Option")

    


