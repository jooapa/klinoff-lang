import start, error

def say(text):
    has_squigel = False
    # remove the first word
    text = text.split(" ", 1)[1]
        
    # check if text is a variable
    if text.startswith("$"):
        text = text.replace("$", "")
        if text in start.variables:
            text = start.variables[text]
        else:
            error.variable_not_found(text)

    # if text is a string, then remove the quotes
    elif text.startswith("\"") and text.endswith("\""):
        text = text.replace("\"", "")
    
    # split text into words and check if they are variables

    words = text.split(" ")
    for word in words:
        if word.startswith("$"):
            if "§" in word:
                has_squigel = True
                word = word.split("§")[0]
                word = word.replace("§", " ")
            word = word.replace("$", "")
            if word in start.variables:
                variable = start.variables[word]
            else:
                error.variable_not_found(word)
            
            # replace word with variable
            text = text.replace("$" + word, variable)
    
    text = text.replace("§", "")
    print(text)