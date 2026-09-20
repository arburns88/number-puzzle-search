# supporting functions - find_blank , swap , get_successors , reconstruct-path

import copy # required for copying a list of lists
from node import Node

def find_blank(state): pass # returns the location of the 0


def swap(state, x, y): pass # swaps empty tile to with tile at x,y


def get_successors(node): pass # create nodes based on new successor states for current node (i.e. bottom left node create a moved-right node and moved-up node)


def reconstruct_path(node): pass # take current node (goal mode ideally) and walk back up tree to start building a path list