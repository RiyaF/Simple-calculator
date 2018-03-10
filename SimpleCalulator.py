
while True:
    print("Your options are : Add, Substract, Divide, Multiply or Enter quit to end the program")
    user_input = input("Options:")
    
    if user_input == "quit":
        break
    
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is: " + result)
        
    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is: " + result)
        
    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is: " + result)
        
    elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        if num2 == 0:
            print("Cannot divide by 0")
            continue
        result = str(num1 / num2)
        print("The answer is: " + result)
        
    else:
        print("Your options are : Add, Substract, Divide, Multiply or Enter quit to end the program")
        