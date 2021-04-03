import os

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

def op(symbol:str):
    match symbol:
        case "+":
            return add
        case "-":
            return subtract
        case "*":
            return multiply
        case "/":
            return divide

def main():
    os.system("clear")
    again = True
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    while again:
        operator = input("+\n-\n*\n/\nPick an operation from the line above: ")
        selected_operation = op(operator)
        result = selected_operation(num1,num2)
        print(f"{num1} {operator} {num2} = {result}")
        cont = input(f"Do you want to continue with {result}? if so please write 'yes' otherwise 'no' \n")
        if cont == "no":
            again = False
        else:
            num1 = result
            num2 = int(input("What is the next number? "))
main()