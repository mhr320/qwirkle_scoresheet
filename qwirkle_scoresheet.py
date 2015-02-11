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
s1 = []
ss1 = []
s2 = []
ss2 = []

player1 = str(raw_input("Please enter Player 1 >>> "))
player2 = str(raw_input("Please enter Player 2 >>> "))


yana("Do you wish to start the game")


if yana:
	yana("%s Ready" % player1)
	if yana:
		scorer(s1,ss1)

p1 = sum(ss1)
print "%s's score: %s \n" % (player1, p1)

yana("%s Ready" % player2)

if yana:
  scorer(s2,ss2)

p2 = sum(ss2)
print "%s's score: %s" % (player2, p2)

