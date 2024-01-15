import start, error, variable as vr

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
    i = 0
    while i < len(words):
        has_squigel = False
        word = words[i]
           
        if word.startswith("$") or word.startswith("§"):
            if word.startswith("§"):
                has_squigel = True
                
            if "§" in word:
                # if letter is § split the word at § and add the § letter to the start of the next word
                variable = word.split("§")[0]
                words[i] = variable
                words.insert(i+1, "§" + word.split("§")[1])
                word = variable
            
            if vr.is_variable(word):
                variable = vr.get_variable_value(word)
            else:
                error.variable_not_found(word)

            # replace word with variable
            if i == len(words) - 1:
                words[i] = variable
            else:
                words[i] = variable[:-1]

        i += 1

    # reconstruct the text with modified words
    text = " ".join(words)

           

    return text