import os, sys, error, oink, variable

# nöff    start of program
# nöf     create variable
# oink    print
# niff    if statement
# niffel  else statement
# nilf    else if statement
# nör     for loop

keywords = ["nöff", "nöf", "oink", "niff", "niffel", "nilf", "nör", "modify",
            "add", "sub", "multiply", "divide", "modulo", "power"]
variables = {}
program_name = ""
line_number = 0
nöff_count = 0 # make sure there is only one nöff

def detect_keywords(line):
    global nöff_count
    # detect keywords
    first_word = line.split(" ")[0]
    if first_word in keywords:
        if first_word == "nöff":
            if nöff_count == 1:
                error.too_much_nöff()
            else:
                nöff_count += 1
        elif first_word == "nöf":
            variable.create(line)
        elif first_word == "oink":
            oink.say(line)
        elif first_word == "niff":
            pass
        elif first_word == "niffel":
            pass
        elif first_word == "nilf":
            pass
        elif first_word == "nör":
            pass
        elif first_word == "modify":
            variable.modify(line)
        elif first_word == "add":
            variable.do_operator(line, "add")
        elif first_word == "sub":
            variable.do_operator(line, "subtract")
        elif first_word == "multiply":
            variable.do_operator(line, "multiply")
        elif first_word == "divide":
            variable.do_operator(line, "divide")
        elif first_word == "modulo":
            variable.do_operator(line, "modulo")
        elif first_word == "power":
            variable.do_operator(line, "power")    
    else:
        error.keyword_not_found(first_word, line)
def start(content):
    global program_name
    global line_number
    
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
        detect_keywords(line)
            