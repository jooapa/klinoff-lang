import start, error, slingshot, pig

if_statement_was_True = False

def if_statement():
    global if_statement_was_True
    
    value1 = start.full_line.split(" ", 2)[1]
    operator = start.full_line.split(" ", 3)[2]
    value2 = start.full_line.split(" ", 4)[3]
    goto_function = start.full_line.split(" ", 5)[5]
    
    if value1.startswith("$"):
        value1 = value1.replace("$", "")
        if value1 in start.variables:
            value1 = start.variables[value1]
        else:
            error.variable_not_found(value1)
            
    if value2.startswith("$"):
        value2 = value2.replace("$", "")
        if value2 in start.variables:
            value2 = start.variables[value2]
        else:
            error.variable_not_found(value2)
            
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
