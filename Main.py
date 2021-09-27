import sys
from collections import deque
from Problem import Problem
from Node import Node


def depth_first_tree_search(problem):
    """
    [Figure 3.7]
     Search the deepest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Does not get trapped by loops.
        If two paths reach a state, only use the first one.
        """

    # This will retun a solution, or a falue.
    # a node with STATE = problem.Initial-State, Path-Cost = 0
    frontier = [Node(problem.initial)]  # Stack, this is the list
    # This pushes all elements that is already declared declared variables
    # in the problem class
    while frontier:  # While the frontier is not empty
        node = frontier.pop()  # pop off the last node
        print(type(node))
        print(frontier)
        # if problem.goal_test(node.state):
        #     return node
        # frontier.extend(node.expand(problem))
    return None


def main():
    p = Problem(["H1", "H2", "H3", "W1", "W2", "W3"], None)
    depth_first_tree_search(p)


main()
