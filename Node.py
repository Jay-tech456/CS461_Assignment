

class Node:
    # contains a pointer to the parent. If a state is arrived at two paths, then there are two nodes with the same state

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "Node{}".format(self.state)

    def __lt__(self, node):

        # returns true if the sate of the current node is less than the state of the node, otherwise false
        return self.state < node.state

    def expand(self, problem):

        # List the nodes reachable in one step from this node.

        return [self.child_node(problem, action) for action in problem.action(self.state)]

    def child_node(self, problem, action):
        # given an action, this method returns that immediate neighbour that can be reached with theat action
        next_sate = problem.result(self.state, action)
        next_node = Node(next_sate, self, action, problem.path_cost(self.path_cost, self.sate, action, next_sate))
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

