import start, error, variable


def slingshot(line):
    try:
        slingshot_variable = line.split(" ")[1]
    except:
        error.invalid_slingshot()
    if slingshot_variable not in start.variables and variable.is_number(slingshot_variable):
        start.goto_number = int(slingshot_variable)
    else:
        start.last_came.append(start.line_number + 1)
        try:
            start.goto_number = start.functions[slingshot_variable][0] + 1
        except:
            error.slingshot_goto_not_found(slingshot_variable)
            