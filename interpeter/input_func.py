import start, error, variable, oink


def input_func():
    variable_name = start.full_line.split(" ")[1]
    input_question = start.full_line.split(" ", 2)[2]
    if input_question.startswith("\"") == False or input_question.endswith("\"") == False:
        error.no_quotes_in_input()
    # remove quotes
    input_question = input_question[1:-1]
    input_question_with_variable = oink.say_quotes(input_question)
    variable_value = input(input_question_with_variable)
    variable.modify("modify " + variable_name + " " + variable_value)
