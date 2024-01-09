import start



def invalid_extension():
    print("Error: Invalid file extension")
    exit()
    
def invalid_file():
    print("Error: Invalid klinoff file")
    print("Klinoff files must start with \"nöff\"")
    exit()
    
def keyword_not_found(keyword, line):
    print("Error: Keyword \"" + keyword + "\" not found")
    print(str(start.line_number) + "| "+ line)
    exit()
    
def variable_not_found(variable):
    print("Error: Variable \"" + variable + "\" not found or defined")
    exit()
    
def too_much_nöff():
    print("Error: Too much nöff at:" + str(start.line_number))
    exit()
    
def invalid_number(number):
    print("Error: Invalid number \"" + number + "\"")
    print("Line: " + str(start.line_number))
    exit()