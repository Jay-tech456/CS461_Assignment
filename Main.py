from collections import deque

from Problem import Problem
from Node import Node


def depth_first_graph_search(problem):
    """
    [Figure 3.7]
    Search the deepest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Does not get trapped by loops.
    If two paths reach a state, only use the first one.
    """
    frontier = [(Node(problem.initial))]  # Stack
    print("frontier " + str(frontier))

    explored = set()

    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node

        print("Here is the node.state" + str(node.state))
        explored.add(node.state)
        print(explored)                 # Should print out the initial string "H1H2W1W2", and then hits the extend
        frontier.extend(child for child in node.expand(problem) if child.state not in explored and child not in frontier)
    return None



def main():
    p = Problem("H1,W1", None)
    depth_first_graph_search(p)
    solution = depth_first_graph_search(p)
    if(solution == None):
        print("No PATHS FOUND")
    else:
        print(solution)


main()
