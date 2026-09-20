# mainly code for cli menu, import everything else - prompt for states -> pass to algorithms -> print output

import ast # required for turning a string into a list of lists 
from bfs import bfs
from dls import dls
from ids import ids

def get_state(prompt): # will be run for both getting start grid and target grid
    while True:
        entry = input(prompt)
        try:
            return ast.literal_eval(entry)
        except:
            print("Invalid input")

def print_output(): pass # output project required output - can be implemented later

def main(): 
    start = get_state("Start State: ")
    goal = get_state("Goal State: ")

    print(type(start), type(start[0]), type(start[0][0]), start) # test list is properly converted

    # prompt for algorithm choice

    # print_output()

if __name__ == "__main__":
    main()