import sys, os


def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def get_absolute_path(file_path):
    return os.path.abspath(file_path)

def interpret(args):
    # file extension
    file_extension = get_file_extension(args[0])
    if file_extension == ".kln" or file_extension == ".klinoff" or file_extension == ".nöff":
        print("Interpreting file: " + args[0])
        
    else:
        print("Error: Invalid file extension")
        return
    
    # absolute path
    klinoff_file = get_absolute_path(args[0])
    
    # open file
    file = open(klinoff_file, "r")
    klinoff_content = file.read()
    file.close()
    
    print(klinoff_content)
    
if __name__ == "__main__":
    interpret(sys.argv[1:])