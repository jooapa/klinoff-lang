import start


def line_error():
    print(str(start.line_number) + "| " + start.full_line)

def invalid_extension():
    print("Error: Invalid file extension")
    exit()
    
def invalid_file():
    print("Error: Invalid klinoff file")
    print("Klinoff files must start with \"nöff\"")
    exit()
    
def keyword_not_found(keyword):
    print("Error: Keyword \"" + keyword + "\" not found")
    line_error()
    exit()
    
def variable_not_found(variable):
    print("Error: Variable \"" + variable + "\" not found or defined")
    line_error()
    exit()
    
def too_much_nöff():
    print("Error: Too much nöff")
    print("There can only be one nöff never ever one more or less")
    line_error()
    exit()
    
def invalid_number(number):
    print("Error: Invalid number \"" + number + "\"")
    line_error()
    exit()
    
def devision_by_zero():
    print("Error: Devision by zero")
    line_error()
    exit()
    
def function_not_found(function):
    print("Error: Function \"" + function + "\" not found")
    line_error()
    exit()
    
def operator_not_found(operator):
    print("Error: Operator \"" + operator + "\" not found")
    line_error()
    exit()
    
def last_line_not_empty():
    print("EcmaScript Error: Last line must be empty")
    exit()
    
def not_number(value):
    print("Error: \"" + value + "\" is not a number")
    line_error()
    exit()
    
def invalid_for_loop():
    print("Error: Invalid for loop")
    line_error()
    exit()
    
def loop_not_found(loop):
    print("Error: Loop \"" + loop + "\" not found")
    line_error()
    exit()
    
def no_variable_value():
    print("Error: No variable value")
    line_error()
    exit()
    
def invalid_if_statement():
    print("Error: Invalid if statement")
    line_error()
    exit()
    
def no_variable_name():
    print("Error: No variable name")
    line_error()
    exit()
    
def invalid_slingshot():
    print("Error: Invalid slingshot")
    line_error()
    exit()
    
def invalid_pig():
    print("Error: Invalid pig")
    line_error()
    exit()
    
def nothing_to_gip():
    print("Error: Nothing to gip")
    line_error()
    exit()
    
def no_quotes_in_input():
    print("Error: No quotes in input")
    line_error()
    exit()
    
def slingshot_goto_not_found(slingshot):
    print("Error: Slingshot goto \"" + slingshot + "\" not found")
    line_error()
    exit()
    
def invalid_operator(operator):
    print("Error: Invalid operator \"" + operator + "\"")
    line_error()
    exit()