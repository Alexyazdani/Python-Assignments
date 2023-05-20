"""
Assignment 9: A Playing Card

Author: Alex Yazdani
CWID: 20399751
Date: 11/27/2022

This file creates the class 'PlayingCard' which stores information representing a playing card.
A dict class variable is used as a lookup for both rank and suit.
The method definitions assume the class will have a rank parameter within (1-13), and a suit parameter of 's', 'h', 'c', or 'd'.
The methods are not equipped to handle invalid parameters.  Use of these may result in errors.
There are methods to return the rank, suit, and blackjack value of the object.
Printing an object of this class will result in a string in the format "Ace of Spades".
"""

class PlayingCard():
    """
    Class that represents a playing card.
    Uses instance variables for rank and suit of the card.
    An instance of this class represent a card with a rank within (1-13) and a suit of 's', 'c', 'h', or 'd', corresponding to Spades, Clubs, Hearts, or Diamonds.
    A rank of 1 represents an Ace, 11 represents a Jack, 12 represents a Queen, and 13 represents a King.
    All other ranks correspond to that number.
    """

    card_lookup = {'1': 'Ace', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten', '11': 'Jack', '12': 'Queen', '13': 'King', 'c': 'Clubs', 's': 'Spades', 'h': 'Hearts', 'd': 'Diamonds'}

    def __init__(self, rank, suit):
        """
        Initialization for PlayingCard class, sets instance variables rank and suit for object
        """
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """
        Returns the Rank (1-13) of PlayingCard object
        """
        return self.rank
    
    def getSuit(self):
        """
        Returns suit of PlayingCard object
        """
        return PlayingCard.card_lookup[self.suit]
            
    def bjValue(self):
        """
        Returns the Blackjack value (1-10) of PlayingCard object
        """
        if self.rank > 10:
            bj_val = 10
        else:
            bj_val = self.rank
        return bj_val
      
    def __str__(self):
        """
        Output string for printing PlayingCard class
        """
        return f"{PlayingCard.card_lookup[str(self.rank)]} of {PlayingCard.card_lookup[self.suit]}"

def main():
    """
    Test program for PlayingCard class and its methods.
    """

    c1 = PlayingCard(5,"c") # constructs the Card object
    print (c1)  # verifies that the Card object got constructed
    print (c1.getRank()) # outputs 5
    print (c1.getSuit()) # outputs "Clubs"
    print (c1.bjValue()) # outputs 5
    
    c2 = PlayingCard(13, "h") # constructs the Card object
    print (c2)  # verifies that the Card object got contructed
    print (c2.getRank()) # outputs 13
    print (c2.getSuit()) # outputs "Hearts"
    print (c2.bjValue()) # outputs 10

if __name__ == "__main__":
    main()

r"""

PS C:\Users\ayazdani\PythonProjects\CSLab9>  c:; cd 'c:\Users\ayazdani\PythonProjects\CSLab9'; & 'C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\ayazdani\.vscode\extensions\ms-python.python-2022.18.2\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '60862' '--' 'c:\Users\ayazdani\PythonProjects\CSLab9\Assignment9.py' 
Five of Clubs
5
Clubs
5
King of Hearts
13
Hearts
10
PS C:\Users\ayazdani\PythonProjects\CSLab9>

"""

