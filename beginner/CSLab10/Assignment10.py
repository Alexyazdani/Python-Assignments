"""
Assignment 10: Sorting Cards

Author: Alex Yazdani
CWID: 20399751
Date: 12/6/2022

This file creates the class 'PlayingCard' which stores information representing a playing card.
A dict class variable is used as a lookup for both rank and suit.
The method definitions assume the class will have a rank parameter within (1-13), and a suit parameter of 's', 'h', 'c', or 'd'.
The methods are not equipped to handle invalid parameters.  Use of these may result in errors.
There are methods to return the rank, suit, and blackjack value of the object.
Printing an object of this class will result in a string in the format "Ace of Spades".
UPDATE (12/06/2022): File uses total_ordering functool, which allows sorting with newly defined methods __eq__() and __lt__().
"""
from functools import total_ordering
import pickle

@total_ordering
class PlayingCard():
    """
    Class that represents a playing card.
    Uses instance variables for rank and suit of the card.
    An instance of this class represent a card with a rank within (1-13) and a suit of 's', 'c', 'h', or 'd', corresponding to Spades, Clubs, Hearts, or Diamonds.
    A rank of 1 represents an Ace, 11 represents a Jack, 12 represents a Queen, and 13 represents a King.
    All other ranks correspond to that number.
    """

    CARD_LOOKUP = {'1': 'Ace', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten', '11': 'Jack', '12': 'Queen', '13': 'King', 'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts',  's': 'Spades'}
    SUIT_LIST = ['c', 'd', 'h', 's']

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
        return PlayingCard.CARD_LOOKUP[self.suit]
            
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
        return f"{PlayingCard.CARD_LOOKUP[str(self.rank)]} of {PlayingCard.CARD_LOOKUP[self.suit]}"

    def __eq__(self, other):
        """
        Returns True if playing card object has same rank and suit as "other" playing card
        """
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """
        Returns True if playing card object is less than "other" playing card based on bridge ranking
        """
        if self.rank == other.rank:
            return PlayingCard.SUIT_LIST.index(self.suit) < PlayingCard.SUIT_LIST.index(other.suit)
        else:
            return self.rank < other.rank
        
def main():
    """
    Test program to use __lt__() and __eq__() methods with sort function on a list of cards.
    Creates an unsorted list of PlayingCard objects, sorts the list, and prints each object __str__() string.
    Also puts one card in a pickle file and reads it into a new PlayingCard object.
    """

    CARD1 = PlayingCard(6,"c")
    CARD2 = PlayingCard(11,"s")
    CARD3 = PlayingCard(6,'d')
    CARD4 = PlayingCard(13,"s")
    CARD5 = PlayingCard(9,'h')

    print(f"\nTests for __eq__() and __lt__() methods:")
    print(f"{CARD1.__eq__(CARD2)}  (Should be false)")
    print(f"{CARD1.__eq__(CARD1)}   (Should be true)")
    print(f"{CARD1.__lt__(CARD3)}   (Should be true)")
    print(f"{CARD1.__lt__(CARD1)}  (Should be false)")
    print(f"{CARD2.__lt__(CARD4)}   (Should be true)\n")

    print("Testing sort() with __eq__() and __lt__():")
    card_hand = [CARD1, CARD2, CARD3, CARD4, CARD5]
  
    card_hand.sort()
    for n in range(5):
        print(card_hand[n])
    
    print("\nPickled card:")

    pickled_card = open('pickled_card.pkl', 'wb')
    pickle.dump(CARD1, pickled_card)
    pickled_card.close

    pickled_card = open('pickled_card.pkl', 'rb')
    CARD6 = pickle.load(pickled_card)
    print(CARD6)
    print()

if __name__ == "__main__":
    main()

r"""
PS C:\Users\ayazdani\PythonProjects\CSLab10>  c:; cd 'c:\Users\ayazdani\PythonProjects\CSLab10'; & 'C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\ayazdani\.vscode\extensions\ms-python.python-2022.18.2\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '57972' '--' 'c:\Users\ayazdani\PythonProjects\CSLab10\Assignment10.py' 

Tests for __eq__() and __lt__() methods:
False  (Should be false)
True   (Should be true)
True   (Should be true)
False  (Should be false)
True   (Should be true)

Testing sort() with __eq__() and __lt__():
Six of Clubs
Six of Diamonds
Nine of Hearts
Jack of Spades
King of Spades

Pickled card:
Six of Clubs

PS C:\Users\ayazdani\PythonProjects\CSLab10> 
"""

