# Claude generated test cases since none were provided:

# test_cases.py
# Hardcoded start/goal pairs for quickly testing without retyping input
# at the CLI prompts every time. Run directly: python3 test_cases.py

from bfs import bfs
from dls import dls
from ids import ids
from main import print_output

TEST_CASES = [
    {
        "label": "1-move",
        "start": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]],
        "goal":  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
    },
    {
        "label": "3-move",
        "start": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 12], [13, 14, 11, 15]],
        "goal":  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
    },
    {
        "label": "12-move",
        "start": [[1, 2, 3, 4], [5, 7, 8, 12], [9, 6, 0, 14], [13, 11, 10, 15]],
        "goal":  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
    },
]

if __name__ == "__main__":
    for case in TEST_CASES:
        print(f"\n===== {case['label']} =====")
        
        print_output("BFS", bfs(case["start"], case["goal"]))

        # Uncomment once dls/ids are actually implemented:

        # print_output("IDS", ids(case["start"], case["goal"]))

        # print_output("DLS", dls(case["start"], case["goal"], limit=15))