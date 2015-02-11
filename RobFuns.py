def scorer(enteredScores,scoresAsInts):
	i = 1 
	while 1:
		i = str(raw_input("Enter Scores >>> "))
#		i = (sum(int(x) for x in raw_input('Enter Scores: ').split()))
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

def players(a,b):
	a = str(raw_input("Please enter Player 1 >>> ")) #Requires player1 be defined
	b = str(raw_input("Please enter Player 2 >>> ")) #Requires player2 be defined
