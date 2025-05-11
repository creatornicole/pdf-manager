import sys

print("""
######################################################################
      
       ############     ############        ###############
      ###############  ###############     ###############       
     ####        #### ####         ####   ####                   
    ###############  ####          ####  ##############  
   ##############   ####          ####  ##############      
  ####             ####          ####  ####              
 ####             ################    ####
####             ###############     ####

      
                   ##### ##### ##### #
            ###      #   #   # #   # #
                     #   ##### ##### ####
      

by Nicole Gottschall
Last Update: 2025-05-11

----------------------------------------------------      

To find out more about the script:
python pdf_manager.py -h

######################################################################
""")

### FUNCTIONS
def remove():
    pass

def merge():
    pass

def add():
    pass

def help(f: str = None) -> str:
    descriptions = {
        "r": remove_descrip,
        "m": merge_descrip,
        "a": add_descrip,
    }

    return_str = "Executed helper function..."

    if f is None:
        print(script_descrip)
    else:
        try: 
            print(descriptions[f])
        except KeyError:
            return_str = f"Error: Invalid helper parameter provided: '{f}'." \
            "\nPlease provide a valid helper parameter or ask for help using -h.\n"
    
    return return_str

### VARIABLES
script_descrip = """
######################################################################

SCRIPT HANDBOOK:

Function that can be executed using the command line:
- remove pages from the PDF
- merge several PDFs together
- add a blank page to the PDF
      
To run the Python script:
python pdf_manager.py [function] [other params]
      
Where function is a placeholder, that should be replaced with the desired action you would like to perform:
- -r ... remove
- -m ... merge
- -a ... add
- -h ... help (provides details and instructions how to use each function to modify the PDF file)

and other params represent function-specific paramters that vary depending on the function you are executing.
      
- -r ... remove
    - 1st: filepath to the PDF file
    - 2nd: page specification
- -m ... merge
    - n params are n PDF files that should be merged togehter
- -a ... add
    - 1st: filepath to the PDF file
    - 2nd: page after which the blank page will be added
- -h ... help
    - 1st: abbreviation of the function to be explained
    - for example: use r to get an explanation of the remove function
      
Each function creates a new version of the original PDF with the specified changes applied. This ensures that the original file remains untouched, preventing any accidental, irreversible modifications.

######################################################################
"""
remove_descrip = """
REMOVE
"""
merge_descrip = """
MERGE
"""
add_descrip = """
ADD
"""

# dictionary mapping abbreviations to function names
operations = {
    "-r": remove,
    "-m": merge,
    "-a": add,
    "-h": help
}

### EXECUTE FUNCTION BASED ON COMMAND LINE ARGUMENTS
try:
    # second command line argument is action parameter
    action = operations[sys.argv[1]](*sys.argv[2:])
    print(action)
except IndexError:
    print("Error: No action parameter provided." \
    "\n Please provide a parameter or ask for help using -h.\n")
except KeyError:
    print("Error: Action parameter invalid." \
    "\n Please provide a valid action parameter or ask for help using -h.\n")

    



