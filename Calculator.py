import math 

#define functions for the 4 operations you will use in the calculator
def add(x,y):
    return x + y
    
def subtract(x,y):
    return x - y
    
def divide(x,y):
    return x / y
    
def multiply(x,y):
    return x * y

#print welcoming line    
print("Welcome to the calculator program! ")

#create dictionary to store the operation functions with the key being their symbol as a string
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

#define a new function to decide whether the user wants to input new calculations (to be used in the calculator function)
def continue_calculating():
    #function stop_calculating used in while loop to define conditions to stop
    stop_calculating = False
    #while loop, when stop_calculating is not false:
    while not stop_calculating:
        #new variable to see if the user wants to input a new calculations
        new_equation = input("Would you like to input a new calculation? Type 'y' if yes: ").lower()
        #if yes, 'y', then print the calculation function
        if new_equation == "y":
            calculator()
                
        else:
            #else change the boolean value of stop_calculating
            stop_calculating = True
            #print a thank you message and the function will close
            print("Thank you for using this service! ")



#define the calculator function
def calculator():
    #Asks the user for the decimal figures they want the answer to be to 
    decimal_figures = int(input("To how many decimal figures do you want your answer to be rounded to? "))
    #Asks for the first number
    num1 = float(input("What is the first number?: "))

    #print each of the keys in the dictionary with for loop. 
    for operation in operations:
        print(operation)

    #store the symbol they want to use as a variable called operation_symbol
    operation_symbol = input("What operation would you like to use from above? ")
    #call the function they need from the dictionary and store as a variable called calculation_function
    calculation_function = operations[operation_symbol]

    #ask for a second number
    num2 = float(input("What is the second number?: "))

    #set a variable to be used in while loop. To define conditions to stop
    stop_calculator = False
    answer = round(calculation_function(num1,num2),decimal_figures)
    print (f"{num1} {operation_symbol} {num2} = {answer} ")

    #when not stop_calucator, keep going through loop
    while not stop_calculator:
        #new variable to ask if the user wants to continue with the current calculation
        continue_calculation = input("Type 'y' If you would like to continue with this calculations: ").lower()
        
        #if yes, allow the user to use the answer from the first calc in the next calc
        if continue_calculation == 'y':
            #ask new operation symbol
            operation_symbol = input("What operation would you like to use? ")
            #ask for a next number
            next_number = float(input("What is the next number?: "))
            #Call the new function from the operations dictionary
            calculation_function =operations[operation_symbol]
            #calculate the new answer
            new_answer = round(calculation_function(answer, next_number),decimal_figures)
            #print new equation and new answer
            print (f"{answer} {operation_symbol} {next_number} = {new_answer} ")
            #reset the answer variable to the new answer to be used if the loop continues
            answer = new_answer
        else:
            #change the variable stop_calculator to true so the loop stops
            stop_calculator = True
            
            continue_calculating()

#use the calculator function
calculator()

