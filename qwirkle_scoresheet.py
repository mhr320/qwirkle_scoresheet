#!/usr/bin/env python -tt
################################################
# Problem Set 
# Name: Michael H. Roberts
# Collaborators: None
# Time: 
################################################
import sys
from RobFuns import *

i = 1
p2 = 'None'
s1 = []
ss1 = []
s2 = []
ss2 = []

player1 = str(raw_input("Please enter Player 1 >>> \n"))
player2 = str(raw_input("Please enter Player 2 >>> \n"))


yana("Do you wish to start the game")

while yana:
	yana("%s Ready \n" % player1)
	if yana:
		scorer(s1,ss1)
	p1 = sum(ss1)
	print "%s's score: %s & %s's score: %s \n" % (player1, p1, player2, p2)

	yana("%s Ready \n" % player2)

  	scorer(s2,ss2)

	p2 = sum(ss2)
	print "%s's score: %s & %s's score: %s \n" % (player1, p1, player2, p2)

