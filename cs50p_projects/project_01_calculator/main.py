def main():
    while True:
        run = input("Start Calculator? (y/n)")
        if run not in ["y", "Y", "n", "N"]:
            print("Please enter a valid key.")
        else:
            break
    while run == "y" or run =="Y":
        
        # Get valid number 1
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        # Get valid operator
        while True:
            op = input("Enter the operator: ")
            if op not in ["+", "-", "*", "/"]:
                print ("Please enter a valid operator.")
            else:
                break
          
        # Get valid number 2
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        # Compute and print result
        if op == "+":
            ans = num1 + num2
            print(f"The answer is {ans}.")
        elif op == "-":
            ans = num1 - num2
            print(f"The answer is {ans}.")
        elif op == "*":
            ans = num1 * num2
            print(f"The answer is {ans}.")
        elif op == "/":
            if num2 != 0:
                ans = num1 / num2
                print(f"The answer is {ans}.")
            else:
                print("You can't divide by zero.")

        # Ask "another calculation? (y/n)"
        while True:
            run = input("Restart calculator? (y/n)")
            if run not in ["y", "Y", "n", "N"]:
                print("Please enter a valid key.")
            else:
                break

main()