import os

def display_cwd():
    cwd = os.getcwd()
    print("The current working directory is", cwd)
    
def parent_directory():
    os.chdir("../")
    
    
      


parent_directory()
display_cwd()
