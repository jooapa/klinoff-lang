import sys, os, start, error

def create():
    
    variable_name = start.full_line.split(" ")[1]
    # value is the rest of the line
    try:
        variable_value = start.full_line.split(" ", 3)[3]
    except:
        error.no_variable_value()
    start.variables[variable_name] = variable_value
    
def modify(line):
    variable_name = line.split(" ")[1]
    # value is the rest of the line
    try:
        variable_value = line.split(" ", 2)[2]
    except:
        error.no_variable_name()
    if is_variable(variable_value):
        variable_value = get_variable_value(variable_value)
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
        float(number)
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

               
def convert_to_number(number):
    try:
        number = float(number)
        return number
    except:
        start.error.invalid_number(number)

def do_operator(operator):
    try:
        value1 = start.full_line.split(" ")[1]
        variable = value1
        value2 = start.full_line.split(" ")[2]
    except:
        error.no_variable_name()
        
    # check if value1 is a variable
    if is_variable(value1):
        value1 = get_variable_value(value1)
    # check if value1 is a number
    if is_variable(value2):
        value2 = get_variable_value(value2)
    # convert value1 and value2 to int
    
    if is_number(value1):
        value1 = convert_to_number(value1)
    else:
        start.error.not_number(value1)
    if is_number(value2):
        value2 = convert_to_number(value2)
    else:
        start.error.not_number(value2)
        
    if operator == "add":
        result = float(value1) + float(value2)
    elif operator == "subtract":
        result = float(value1) - float(value2)
    elif operator == "multiply":
        result = float(value1) * float(value2)
    elif operator == "divide":
        if float(value2) == 0:
            start.error.devision_by_zero()
        result = float(value1) / float(value2)
    elif operator == "modulo":
        result = float(value1) % float(value2)
    elif operator == "power":
        result = float(value1) ** float(value2)

    modify("modify " + str(variable) + " " + str(result))
    