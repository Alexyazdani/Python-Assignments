"""
Lab 6: Blockchain
Alexander Yazdani
CWID: 20399751
Date: 05/25/2023

This file contains a definition for a class, Block(), which functions as a blockchain.
The blockchain itself is effectively a linked list.
There is a method to add to the blockchain and to replay the list of transactions.
Hashes are compared during the replay to catch if a fraudulent transaction was added.
A test program at the end of the file demonstrates the blockchain's performance.
"""
class Block():
    """
    Block() class to function as a blockchain, effectively a linked list.
    """
    def __init__(self, data=None, prev_hash=0):
        """
        First node will have prev_hash=0, last node with have ._next=None.
        New hash is created using a tuple containing data and the previous hash.
        """
        self._data = data
        self._next = None
        self._hash = hash((self._data, prev_hash))
        print(f"Transaction added.  New hash is {self._hash}")
    
    def add_block(self, data):
        """
        Method to add a block to the end of the chain.
        """
        if self._next is None:
            self._next = Block(data, self._hash)
        else:
            self._next.add_block(data)

    def replay(self, prev_hash=0):
        """
        Method to traverse the chain and display each transaction.
        Hashes are compared for validation.
        """
        if self._hash != hash((self._data, prev_hash)):
            print("Blockchain is Corrupted!\n")
            return
        elif self._next is None:
            print(self._data)
            print("Blockchain Verified.  End of Transactions")
            print(f"Final hash is {self._hash}")
        else:
            if prev_hash == 0:
                print("Replaying Blockchain")
            print(self._data)
            self._next.replay(self._hash)


def main():
    """
    Demonstration of working blockchain with fraud detection.
    """
    new_chain = Block("Starting Balance Alex = $1000")
    new_chain.add_block("Alex pays John $10 for providing a great idea.")
    new_chain.add_block("Alex pays the Tommy $50 for ending the noise.")
    new_chain.add_block("The cat pays Pet Food Express $20 for catnip.")
    print()
    new_chain.replay()
    print()

    fraud = "Alex Pays John $1000 for providing a great idea."
    new_chain._next._next._data = fraud
    new_chain.replay()

if __name__ == "__main__":
    main()

"""
Transaction added.  New hash is 4485840974297721699
Transaction added.  New hash is -4869252577676190059
Transaction added.  New hash is -3450184786312627777
Transaction added.  New hash is 6798113637278573581

Replaying Blockchain
Starting Balance Alex = $1000
Alex pays John $10 for providing a great idea.
Alex pays the Tommy $50 for ending the noise.
The cat pays Pet Food Express $20 for catnip.
Blockchain Verified.  End of Transactions
Final hash is 6798113637278573581

Replaying Blockchain
Starting Balance Alex = $1000
Alex pays John $10 for providing a great idea.
Blockchain is Corrupted!

"""