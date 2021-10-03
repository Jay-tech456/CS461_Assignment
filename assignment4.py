# Manjesh Prasad
# Abraham Abundis Rocha
# breadth_first_tree_search
# Assignment 4

from collections import deque
class Node:
    # contains a pointer to the parent. If a state is arrived at two paths, then there are two nodes with the same state

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "Node{}".format(self.state)

    def __lt__(self, node):

        # returns true if the sate of the current node is less than the state of the node, otherwise false
        return self.state < node.state

    def expand(self, problem):

        # List the nodes reachable in one step from this node.

        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        # given an action, this method returns that immediate neighbour that can be reached with theat action
        next_sate = problem.result(self.state, action)
        next_node = Node(next_sate, self, action, problem.path_cost(self.path_cost, self.state, action, next_sate))

        return next_node

    def solution(self):
        # retuns the sequence of actions required to reach this node from the root node

        return [node.action for node in self.path()[1:]]

    def path(self):
        # returns a list of nodes forming the path from the root to this node
        node, path_back = self, []
        while node:
            path_back.append(node)

            node = node.parent
        return list(reversed((path_back)))


    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):           # returns a list of all possible actions that can be taken place

        if len(state) == 2:             # if only one husband and wife exist in the site, then there are only
            return list(state)          # one possible action to be taken place
        elif len(state) == 1:
            return None
        if len(state) > 1 and ("," in state):   # if there are multiple people on te isde
            b = state.split(",")
        else:
            b = state
        a = []
        i = 0
        while i < len(b):                       # O(n)
            if i + 1 > (len(b) - 1):
                break
            else:                               # appends to a over a pair that can travel together
                a.append((b[i] + " " + b[i +1]))
            i += 1
        for count in b:
            a.append(count)

        return a

    def result(self, state, action):            # returns a result over any the outcome
        if len(action) == 1:
            return None
        b= state.split(",")
        if " " in action:                       # to delete the element that exist in b
            a = action.split(" ")
            if a[0] in b:
                temp = b.index(a[0])
                b.pop(temp)
            if a[1] in b:
                temp = b.index(a[1])
                b.pop(temp)
        else:

            temp = b.index(action)
            b.pop(temp)

        # ***************** converting the list into a string
        d = ""
        for count in b:
            if count != b[len(b) - 1]:
                d = d + count + " n "
            else:
                d = d + count
        d = d.replace(" n ", ",", 20)

        return d                        # returning d as the string for the next step

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return True
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        if len(state1) == 1:
            return c
        else:
            return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


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


main()
