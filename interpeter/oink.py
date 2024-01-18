import start
import error
import variable as vr


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
        variable = word

        if word.startswith("$") or word.startswith("§"):
            if word.startswith("§"):
                word = word.replace("§", "")
            #     print("www" + str(words))
            #     input()

            # print("w" + str(words))
            # input()

            if "§" in word:
                # if letter is § split the word at § and add the § letter to the start of the next word
                variable = word.split("§")[0]
                words[i] = variable
                words.insert(i+1, "§" + word.split("§")[1])
                word = variable
                # print("ww" + str(words))
                # input()

            if vr.is_variable(word) and not word.startswith("§"):
                variable = vr.get_variable_value(word)
            elif vr.is_number(word):
                error.variable_not_found(word)

            # replace word with variable

            words[i] = variable

        # reconnect words if next word starts with § dont add a space
        # if last
        if i != len(words) - 1:
            next_word = words[i+1]
        else:
            next_word = ""

        # print("next_word: " + str(next_word),": word i:" ,str(words[i]))
        if next_word.startswith("§"):
            converted_text += words[i]
            # print("1: " + str(converted_text))
            # input()
        else:
            if i != len(words) - 1:
                converted_text += words[i] + " "
                # print("2: " + str(converted_text))
                # input()
            else:
                # if last replace § with space
                if words[i].startswith("§"):
                    words[i] = words[i].replace("§", "")
                converted_text += words[i]
                # print("3: " + str(converted_text))
                # input()
        i += 1

    # print("wwww: " + str(converted_text))
    # input()

    # Final check for §
    if "§" in converted_text:
        converted_text = converted_text.replace("§", "")
    return converted_text
