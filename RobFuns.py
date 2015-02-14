def scorer(enteredScores):
	i = 1 
	while 1:
		i = str(raw_input("<<<Score>>> "))
		if i in ('n'): break
		enteredScores.append(i)
		for i in enteredScores:
			print i


