def scorer(enteredScores,scoresAsInts):
	i = 1 
	while 1:
		i = str(raw_input("Enter Scores >>> "))
		if i in ('n'): break
		enteredScores.append(i)
		for i in enteredScores:
			print i
	for i in enteredScores:
		scoresAsInts.append(int(i))

def yana(question):
	reply = str(raw_input(question+' (y/n): ')).lower().strip()
	if reply[0] == 'y':
		return True
	if reply[0] == 'n':
		return False
	else:
		return yes_or_no("Uhhhh... please enter ")
