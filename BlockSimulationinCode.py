# Block Simulation in Code

import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def __str__(self):
        return f"""
        Block {self.index}:
        Timestamp     : {self.timestamp}
        Data          : {self.data}
        Previous Hash : {self.previous_hash}
        Hash          : {self.hash}
        """


def create_blockchain():
    blockchain = []
    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    blockchain.append(genesis_block)
    for i in range(1, 3):
        new_block = Block(i, time.time(), f"Block {i} data", blockchain[i-1].hash)
        blockchain.append(new_block)

    return blockchain


def display_chain(blockchain):
    for block in blockchain:
        print(block)


def tamper_chain(blockchain):
    print("Tampering Block 1...\n")
    blockchain[1].data = "Tampered data"
    blockchain[1].hash = blockchain[1].compute_hash()


def check_chain_validity(blockchain):
    for i in range(1, len(blockchain)):
        current = blockchain[i]
        previous = blockchain[i - 1]

        if current.previous_hash != previous.hash:
            print(f"Block {i} is INVALID due to broken hash link!")
        else:
            print(f"Block {i} is valid.")


blockchain = create_blockchain()
print("Original Blockchain:\n")
display_chain(blockchain)

tamper_chain(blockchain)
print("Blockchain After Tampering:\n")
display_chain(blockchain)

print("Validity Check:\n")
check_chain_validity(blockchain)

# OUTPUT
Original Blockchain: 


        Block 0:
        Timestamp     : 1749393346.947217
        Data          : Genesis Block
        Previous Hash : 0
        Hash          : 7e0431b850efaeaf41a911c5f23d44682893b456f94fc26e5917dc2cbec203a5


        Block 1:
        Timestamp     : 1749393347.018393
        Data          : Block 1 data
        Previous Hash : 7e0431b850efaeaf41a911c5f23d44682893b456f94fc26e5917dc2cbec203a5
        Hash          : df754b4f21f229d7c20f90522f68176daeedc4734f1a667fea3b216ed7b12379


        Block 2:
        Timestamp     : 1749393347.019385
        Data          : Block 2 data
        Previous Hash : df754b4f21f229d7c20f90522f68176daeedc4734f1a667fea3b216ed7b12379
        Hash          : f83eed47beb8c72787aade78fb101277c2266c34792bb95d2d397cd2ead31c23

Tampering Block 1...

Blockchain After Tampering:


        Block 0:
        Timestamp     : 1749393346.947217
        Data          : Genesis Block
        Previous Hash : 0
        Hash          : 7e0431b850efaeaf41a911c5f23d44682893b456f94fc26e5917dc2cbec203a5


        Block 1:
        Timestamp     : 1749393347.018393
        Data          : Tampered data
        Previous Hash : 7e0431b850efaeaf41a911c5f23d44682893b456f94fc26e5917dc2cbec203a5
        Hash          : 1b3eb3a8ad1d988ea950c120dbf6beb6a7c912f72a79abb4c62952397858e2d0


        Block 2:
        Timestamp     : 1749393347.019385
        Data          : Block 2 data
        Previous Hash : df754b4f21f229d7c20f90522f68176daeedc4734f1a667fea3b216ed7b12379
        Hash          : f83eed47beb8c72787aade78fb101277c2266c34792bb95d2d397cd2ead31c23

Validity Check:

Block 1 is valid.
Block 2 is INVALID due to broken hash link!
