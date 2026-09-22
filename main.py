# mainly code for cli menu, import everything else - prompt for states -> pass to algorithms -> print output

import ast # required for turning a string into a list of lists 
from bfs import bfs
from dls import dls
from ids import ids


def get_state(prompt): # will be run for both getting start grid and target grid
    while True: # prompt user for input state until correct format is recieved
        entry = input(prompt)
        try:
            return ast.literal_eval(entry)
        except:
            print("Invalid input.\nExample input: [ [ 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0] ]\n")


def print_output(search, result): # output project required output - can be implemented later
    moves, states_processed, max_size, cpu_time = result # outputs of search algorithms

    print(f"\nSearch type: {search} \n")
    if moves is None: # no solution found
        print("No solution found.")
    else: # solution found
        print(f"Number of moves: {len(moves)}")
        print(f"Sequence of moves: {', '.join(moves)}") # prints moves as a string (project requirement)
    print(f"Number of states removed: {states_processed}")
    print(f"Maximum size of the queue/stack: {max_size}")
    print(f"CPU time: {cpu_time}")


def main(): 
    # get start and target states from user input
    start = get_state("Start State: ")
    goal = get_state("Goal State: ")

    # print(type(start), type(start[0]), type(start[0][0]), start) # test input string is properly converted

    # prompt user for algorithm choice (project specifies: 1-BFS 2-IDS 3-BFS and IDS 4-DLS)
    print("\nChoose algorithm to run: \n  1) BFS\n  2) IDS\n  3) BFS and IDS\n  4) DLS\n")
    while True: # prompt for input until a valid int is recieved
        try:
            algorithm = int(input("Enter choice: "))
            break
        except:
            print("Entry not an int")
    
    # print the output
    if algorithm == 1: # BFS
        print_output("BFS", bfs(start, goal))

    if algorithm == 2: # IDS
        print("IDS not yet implemented")

    if algorithm == 3: # BFS and IDS (BFS first then IDS?)
        print_output("BFS", bfs(start, goal))
        print("\n")
        print("IDS not yet implemented")

    if algorithm == 4: # DLS
        print("DLS not yet implemented")


if __name__ == "__main__":
    main()