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

#Output :-

Mining Block 0 with difficulty 4...
Block 0 mined!
Nonce: 16466
Time Taken: 0.05 seconds
Hash: 0000ed95cc7b9820ff30987e4c3bac06b46bd6d55bcef4f1f6f18700b51577c1

Mining Block 1 with difficulty 4...
Block 1 mined!
Nonce: 74550
Time Taken: 0.22 seconds
Hash: 0000fd580e306a25aeff8d475edd6426c3e8ba997d1f3f4ef14e514d36faf7e4

Mining Block 2 with difficulty 4...
Block 2 mined!
Nonce: 36803
Time Taken: 0.11 seconds
Hash: 0000d51a4a7c5fd33c2c68af73d80772156d25dee0fc93ad19353e30b1f34cca


        Block 0:
        Timestamp     : 1749393716.5219939
        Data          : Genesis Block
        Nonce         : 16466
        Previous Hash : 0
        Hash          : 0000ed95cc7b9820ff30987e4c3bac06b46bd6d55bcef4f1f6f18700b51577c1


        Block 1:
        Timestamp     : 1749393716.5768156
        Data          : Block 1 data
        Nonce         : 74550
        Previous Hash : 0000ed95cc7b9820ff30987e4c3bac06b46bd6d55bcef4f1f6f18700b51577c1
        Hash          : 0000fd580e306a25aeff8d475edd6426c3e8ba997d1f3f4ef14e514d36faf7e4


        Block 2:
        Timestamp     : 1749393716.796886
        Data          : Block 2 data
        Nonce         : 36803
        Previous Hash : 0000fd580e306a25aeff8d475edd6426c3e8ba997d1f3f4ef14e514d36faf7e4
        Hash          : 0000d51a4a7c5fd33c2c68af73d80772156d25dee0fc93ad19353e30b1f34cca
