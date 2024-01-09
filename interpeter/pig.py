import start, error, if_statement


def pig():
    function_variable = start.full_line.split(" ", 1)[1]
    start_line, end_line = start.functions[function_variable]
    start.goto_number = end_line + 1
    
    

def gip():
       
    lines = start.full_code.split("\n")

    start.goto_number = start.last_came[-1]
    # print(if_statement.if_statement_was_True)
    if if_statement.start.coming_from_if and if_statement.if_statement_was_True:
        if_statement.start.coming_from_if = False
        if_statement.if_statement_was_True = False
        
        while True:
            # goto next line as long as it is not an line with "nilf"
            start.goto_number += 1
            if not lines[start.goto_number - 1].startswith("niff"):
                break
    
    
    # print(start.goto_number)