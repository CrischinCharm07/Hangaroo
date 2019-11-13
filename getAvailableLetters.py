import string
englet = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    
    word = []
    
    for letters in englet:
        if letters not in lettersGuessed:
            word.append(letters)
            
    return ''.join(word)
