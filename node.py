# node class - separate to not conflict in edits

class Node:
    def __init__(self, state, parent, move, depth):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
