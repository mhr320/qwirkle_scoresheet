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
player1 = str(raw_input("\nPlease enter Player 1 >>> \n"))
player2 = str(raw_input("\nPlease enter Player 2 >>> \n"))
while True:
	option = int(raw_input("\nChoose 1 to play, 2 to quit, or 3 to see scores (if any)\n"))
	if option == 1:
		print "\nPlease enter %s's scores: \n" % player1	
		scorer(s1)
		ss1 = map(int, s1)
		p1 = sum(ss1)
		p1Len = len(s1)
		print "\n%s's score: %s & %s's score: %s \n" % (player1, p1, player2, p2)
		print "\nPlease enter %s's scores: \n" % player2	
		scorer(s2)
		ss2 = map(int, s2)
		p2 = sum(ss2)
		p2Len = len(s2)
		print "\n%s's score: %s & %s's score: %s \n" % (player1, p1, player2, p2)
	if option == 2:
		break
	if option == 3:
		print " \n\n"
		print "-----------------SCORES----------------- \n"
		print "   %s                        %s \n" % (player1,player2)
		print "%s in %s moves!              %s in %s moves! " % (p1, p1Len, p2, p2Len)
		print " \n\n "