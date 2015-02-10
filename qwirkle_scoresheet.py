#!/usr/bin/env python -tt
################################################
# Problem Set 
# Name: Michael H. Roberts
# Collaborators: None
# Time: 
################################################
import sys

print 'Player 1 > '
p1 = raw_input()
print 'Player 2 > '
p2 = raw_input()

def yes_or_no(question):
	reply = str(raw_input(question+' (y/n): ')).lower().strip()
	if reply[0] == 'y':
		return True
	if reply[0] == 'n':
		return False
	else:
		return yes_or_no("Uhhhh... please enter ")

def main():
	yes_or_no("hrlp")

if __name__ == '__main__':
	main()
