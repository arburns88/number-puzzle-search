# bfs algorithm

import time # required for cpu time in required output
from collections import deque # used as queue
from node import Node
from search_utilities import get_successors, reconstruct_path


def bfs(start, goal) :
    root = Node(start, None, None, 0)
    queue = deque([root])
    peak_queue_size = 1 # track the highest size of the queue (required output)
    states_processed = 0 # track number of states processed (required output)
    start_time = time.process_time() # track algorithm runtime (required output)

    while queue:
        curr = queue.popleft()
        states_processed += 1

        if curr.state == goal:
            cpu_time = time.process_time() - start_time # take time from start of algorithm to now
            return reconstruct_path(curr), states_processed, peak_queue_size, cpu_time

        for child in get_successors(curr): # get possible child state nodes of curr
            queue.append(child) # add to queue

        peak_queue_size = max(peak_queue_size, len(queue)) # check if at largest queue size

    # if queue runs without reaching goal state
    cpu_time = time.process_time() - start_time 
    return None, states_processed, peak_queue_size, cpu_time