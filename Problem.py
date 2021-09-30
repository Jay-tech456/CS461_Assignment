#
# class Problem:
#     # There is a chance that we might need to pass in the objects as the husband and wives
#     def __init__(self, initial, goal=None):
#         # This is the class constructor,
#         # T
#         self.initial = initial  # the initial state of the entire program
#         self.goal = goal  # The goal is to get everyone into the other side of the river
#
#     def actions(self, state):
#         # This will return the actions that can be executred in the given state. The result would be a list
#         # if there are still more actions.
#         # This method returns all possible actions agent can execute in the given state state
#         raise NotImplementedError("The class should implement this ")
#         return self.state
#
#     def result(self, state, action):
#         # return the state that results from executing the given actions in the given state.... the action must be
#         # one of self.actions(state)
#         raise NotImplementedError
#
#     def goal_test(self, state):
#         # returns true if the state is a goal. The default method compares to the state to self.goal
#         # or checks for state in self.goal if it is a list, as specified in the
#         # constructor. Overide this mehtod if checking against a single self.goal is not enough.
#         if isinstance(self.goal, list):
#             return is_in(state, self.goal)
#         else:
#             return state == self.goal
#
#     def path_cost(self, c, state1, action, state2):
#         # returns the cost of a solution path that arrives at state 2 from state 1 through actions
#         # assuming that there exist a state that cost 1 up to state.
#         # if the path does matter, it will consider c and maybe state1, but if the path does not matter, it will
#         # only look at state2
#
#         # We are moving the couples from state1 to state 2, and the total mount of actions that is cost initially is
#         # 0, but once moving between state1 to state2, if the order matters, then we have to increment by one, but if the
#         # order does not matter, than bypass
#
#         return c + 1

class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        b = state.split(" ")
        print("Here is the state that is being passed in " + str(state))
        print("Here is B " + str(b))
        a = []
        i = 0
        while i < len(b):                       # O(n) W1H1
            if i + 1 > (len(b) - 1):
                break
            a.append((b[i] + b[i+1]))
            i += 1
        for count in b:
            a.append(count)
            print( "Here is a " + str(a))
        return a

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        count = 0
        a = action[count]
        state = a
        count += 1
        return state

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError
