def isWordGuessed(secretWord, lettersGuessed):
    
    n = 0
    for l, letter in enumerate(secretWord):
    	if letter in lettersGuessed:
    		n += 1
    if n == len(secretWord):
    	return True
    else:
    	return False
