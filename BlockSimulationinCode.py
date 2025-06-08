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

# 🔍 Check integrity
def check_chain_validity(blockchain):
    for i in range(1, len(blockchain)):
        current = blockchain[i]
        previous = blockchain[i - 1]

        if current.previous_hash != previous.hash:
            print(f"⚠️ Block {i} is INVALID due to broken hash link!")
        else:
            print(f"Block {i} is valid.")

# 🚀 Run it
blockchain = create_blockchain()
print("Original Blockchain:\n")
display_chain(blockchain)

tamper_chain(blockchain)
print("Blockchain After Tampering:\n")
display_chain(blockchain)

print("Validity Check:\n")
check_chain_validity(blockchain)
