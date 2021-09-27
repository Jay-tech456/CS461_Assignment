class Problem:
    # There is a chance that we might need to pass in the objects as the husband and wives
    def __init__(self, initial, goal=None):
        # This is the class constructor,
        # T
        self.initial = initial  # the initial state of the entire program
        self.goal = goal  # The goal is to get everyone into the other side of the river
        print("Hello world")

    def actions(self, state):
        # This will return the actions that can be executred in the given state. The result would be a list
        # if there are still more actions.
        # This method returns all possible actions agent can execute in the given state state
        raise NotImplementedError("The class should implement this ")

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