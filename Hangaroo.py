def Hangaroo(secretWord):
    
    print(' ')
    print('Welcome to the Hangaroo Game!')
    print('You need to guess the word that is composed of', len(secretWord), 'letters.')
    
    mistakesMade = 0
    lettersGuessed = []
    
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord,lettersGuessed) == True:
            "\n"
            print('Congratulations! You guessed the word.')
            break
        else:
                "\n"
                print('You have', 8 - mistakesMade, 'guesses left.')
                print('The available letters are', getAvailableLetters(lettersGuessed), '.')
                
                answer = str(input('Guess a letter: ')).lower()
        
                if answer in secretWord and answer not in lettersGuessed:
                    lettersGuessed.append(answer)
                    print('Good guess: ', getGuessedWord(secretWord,lettersGuessed))
        
                elif answer in lettersGuessed:
                    print("You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed))
            
                elif answer not in secretWord:
                    print("That letter is not in the word: ", getGuessedWord(secretWord,lettersGuessed))
                    lettersGuessed.append(answer)
                    mistakesMade += 1
    
        if 8 - mistakesMade == 0:
                "\n"
                print('Sorry, you ran out of guesses. The word was', secretWord, '.')
                break
    
        else:
                continue
    
        
        