num1 = float(input("Enter first number:- "))
op = input("Enter operatin:- ")
num2 = float(input("Enter second number:- "))

def Calculater():

    if op == "+":
        print("Addition:- " + str(num1 + num2))
    elif op == "-":
        print("Subtraction:- " + str(num1 - num2))
    elif op == "*":
            print("Multiplication:- " + str(num1 * num2))
    elif op == "/":
            print("Division:- " + str(num1 / num2))
    else:
        print("Invalid operation.")

Calculater()