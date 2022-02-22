"""
Name: Luciano Zavala
Date: 02/13/22
Assignment: Module 5 & 6: Project - Adversarial Search
Due Date: 02/13/22
About this project: Implement applications that utilize classical Artificial Intelligence techniques, such as
  search algorithms. In this specific code i'm implementing alpha beta prunning using minmax algorithm to get an AI
  based player to compete with.
All work below was performed by LZZ
"""
import itertools


# terminal state function
def terminal_test(state):
    if state in [([1], 1), ([], 2)]:
        terminal_state = True
    elif state in [([1], 2), ([], 1)]:
        terminal_state = True
    else:
        terminal_state = False
    return terminal_state


# utility test function defined to check if theres utility on the move
def utility_test(state):
    # wining state
    if state in [([1], 1), ([], 2)]:
        utility = 1
    # losing state
    elif state in [([1], 2), ([], 1)]:
        utility = -1
    else:
        if state[1] == -1:
            utility = 1
        else:
            utility = -1
    return utility


# function defined to check the next successor moves
def successors(s):
    successor_states = []
    succ = []
    player = s[-1]
    piles = s[0]

    # definition of the success piles
    for i, pile in enumerate(piles):
        for remove in [1, 2, 3]:
            if pile >= remove:
                result = pile - remove
                if result != 0:
                    next_piles = sorted(piles[:i] + [result] + piles[i + 1:])
                else:
                    next_piles = sorted(piles[:i] + piles[i + 1:])
                successor_states.append(next_piles)
    successor_states.sort()

    # define the successor state list
    successor_states = list(successor_states for successor_states, ii in itertools.groupby(successor_states))

    # append the values on the best possible path and return it
    for i in range(len(successor_states)):
        succ.append([successor_states[i], player])
    return succ


# max value computation function
def max_value(max_state):
    # max value
    v = 1

    # terminal state and utility definition
    terminal_state, utility = terminal_test(max_state)
    if not terminal_state:

        # for the next possible moves
        for s in successors(max_state):
            # minimum computation
            v = min(v, min_value(s))
        return v
    else:
        return terminal_test(max_state)


# min value computation function
def min_value(min_state):
    # min value
    v = -1
    # terminal state and utility definition
    terminal_state, utility = terminal_test(min_state)
    if not terminal_state:

        # for the next possible moves
        for s in successors(min_state):
            # minimum computation
            v = max(v, max_value(s))
        return v
    else:
        return terminal_test(min_state)


# Min-Max algorithm computation
def min_max(state):
    if state[1] == 1:
        utility = max_value(state)
    else:
        utility = min_value(state)
    return utility


# alpha beta for max  computation optimization
def max_value_ab(min_state, a, b):
    # value
    v = 1

    # terminal state
    terminal_state = terminal_test(min_state)
    utility = utility_test(min_state)

    if not terminal_state:
        # iteration through the terminal states
        for _ in successors(min_state):

            # check the utility value
            if v > utility:
                utility = v
            if v >= b:
                return utility
            if v > a:
                a = v

    return utility


# alpha beta for min computation optimization
def min_value_ab(max_state, a, b):
    # value
    v = -1

    # terminal state
    terminal_state = terminal_test(max_state)
    utility = utility_test(max_state)

    if not terminal_state:

        # iteration through the terminal states
        for _ in successors(max_state):

            if v < utility:
                utility = v
            if v <= a:
                return utility
            if v < b:
                b = v

    return utility


# Min Max - Alpha Beta pruning
def minimax_ab(state):
    alpha = 0
    beta = 0
    if state[1] == 1:

        # utility based on min
        utility_value = min_value_ab(state, alpha, beta)
    else:
        # utility based on max
        utility_value = max_value_ab(state, alpha, beta)
    return utility_value
