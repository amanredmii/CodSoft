print("\n---------Calculator---------")

def calculation(num1, num2, opr):
    match opr:
        case '+':
            print("\nPc : The sum of", num1, "and", num2, "is", num1 + num2)

        case '-':
            print("\nPc : The difference of", num1, "and", num2, "is", num1 - num2)

        case '*':
            print("\nPc : The product of", num1, "and", num2, "is", num1 * num2)

        case '/':
            try:
                result = num1 / num2
                print("\nPc : The division of", num1, "and", num2, "is", result)
            except ZeroDivisionError:
                print("\nPc : Division by zero is not allowed, please enter a valid denominator..!!")
                
        case _:
            print("\nPc : Enter a valid operation..!!")

try:
    num1 = float(input("\nPc : Enter the first number..!!\nUser : "))
    opr = input("\nPc : Enter the operation..!!\nUser : ")
    num2 = float(input("\nPc : Enter the second number..!!\nUser : "))
    calculation(num1, num2, opr)

except ValueError:
    print("\nPc : Invalid input, please enter numeric values..!!")