
# Manjesh Prasad
# Abraham Abundis Rocha
# breadth_first_tree_search
# Assignment 4
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
