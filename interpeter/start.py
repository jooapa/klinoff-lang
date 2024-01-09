import os, sys, error, oink, variable

# nöff    start of program
# nöf     create variable
# oink    print
# niff    if statement
# niffel  else statement
# nilf    else if statement
# nör     for loop

keywords = ["nöff", "nöf", "oink", "niff", "niffel", "nilf", "nör"]
variables = {}
program_name = ""

def detect_keywords(line):
    
    # detect keywords
    first_word = line.split(" ")[0]
    if first_word in keywords:
        if first_word == "nöff":
           pass
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
       
    else:
        error.keyword_not_found(first_word)
def start(content):
    global program_name
    
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
        # if line is empty, then skip it
        if line == "": continue
        
        # detect keywords
        detect_keywords(line)
            