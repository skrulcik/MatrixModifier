#/bin/python
import string
from Matrix import *

alpha_index = 0 #Used in generating names for new matrices
def defaultName(length=1):
    chars = string.ascii_uppercase
    name = ''.join()
    return random.choice(chars)

# TODO:add help text for other commands
help_texts = {"welcome":"\n\n Welcome to Matrix Helper \n Enter 'help' for instructions, 'quit' to exit program \n",
	    "std_help": """
            How to Use Matrix Helper
            
            Instead of simple solving systems of equations,
            Matrix Helper will allow you to "show work" for
            your own problems. It is restricted to elementary
            row operations, but will show you the output for
            ensure no arithmetic errors are made.

            In the future, output will go to a TeX file so it
            can be used as a legitimate record of work.

            Using Matrix Helper

            To create a matrix:
            --> create
            How many rows in your matrix?
            --> <number_of_rows>
            How many columns in your matrix?
            --> <number_of_columns>           
            Enter row 1 of your matrix:
            --> <entry 1> <entry 2>....<entry m>
            

            To mutiply a row by a constant:
            --> scale <row_number> by <constant>

            To add a row to another:
            --> add <row_number> <optional coefficient> to <row_to_be_modified>

            To swap two rows:
            --> swap <row_a> and <row_b>

            To raise current matrix to a power:
            --> power <exp>

            To output TeX:
            --> tex

            To print current matrices:
            --> print state

            To Select the current matrix:
            --> select <matrix id>

            To multiply the current matrix by another:
            --> multiply by <other matrix id>
            """}
matrices = [] #Global for now, objects in future
current = -1

def howto(mode):
    # Generic method for printing help text for various commands
    if mode not in help_texts:
	mode = "std_help"
    print help_texts[mode]
def std_help(raw_data):
    howto("std_help")
def welcome(raw_data):
    howto("welcome")

# Helper for create method
def get_col_values(row, num_cols):
    col_values = raw_input("Enter row %r of your matrix:\n"%row)
    col_values = col_values.replace(","," ") #Prefer space delimiter, but accept comma
    col_values = col_values.strip().split() #Remove whitespace and seperate values
    if len(col_values) != num_cols:
	# User error: did not enter columns correctly
	print("Please enter the correct number of values.")
        return get_col_values(row, num_cols)
    for i in xrange(len(col_values)):
	# Ensure we are working with numbers
	if(col_values[i].isalpha()):
	    print("Illegal character, please re-enter.")
	    print("Variable implementation available in future.")
	    return get_col_values(row, num_cols)
	# If number, safe to convert to float
        col_values[i] = float(eval(col_values[i]))
    return col_values


def create_sequence(raw_data):
    global current
    num_rows = int(input("How many rows in your matrix?"))
    if(num_rows <= 0):
        print "Invalid input: must have at least 1 row in your matrix"
        return None
    num_cols = int(input("How many columns in your matrix?"))
    if(num_cols <= 0):
        print "Invalid input: must have at least 1 column in your matrix"
        return None
    new_matrix = Matrix(num_rows, num_cols)
    for r in range(1,num_rows+1):
        col_values = get_col_values(r, num_cols)
        for c in range(num_cols):
            new_matrix.model[r-1][c] = col_values[c]
    new_matrix.display()
    matrices.append(new_matrix)
    current = len(matrices)-1
    print "current", current

def row_swap(data, matrix):
    tokens = data.split()
    if(len(tokens) == 4):
        #Work with coefficient
        rowa = int(tokens[1])
        rowb = int(tokens[3])
        matrix.swap(rowa, rowb)
    else:
        print("Please use format 'swap <row_a> and <row_b>'")
def tex_it(raw_data):
    global current
    global matrices
    if current >= 0 and current < len(matrices):
        print(matrices[current].to_latex())
    else:
        print("There are no matrices yet")

def print_info(raw_data):
    # print matrix state by default
    global matrices
    global current
    print("\n\nBegin Print State:")
    for c in range(len(matrices)):
        if c == current:
            h,w = matrices[current].size()
            print("\n\nCurrent Matrix (%d) :" % c)
            buff = ""
            for _ in range(4*w+5): buff += "-"
            print(buff)
            matrices[c].display()
            print(buff)
        else:
            print("\n\nMatrix (%d):" % c)
            matrices[c].display()
    print("End Print State\n\n")
                
            


def row_add(data, matrix):
    tokens = data.split()
    if(len(tokens) == 5):
        #Work with coefficient
        origin_row = float(tokens[4])
        add_row = float(tokens[1])
        add_coefficient = float(eval(tokens[2]))
        matrix.rowAddOther(origin_row, add_row, add_coefficient)
    elif (len(tokens) == 4):
        #Without coefficient
        origin_row = float(tokens[3])
        add_row = float(tokens[1])
        matrix.rowAddOther(origin_row, add_row, 1)
    else:
        print("Please use format 'add <row_number> <optional coefficient> to <row_to_be_modified>'")

def row_scale(data, matrix):
    tokens = data.split()
    if(len(tokens) != 4):
        print("Please use format 'scale <row_number> by <constant>'")
    else:
        row = float(tokens[1])
        factor = float(eval(tokens[3]))
        matrix.rowScale(row, factor)
 
def raise_power(data, matrix):
    tokens = data.split()
    if len(tokens) != 2:
            print("Please use format 'power <exp>'")
    else:
        exp = int(tokens[1])
        matrix.to_power(exp)
def select_new(data, matrix):
    tokens = data.split()
    global current
    global matrices
    if len(tokens) != 2:
        print("Please use format 'select <matrix id>'")
    else:
        current = int(tokens[1])
        print("Current matrix:")
        matrices[current].display()
        
def matrix_mult(data, matrix):
    tokens = data.split()
    global current
    global matrices
    if len(tokens) != 3:
        print("Please use format 'multiply by <other_id>'")
    else:
        other_idx = int(tokens[2])
        # NOTE this creates a new matrix, not modifying the original
        C = matrices[current].multiply(matrices[other_idx])
        matrices.append(C)
        current = len(matrices) - 1


def main():
    commands = {"create":create_sequence,
                    "welcome":welcome,
                    "help":std_help,
                    "tex":tex_it,
                    "print":print_info}
    modifiers = {"swap":row_swap,
                    "add":row_add,
                    "scale":row_scale,
                    "power":raise_power,
                    "select":select_new,
                    "multiply":matrix_mult}
    should_exit = False
    welcome("")
    while not should_exit:
        #Main application loop
        raw_data = raw_input("Enter a command:")
        raw_data = raw_data.strip().lower() #Commands are not case sensitive
        request = raw_data.split()[0]
        if request == "":
    	    # No input is interpreted as not knowing what to do
    	    request = "help"
        if request in commands:
    	    # Standard command list
    	    commands[request](raw_data)
        elif request in modifiers:
            if current >= 0:
                modifiers[request](raw_data, matrices[current])
            else:
                print("Please create a Matrix first.")
        elif request == "quit":
    	    # User wants to quit
    	    should_exit = True
        else:
            print "Whoops! We haven't implemented that command yet"
    print "Thanks for using Matrix Helper!"
            
        
    

if __name__ == "__main__":
    main()
