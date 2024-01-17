import start, error, variable as vr, re

def say():
    if start.full_line == "oink":
        print("")
        return
    # remove the first word
    text = start.full_line.split(" ", 1)[1]
    
    text = say_quotes(text)
    print(text)
    
def say_quotes(text):
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
    converted_text = ""
    i = 0
    while i < len(words):
        word = words[i]
           
        if word.startswith("$") or word.startswith("§"):
            if word.startswith("§"):
                word = word.replace("§", "")
            
            if vr.is_variable(word) and not word.startswith("§"):
                variable = vr.get_variable_value(word)
            elif not word.startswith("§"):
                error.variable_not_found(word)

            # replace word with variable
            words[i] = variable
                
        # reconnect words if next word starts with § dont add a space
        # if last
        if i != len(words) - 1:
            next_word = words[i+1]
            
        if next_word.startswith("§"):
            converted_text += words[i]
        else:
            if i != len(words) - 1:
                converted_text += words[i] + " "
            else:
                converted_text += words[i]            
        i += 1
        
    return converted_text
