import os, sys, error, oink, variable, if_statement

# nöff    start of program
# nöf     create variable
# oink    print
# niff    if statement
# niffel  else statement
# nilf    else if statement
# nör     for loop

keywords = ["nöff", "nöf", "oink", "niff", "niffel", "nilf", "nör", "modify",
            "add", "sub", "multiply", "divide", "modulo", "power", "//", 
            "slingshot", "pig"]
variables = {}
program_name = ""
line_number = 0
full_line = ""
nöff_count = 0 # make sure there is only one nöff

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
        elif first_word == "niffel":
            pass
        elif first_word == "nilf":
            pass
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
            pass
        elif first_word == "pig":
            pass
    else:
        error.keyword_not_found(first_word)
def start(content):
    global program_name, line_number, full_line
    
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
    for line in lines:
        line_number += 1
        # if line is empty, then skip it
        if line == "": continue
        
        # detect keywords
        full_line = line
        detect_keywords()
            