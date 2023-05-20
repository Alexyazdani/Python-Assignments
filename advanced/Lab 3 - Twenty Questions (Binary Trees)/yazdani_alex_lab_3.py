"""
Lab 3: Twenty Questions
Alexander Yazdani
CWID: 20399751
Date: 05/01/2023

This program acts as a game of Twenty questions.
First, a class BinaryTreeNode is defined to act as the nodes of the next class.
The class TwentyQuestions first initializes its only attribute, its root node.
It then uses the guess_routine() method to build up a binary tree, which acts
as a database for the game of twenty questions.
This method uses recursion to traverse through the tree and add nodes when
incorrect guess are made.  When a correct guess is made, the method exits
without changing the tree.

The main() function Instantiates the TwentyQuestions class, and loops through
its guess_routine() method to build the binary tree while playing with the
user.

The file assumes valid user input of Y, y, N, or n.
Invalid input may result in unexpected behavior.
"""


class BinaryTreeNode:
    """
    This class will act as the nodes of any binary tree.
    The class has a data attribute and up to two child nodes, distinguised
    by left or right side.
    """

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class TwentyQuestions:
    """
    This class defines a game of twenty questions based on a binary tree.
    When instantiated, the guess_routine() method may be used to play the game.
    The program must be trained by the user to build the binary tree.
    Recursion is used to traverse the tree, effectively asking the user
    questions until making a guess.
    """
    def __init__(self):
        self._root = None

    def guess_routine(self):
        """
        Public method for guess_routine()
        This method prompts the user for a creature, which will act as the
        root node of the binary tree.  This root node is then used as input to
        the recursive private method.
        """
        print("\n*** Let's Play! ***\n\nThink of a creature...")
        if self._root is None:
            self._root = BinaryTreeNode(input(
                "There are no creatures loaded, please tell me your creature. "
                ))
            print("Thank you!  Now we can play.")
            return
        self._guess_routine(self._root)

    def _guess_routine(self, sub_root):
        """
        Private method for guess_routine()
        This method checks whether the current node is a leaf or not.  If it is
        not a leaf, a question will be asked to the user and recursion will be
        used with the user's response to traverse the tree.
        If it is a leaf node, the program will attempt to guess the user's
        creature.  If correct, the program ends.  If incorrect, the program
        will ask the user some further questions, add the new creature to the
        tree, then end.
        """
        if sub_root.left_child is None:
            response = input(
                f"Is this your creature: {sub_root.data}? (Y/N): ")
            if response.upper() == "Y":
                print("Excellent, thank you for playing!")
                return
            new_leaf = input("What is your creature? ")
            new_question = input(
                "Please enter a yes or no question that will"+
                f" distinguish {sub_root.data} from {new_leaf}. ")
            new_response = input(
                f"For your creature {new_leaf}, {new_question} (Y/N) ")
            if new_response.upper() == "Y":
                sub_root.left_child = BinaryTreeNode(new_leaf)
                sub_root.right_child = BinaryTreeNode(sub_root.data)
            else:
                sub_root.left_child = BinaryTreeNode(sub_root.data)
                sub_root.right_child = BinaryTreeNode(new_leaf)
            sub_root.data = new_question
            print(f"Thank you, I have added {new_leaf} to the database.")
        else:
            response = input(f"{sub_root.data}\nPlease enter Y or N ")
            if response.upper() == "Y":
                self._guess_routine(sub_root.left_child)
            else:
                self._guess_routine(sub_root.right_child)


def main():
    """
    Test Run Output:  (May contain PEP8 Violations)

    *** Let's Play! ***

    Think of a creature...
    There are no creatures loaded, please tell me your creature. Cat
    Thank you!  Now we can play.

    *** Let's Play! ***

    Think of a creature...
    Is this your creature: Cat? (Y/N): N
    What is your creature? Dog
    Please enter a yes or no question that will distinguish Cat from Dog. Does it bark?
    For your creature Dog, Does it bark? (Y/N) Y
    Thank you, I have added Dog to the database.

    *** Let's Play! ***

    Think of a creature...
    Does it bark?
    Please enter Y or N N
    Is this your creature: Cat? (Y/N): N
    What is your creature? Giraffe
    Please enter a yes or no question that will distinguish Cat from Giraffe. Does it have long legs?
    For your creature Giraffe, Does it have long legs? (Y/N) Y
    Thank you, I have added Giraffe to the database.

    *** Let's Play! ***

    Think of a creature...
    Does it bark?
    Please enter Y or N n
    Does it have long legs?
    Please enter Y or N y
    Is this your creature: Giraffe? (Y/N): n
    What is your creature? Spider
    Please enter a yes or no question that will distinguish Giraffe from Spider. Does it have a long neck?
    For your creature Spider, Does it have a long neck? (Y/N) n
    Thank you, I have added Spider to the database.

    *** Let's Play! ***

    Think of a creature...
    Does it bark?
    Please enter Y or N n
    Does it have long legs?
    Please enter Y or N y
    Does it have a long neck?
    Please enter Y or N y
    Is this your creature: Giraffe? (Y/N): y
    Excellent, thank you for playing!

    *** Let's Play! ***

    Think of a creature...
    Does it bark?
    Please enter Y or N
    """
    creature_game = TwentyQuestions()
    while True:
        creature_game.guess_routine()


if __name__ == "__main__":
    main()
