import start, error, slingshot, pig, variable

if_statement_was_True = False

def if_statement():
    global if_statement_was_True
    try:
        value1 = start.full_line.split(" ", 2)[1]
    except:
        error.invalid_if_statement()
        
    operator = start.full_line.split(" ", 3)[2]
    value2 = start.full_line.split(" ", 4)[3]
    goto_function = start.full_line.split(" ", 5)[5]
    
    if variable.is_variable(value1):
        value1 = variable.get_variable_value(value1)
    if variable.is_variable(value2):
        value2 = variable.get_variable_value(value2)
    if variable.is_number(value1):
        variable.convert_to_number(value1)
    if variable.is_number(value2):
        variable.convert_to_number(value2)
    
    if operator == ">":
        if value1 > value2:
            if_statement_was_True = True
            start.coming_from_if = True
            slingshot.slingshot(goto_function)
    elif operator == "<":
        if value1 < value2:
            if_statement_was_True = True
            start.coming_from_if = True
            slingshot.slingshot(goto_function)
        else:
            if_statement_was_True = False
            
    elif operator == "==":
        if value1 == value2:
            if_statement_was_True = True
            start.coming_from_if = True
            slingshot.slingshot(goto_function)
        else:
            if_statement_was_True = False
            
    elif operator == "!=":
        if value1 != value2:
            if_statement_was_True = True
            start.coming_from_if = True
            slingshot.slingshot(goto_function)
        else:
            if_statement_was_True = False
            
    elif operator == ">=":
        if value1 >= value2:
            if_statement_was_True = True
            start.coming_from_if = True
            slingshot.slingshot(goto_function)
        else:
            if_statement_was_True = False
            
    elif operator == "<=":
        if value1 <= value2:
            if_statement_was_True = True
            start.coming_from_if = True
            slingshot.slingshot(goto_function)
        else:
            if_statement_was_True = False
            
    else:
        error.invalid_operator(operator)
