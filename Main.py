# Manjesh Prasad
# breadth_first_tree_search
# Assignment 4

from collections import deque

from Problem import Problem
from Node import Node


def breadth_first_tree_search(problem):
    print(problem.initial)
    frontier = deque([Node(problem.initial)])  # FIFO queue
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):                   # if node == goal, then return the node
            return node
        frontier.extend(node.expand(problem))
    return None

def main():
    p = Problem("H1,W1,H2,W2,H3,W3", None)
    solution = breadth_first_tree_search(p)
    if solution == None:
        print("No PATHS FOUND")
    else:
        for count in solution.solution():
            print(count)
        print(solution.depth)


main()
