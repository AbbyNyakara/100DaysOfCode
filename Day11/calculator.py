
def add(n1, n2):
    """
    Takes two numbers as inputs and returns the sum
    """
    return(n1+n2)

def multiply(n1, n2):
    """
    Takes two numbers as inputs and returns the product
    """
    return(n1*n2)

def subtract(n1, n2):
    """
    Takes two numbers and subracts the numbers
    """
    return (n1 - n2)

def divide(n1, n2):
    """
    Takes two numbers and returns the division of the two numbers
    """
    return (n1/n2)

math_operations = {
    '+': add,
    '-': subtract ,
    '/' : divide,
    '*': multiply
}

def calculate():
    """
    A calculator function for add, subtract, divide and multiply
    """
    
    num1 = int(input("Enter the first number: "))
    
    should_continue = True
    while should_continue:
        for keys, val in math_operations.items():
            print(keys)
        operation_symbol = input("Pick an operation from the options above: ")
        num2 = int(input("What is the next number?: "))
        calculation_function = math_operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")
        to_continue = input(f"Type 'y' to contine calculating with {answer} or 'n' to start a new calculation: \n")
        if to_continue == "y".lower():
            num1 = answer
        else:
            should_continue = False
            calculate()


calculate()
