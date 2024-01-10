import sys, os, start
from error import invalid_extension


def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def get_absolute_path(file_path):
    return os.path.abspath(file_path)

def get_contents(file_path):
    file = open(file_path, "r", encoding="utf-8")
    contents = file.read()
    file.close()
    return contents

def interpret(args):
    # file extension
    file_extension = get_file_extension(args[0])
    if file_extension == ".kln" or file_extension == ".klinoff" or file_extension == ".nöff" or file_extension == ".sh":
        pass   
    else:
        invalid_extension()
        return
    
    # absolute path
    klinoff_file = get_absolute_path(args[0])
    klinoff_content = get_contents(klinoff_file)
    
    for arg in args:
        if arg == "--debug" or arg == "-d":
            start.Debug_mode = True
            
    os.system("cls")
    start.start(klinoff_content)
    
if __name__ == "__main__":
    interpret(sys.argv[1::])