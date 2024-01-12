import start, error, variable


def start_loop():
    loop_name = get_loop_name_from_start_for_loops(start.line_number)
    try:
        only_loop_name = loop_name.split(" ", 2)[0]
    except:
        error.invalid_for_loop()
        
    loop_number = loop_name.split(" ", 2)[1]
    if loop_number != "infinite":
        if variable.is_variable(loop_number):
            loop_number = variable.get_variable_value(loop_number)
        loop_number = int(loop_number)
        
        loop_number -= 1
        change_loop_name(start.for_loops, start.line_number, 
                        only_loop_name + " " + str(loop_number))     
    
def end_loop():
    # get the start line number by the giving the end line number
    try:
        start_line, loop_name = get_start_line(start.for_loops, 
                                            start.line_number)
        loop_number = loop_name.split(" ", 2)[1]
    except:
        error.invalid_for_loop()
    
    if loop_number != "infinite":
        if variable.is_variable(loop_number):
            loop_number = variable.get_variable_value(loop_number)
        loop_number = int(loop_number)
        
        if int(loop_number) <= 0:
            pass
        else:
            start.goto_number = start_line
    else:
        start.goto_number = start_line

def get_start_line(loops, end_line):
    for loop_name, (start_line, loop_end_line) in loops.items():
        if loop_end_line == end_line:
            return start_line, loop_name
    return None

def change_loop_name(loops, start_line, new_name):
    for loop_name, (loop_start_line, end_line) in list(loops.items()):
        if loop_start_line == start_line:
            loops[new_name] = loops.pop(loop_name)
            return
    error.loop_not_found(start_line)
    
def get_loop_name_from_start_for_loops(start_line):
    for loop_name, (loop_start_line, end_line) in start.for_loops.items():
        if loop_start_line == start_line:
            return loop_name
    return None

def get_loop_name_from_current_line(loops, current_line):
    for loop_name, (loop_start_line, end_line) in loops.items():
        if loop_start_line <= current_line <= end_line:
            return loop_name
    return None

def change_loop_name_from_name(loops, loop_name, new_name):
    for loop, (loop_start_line, end_line) in loops.items():
        if loop == loop_name:
            loops[new_name] = loops.pop(loop)
            return
    error.loop_not_found(loop_name)
    
def pop_loop():
    loop_name = get_loop_name_from_current_line(start.for_loops, start.line_number)
    only_loop_name = loop_name.split(" ", 2)[0]
    change_loop_name_from_name(start.for_loops, loop_name, only_loop_name + " 0")
