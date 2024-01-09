import sys, os, start

def create(line):
    variable_name = line.split(" ")[1]
    # value is the rest of the line
    variable_value = line.split(" ", 2)[2]
    start.variables[variable_name] = variable_value