#!/usr/bin/env python
################################################
# Problem Set 
# Name: Michael H. Roberts
# Collaborators: None
# Time: 
################################################
import sys

i = 1 
scoret = []
scored = []
score_int = []
score_int2 = []
while 1:
	i = raw_input('Enter Score >>>  ')
	if i in ('t'):
		scoret.append(i)
	if i in ('d'):
		scored.append(i)
for i in scoret:
	score_int.append(int(i))
	x = sum(score_int)
for i in scored:
	score_int2.append(int(i))
	y = sum(score_int2)
