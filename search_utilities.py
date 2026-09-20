# supporting functions - find_blank , swap , get_successors , reconstruct-path

import copy # required for copying a list of lists
from node import Node

Moves = { # directions to try moving and their move values
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def find_blank(state): # returns the location of the 0
    rows = range(len(state))
    columns = range(len(state[row]))
    for row in rows: # for every row (lists in state)
        for coloumn in columns: # for every column in curr row (list of list in state)
            if state[row][column] == 0:
                return (row, column)


def swap(state, p1, p2): # swaps tiles p1 and p2 (moving empty tile)
    new_state = copy.deepcopy(state) # required to make new_state a new distinct copy
    r1, c1 = pos1
    r2, c2 = pos2
    new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
    return new_state


def get_successors(node): # create nodes based on new successor states for current node (i.e. bottom left node create a moved-right node and moved-up node)
    successors = []
    size = len(node.state)
    empty = find_blank(node.state)
    empty_row, empty_column = empty
    for move, (dr, dc) in moves.items(): # for all possible move directions
        target_row, target_col = empty_row + dr, empty_col + dc # set target position

        if 0 <= target_row < size and 0 <= target_col < size: # if target positions are valid in lists
            new_state = swap(node.state, blank_pos, (target_row, target_col))

            if node.parent is None or new_state != node.parent.state: # if new state isnt its grandparents state (i.e. != move right then move left (inverse of parents move))
                child = Node(new_state, node, move, node.depth + 1)
                successors.append(child)

    return successors


def reconstruct_path(node): # take current node (goal mode ideally) and walk back up tree to start building a path list
    moves = []
    curr = node
    while curr.parent is not None:
        moves.append(curr.move) # project specifies output should be a list of moves
        curr = curr.parent
    moves.reverse() # moves get appended in last-first order, need to be reversed
    return moves