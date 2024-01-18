import sys, os, start, textwrap
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
    if file_extension == ".kln":
        pass   
    else:
        invalid_extension()
        return
    
    # absolute path
    klinoff_file = get_absolute_path(args[0])
    klinoff_content = get_contents(klinoff_file)
    
    # remove indentations
    no_indent_klinoff_content = ""
    for line in klinoff_content.split("\n"):
        no_indent_klinoff_content += textwrap.dedent(line) + "\n"
    
    #  remove last \n
    no_indent_klinoff_content = no_indent_klinoff_content[:-1]
    
    no_comment_klinoff_content = ""
    for line in no_indent_klinoff_content.split("\n"):
        if "//" in line:
            no_comment_klinoff_content += line.split("//")[0] + "\n"
        else:
            no_comment_klinoff_content += line + "\n"
            
    # remove last \n
    no_comment_klinoff_content = no_comment_klinoff_content[:-1]
    
    for arg in args:
        if arg == "--debug" or arg == "-d":
            start.Debug_mode = True
    
    # Cross-platform SUpport for the one and only klinoff-lang
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
    start.start(no_comment_klinoff_content)
    
if __name__ == "__main__":
    interpret(sys.argv[1::])