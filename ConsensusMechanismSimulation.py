import random

miners = [
    {"name": "Miner A", "power": random.randint(10, 100)},
    {"name": "Miner B", "power": random.randint(10, 100)},
    {"name": "Miner C", "power": random.randint(10, 100)},
]

pow_winner = max(miners, key=lambda miner: miner["power"])

print(" PoW (Proof of Work)")
print("Miners and their power:")
for miner in miners:
    print(f"- {miner['name']}: Power {miner['power']}")
print(f"Selected: {pow_winner['name']} with power {pow_winner['power']}")
print("Logic: The miner with the **most computational power** wins.\n")


stakers = [
    {"name": "Staker X", "stake": random.randint(100, 1000)},
    {"name": "Staker Y", "stake": random.randint(100, 1000)},
    {"name": "Staker Z", "stake": random.randint(100, 1000)},
]

pos_winner = max(stakers, key=lambda staker: staker["stake"])

print("PoS (Proof of Stake)")
print("Stakers and their stakes:")
for staker in stakers:
    print(f"- {staker['name']}: Stake {staker['stake']}")
print(f"Selected: {pos_winner['name']} with stake {pos_winner['stake']}")
print("Logic: The staker with the **highest amount staked** is chosen.\n")


delegates = [
    {"name": "Delegate 1", "votes": 0},
    {"name": "Delegate 2", "votes": 0},
    {"name": "Delegate 3", "votes": 0},
]

voters = [
    {"name": "Voter A", "vote": "Delegate 2"},
    {"name": "Voter B", "vote": "Delegate 1"},
    {"name": "Voter C", "vote": "Delegate 2"},
]

for voter in voters:
    for delegate in delegates:
        if delegate["name"] == voter["vote"]:
            delegate["votes"] += 1

max_votes = max(delegate["votes"] for delegate in delegates)
top_delegates = [d for d in delegates if d["votes"] == max_votes]


dpos_winner = random.choice(top_delegates)

print("DPoS (Delegated Proof of Stake)")
print("Voters and their votes:")
for voter in voters:
    print(f"- {voter['name']} voted for {voter['vote']}")
print("Delegates and their vote counts:")
for delegate in delegates:
    print(f"- {delegate['name']}: {delegate['votes']} votes")
print(f"Selected: {dpos_winner['name']} with {dpos_winner['votes']} vote(s)")
print("Logic: Users vote for delegates. The top-voted is chosen to produce blocks.\n")

# output 

PoW (Proof of Work)
Miners and their power:
- Miner A: Power 40
- Miner B: Power 47
- Miner C: Power 87
Selected: Miner C with power 87
Logic: The miner with the **most computational power** wins.

PoS (Proof of Stake)
Stakers and their stakes:
- Staker X: Stake 356
- Staker Y: Stake 238
- Staker Z: Stake 994
Selected: Staker Z with stake 994
Logic: The staker with the **highest amount staked** is chosen.

DPoS (Delegated Proof of Stake)
Voters and their votes:
- Voter A voted for Delegate 2
- Voter B voted for Delegate 1
- Voter C voted for Delegate 2
Delegates and their vote counts:
- Delegate 1: 1 votes
- Delegate 2: 2 votes
- Delegate 3: 0 votes
Selected: Delegate 2 with 2 vote(s)
Logic: Users vote for delegates. The top-voted is chosen to produce blocks.
