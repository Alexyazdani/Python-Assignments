import random
def guessingGame():
    """
    generates a random number between 1 and 10 and repeatedly asks the user to guess it until she gets it right
    """
    secretNumber = random.randint(1, 11)
    userGuess = 0
    while userGuess != secretNumber:
        userGuess = int(input("Type your guess"))
    print ("you got it!")

if __name__ == "__main__":
    guessingGame()