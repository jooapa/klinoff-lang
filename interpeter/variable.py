import sys, os, start

def create(line):
    variable_name = line.split(" ")[1]
    # value is the rest of the line
    variable_value = line.split(" ", 3)[3]
    start.variables[variable_name] = variable_value
    
def modify(line):
    variable_name = line.split(" ")[1]
    # value is the rest of the line
    variable_value = line.split(" ", 2)[2]
    # remove $ from variable name
    variable_name = variable_name.replace("$", "")
    start.variables[variable_name] = variable_value
    
    
def is_variable(variable):
    if variable.startswith("$"):
        return True
    else:
        return False

def is_number(number):
    try:
        number = int(number)
        return True
    except:
        return False
     
def get_variable_value(variable):
    variable = variable.replace("$", "")
    if variable in start.variables:
        variable = start.variables[variable]
        return variable
    else:
        start.error.variable_not_found(variable)

               
def convert_to_int(number):
    try:
        number = int(number)
        return number
    except:
        start.error.invalid_number(number)

def do_operator(line, operator):
    value1 = line.split(" ")[1]
    variable = value1
    value2 = line.split(" ")[2]
        
    # check if value1 is a variable
    if is_variable(value1):
        value1 = get_variable_value(value1)
    # check if value1 is a number
    if is_variable(value2):
        value2 = get_variable_value(value2)
    # convert value1 and value2 to int
    
        
    if operator == "add":
        result = int(value1) + int(value2)
    elif operator == "subtract":
        result = int(value1) - int(value2)
    elif operator == "multiply":
        result = int(value1) * int(value2)
    elif operator == "divide":
        result = int(value1) / int(value2)
    elif operator == "modulo":
        result = int(value1) % int(value2)
    elif operator == "power":
        result = int(value1) ** int(value2)
    modify("modify " + str(variable) + " " + str(result))
    
