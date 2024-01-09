import sys, os
import error, oink, variable, if_statement, slingshot, pig
# nöff    start of program
# nöf     create variable
# oink    print
# niff    if statement
# niffel  else statement
# nilf    else if statement
# nör     for loop

full_code = ""
keywords = ["nöff", "nöf", "oink", "niff", "nilf", "nör", "modify",
            "add", "sub", "multiply", "divide", "modulo", "power", "//", 
            "slingshot", "pig", "gip", "når", "nöffnöff"]
variables = {}
functions = {
    # "function_name": [start_line, end_line]
}

program_name = "" 
line_number = 0 # current line number
goto_number = -1 # if this is not -1, then start reading from this line
full_line = "" # current line in text
nöff_count = 0 # make sure there is only one nöff
coming_from_if = False
last_came = []

def find_words_line(text, word):
    lines = text.split("\n")
    line_number = 0
    for line in lines:
        line_number += 1
        if line.startswith(word):
            break
    return line_number

def return_line_text(line_number):
    lines = full_code.split("\n")
    return lines[line_number-1]

def setup_functions(lines):
    # add every function to the functions dictionary with the line number
    # for the start and end of the function, function starts with pig and ends with gip
    global functions
    line_number = 0
    last_function_name = None
    for line in lines:
        line_number += 1
        if line.startswith("pig ") and len(line.split()) > 1:
            function_name = line.split(" ", 1)[1]
            functions[function_name] = [line_number, 0]
            last_function_name = function_name
        elif line.startswith("gip"):
            if last_function_name is not None:
                functions[last_function_name][1] = line_number
                last_function_name = None
                
    
def detect_keywords():
    global nöff_count, full_line
    # detect keywords
    first_word = full_line.split(" ")[0]
    if first_word in keywords:
        if first_word == "nöff":
            if nöff_count == 1:
                error.too_much_nöff()
            else:
                nöff_count += 1
        elif first_word == "nöf":
            variable.create()
        elif first_word == "oink":
            oink.say()
        elif first_word == "niff":
            if_statement.if_statement()
        elif first_word == "nilf":
            if_statement.if_statement()
        elif first_word == "nör":
            pass
        elif first_word == "når":
            pass
        elif first_word == "modify":
            variable.modify()
        elif first_word == "add":
            variable.do_operator("add")
        elif first_word == "sub":
            variable.do_operator("subtract")
        elif first_word == "multiply":
            variable.do_operator("multiply")
        elif first_word == "divide":
            variable.do_operator("divide")
        elif first_word == "modulo":
            variable.do_operator("modulo")
        elif first_word == "power":
            variable.do_operator("power")
        elif first_word == "//":
            pass
        elif first_word == "":
            if full_line != "":
                print("fsdfddffdfdfsdfd")
        elif first_word == "slingshot":
            slingshot.slingshot(full_line)
        elif first_word == "pig":
            pig.pig()
        elif first_word == "gip":
            pig.gip()
        elif first_word == "nöffnöff":
            pass
    else:
        error.keyword_not_found(first_word)
        
def start(content):
    global program_name, line_number, full_line, full_code, goto_number
    full_code = content
    
    # if content is empty, then skip it
    if content == "":
        error.invalid_file()
        
    # if first line does not start with "nöff", then it is not a valid klinoff file
    if content.split("\n")[0].startswith("nöff") == False:
        error.invalid_file()
    else:
        program_name = content.split("\n")[0].replace("nöff ", "")
        print("Program name: " + program_name)
        
    # read every line
    lines = content.split("\n")
    
    setup_functions(lines)
    i = 1
    while i <= len(lines):
        # if goto_number is not -1, start reading from goto_number down
        if goto_number != -1:
            i = goto_number
            goto_number = -1
            continue
        
        full_line = lines[i-1]
        line_number = i
        
        input()
        print(str(line_number) + "| " + full_line, end="")
        
        # if line is empty, then skip it
        if full_line == "":
            i += 1
            continue
        
        # detect keywords
        detect_keywords()
        
        i += 1
            