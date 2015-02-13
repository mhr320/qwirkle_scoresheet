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
p2 = 'NaDa'
s1 = []
ss1 = []
s2 = []
ss2 = []

player1 = str(raw_input("Please enter Player 1 >>> \n"))
player2 = str(raw_input("Please enter Player 2 >>> \n"))


while 1:
	print "Please enter %s's scores: " % player1	
	scorer(s1)
	ss1 = map(int, s1)
	p1 = sum(ss1)
	print "%s's score: %s & %s's score: %s \n" % (player1, p1, player2, p2)
	print "Please enter %s's scores: " % player2	
	scorer(s2)
	ss2 = map(int, s2)
	p2 = sum(ss2)
	print "%s's score: %s & %s's score: %s \n" % (player1, p1, player2, p2)
	
