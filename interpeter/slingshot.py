import start


def slingshot(line):
    slingshot_variable = line.split(" ", 1)[1]
    start.last_came.append(start.line_number + 1)
    start.goto_number = start.functions[slingshot_variable][0] + 1
        