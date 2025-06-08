# Nonce Mining Simulation

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

    def mine_block(self, difficulty):
        print(f"Mining Block {self.index} with difficulty {difficulty}...")
        start_time = time.time()
        target = '0' * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.compute_hash()

        end_time = time.time()
        print(f"Block {self.index} mined!")
        print(f"Nonce: {self.nonce}")
        print(f"Time Taken: {end_time - start_time:.2f} seconds")
        print(f"Hash: {self.hash}\n")

    def __str__(self):
        return f"""
        Block {self.index}:
        Timestamp     : {self.timestamp}
        Data          : {self.data}
        Nonce         : {self.nonce}
        Previous Hash : {self.previous_hash}
        Hash          : {self.hash}
        """
def simulate_mining():
    blockchain = []
    difficulty = 4  

    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    genesis_block.mine_block(difficulty)
    blockchain.append(genesis_block)

    for i in range(1, 3):
        new_block = Block(i, time.time(), f"Block {i} data", blockchain[i - 1].hash)
        new_block.mine_block(difficulty)
        blockchain.append(new_block)
    for block in blockchain:
        print(block)

simulate_mining()
