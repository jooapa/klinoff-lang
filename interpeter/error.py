def invalid_extension():
    print("Error: Invalid file extension")
    exit()
    
def invalid_file():
    print("Error: Invalid klinoff file")
    print("Klinoff files must start with \"nöff\"")
    exit()
    
def keyword_not_found(keyword):
    print("Error: Keyword \"" + keyword + "\" not found")
    exit()
    
def variable_not_found(variable):
    print("Error: Variable \"" + variable + "\" not found")
    exit()