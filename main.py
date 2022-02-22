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
import random
from algorithms import *


# Pre : accepts empty rockList, random pile as integers
# Post: creates the board
def create_board(rock_list, rand_pile):
    # create board
    for i in range(0, rand_pile):
        randRock = random.randint(1, 8)
        rock_list.append(randRock)
    print("-" * 25)


# Pre : accepts empty rockList, random pile as integers
# Post: prints the board
def display_board(rock_list, rand_pile):
    # display board
    print("-" * 25)
    for i in range(0, rand_pile):
        print('Pile {}: {}'.format(i + 1, 'O' * rock_list[i]))
    print("-" * 25)


# Pre : accepts modified rockList, random integer for piles, current player as string
# Post: returns a string when input is invalid, updates game board for following turns
def get_valid_input(rock_list, current_player):
    # Begin loop that tests for valid input - if valid, break loop - if not, keep asking
    while True:
        stones = input('{}, how many stones to remove? '.format(current_player))
        piles = input('Pick a pile to remove from: ')

        # If all conditions for input are CORRECT, break out of loop
        if (stones and piles) and (stones.isdigit()) and (piles.isdigit()):
            if (int(stones) > 0) and (int(piles) <= len(rock_list)) and (int(piles) > 0):
                if int(stones) <= rock_list[int(piles) - 1]:
                    if (int(stones) != 0) and (int(piles) != 0):
                        break

        # If not, display this statement
        print("Hmmm.", current_player, ", you entered an invalid value. Please try again.")

    # Update state
    rock_list[int(piles) - 1] -= int(stones)


# Pre : accepts modified rockList, random integer for piles, names of players, current palyer as string
# Post: prints winner of game, asks if players want to play game again, determine current player
def play(rock_list, rand_pile, name_1, current_player):

    # Begin loop to initiate player switching
    while rock_list != [0] * len(rock_list):
        get_valid_input(rock_list, current_player)

        # state definition
        state = (rock_list, current_player)

        # list of successor moves
        list_of_successors = successors(state)

        # enumerate teh state number
        number_of_next_states = len(list_of_successors)

        # Iterate through list of successor and implement ab pruning
        for s, next_state in enumerate(list_of_successors):
            utility_value = minimax_ab(next_state)

            # redefine th utility value adn assign next state
            if utility_value == -1:
                state = next_state

            elif utility_value == 1:
                state = list_of_successors[random.randrange(0, number_of_next_states)]
                # state = next_state

        # display the board
        display_board(rock_list, rand_pile)

        # switch players 2->1, 1->2

        """
        I couldn't figure out how to define the next state to be a move 
        """

        if current_player == name_1:
            current_player = state
        else:
            current_player = name_1

    print(current_player, " is the winner is :)")


# Define an empty rock list to append rocks to, define random integers, call functions
rockList = []
# random number of rock piles
randPile = random.randint(2, 5)
# random number of rocks
# randRock = random.randint(1, 9)

# get the name of the players
name1 = input("Enter player 1 name: ")

# Set current player to 1 (for switching later)
player = name1

create_board(rockList, randPile)
display_board(rockList, randPile)  # Set initial board

play(rockList, randPile, name1, player)
