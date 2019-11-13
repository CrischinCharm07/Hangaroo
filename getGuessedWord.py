def getGuessedWord(secretWord,lettersGuessed):
    
    word = []
    for letters in secretWord:
        if letters in lettersGuessed:
            word.append(letters)
        else:
             word.append('_')
             
    return ' '.join(word)
    
