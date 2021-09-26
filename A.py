class Problem(object):
    # There is a chance that we might need to pass in the objects as the husband and wives
    def __init__(self, initial, goal=None):
        # This is the class constructor,
        # T
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        # This will return the actions that can be executred in the given state. The result would be a list
        # if there are still more actions.
        # This method returns all possible actions agent can execute in the given state state
        raise NotImplementedError

    def result(self, state, action):
        # return the state that results from executing the given actions in the given state.... the action must be
        # one of self.actions(state)
        raise NotImplementedError

    def goal_test(self, state):
        # returns true if the state is a goal. The default method compares to the state to self.goal
        # or checks for state in self.goal if it is a list, as specified in the
        # constructor. Overide this mehtod if checking against a single self.goal is not enough.
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        # returns the cost of a solution path that arrives at state 2 from state 1 through actions
        # assuming that there exist a state that cost 1 up to state.
        # if the path does matter, it will consider c and maybe state1, but if the path does not matter, it will
        # only look at state2

        # We are moving the couples from state1 to state 2, and the total mount of actions that is cost initially is
        # 0, but once moving between state1 to state2, if the order matters, then we have to increment by one, but if the
        # order does not matter, than bypass

        return c + 1


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
