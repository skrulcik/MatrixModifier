#/bin/python

from Matrix import *

def welcome():
    return """ Welcome to Matrix Helper
              Type 'help' to get started."""

def howto():
    return """
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
            -->scale row <row_number> by <constant>

            To add a row to another:
            --> add <row_number> <optional coefficient> to <row_to_be_modified>

            To swap two rows:
            --> swap <row_a> and <row_b>
            """
def get_col_values(row):
    col_values = input("Enter row % of your matrix:",r).split()
    if len(col_values) != num_cols:
        return get_col_values(row)
    else:
        return col_values


def create_sequence():
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
        col_values = get_col_values(r)
        for c in range(num_cols):
            new_matrix.model[r-1][c] = col_values[c]
    return new_matrix
            
    

def main():
    print(welcome())
    should_exit = False
    current = []
    while not should_exit:
        if len(current) == 0:
            current = create_sequence()
        else:
            request = input()
            print "Whoops! We haven't implemented that command yet"
            
        
    

if __name__ == "__main__":
    main()
