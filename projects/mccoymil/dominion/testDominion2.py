# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:43 2020

@author: mccoymil
"""

import Dominion
import testUtility as test

# list: 0 num of players, 1 old nV, 2 old nC, 4 number of cards for deck
values = []

# Costruct the Player objects
# param:    values list
#           populates values with number of nC, nV
# return:   players list for game play
players = test.players(values)

# Define box with call to test.box
# passed values for nC and nV information
box = test.box(values)

# define supply order from test.supplyorder
supply_order = test.supplyorder()

# Pick 10 cards from box to be in the supply.
# add the value to select
values.append(10)
supply = test.defaultsupply(box, values)

# initialize the trash
trash = []

# Play the game
turn = 0
while not Dominion.gameover(supply):

    # supply resets every round, the victory condition cannot be reached.
    # creates a random supply every turn

    supply = test.defaultsupply(box, values)
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)