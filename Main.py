from collections import deque

from Problem import Problem
from Node import Node


def breadth_first_tree_search(problem):
    """
    [Figure 3.7]
    Search the shallowest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """

    frontier = deque([Node(problem.initial)])  # FIFO queue

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None



def main():
    p = Problem("H1,W1,H2,W2", None)
    solution = breadth_first_tree_search(p)
    if(solution == None):
        print("No PATHS FOUND")
    else:
        print(solution)


main()
