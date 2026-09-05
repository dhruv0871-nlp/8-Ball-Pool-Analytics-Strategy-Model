"""
8 Ball Pool Synthetic Data Generator
Author: Dhruv
Description: Generates 1,000 simulated matches for exploratory data analysis,
tracking break patterns, wagers, and match outcomes.
"""

import pandas as pd
import numpy as np
import random

# Set seed so the "random" data is reproducible every time you run it
np.random.seed(42)
random.seed(42)

# Define the game constraints
num_matches = 1000

table_tiers = {
    'London Pub': 50,
    'Sydney Marina': 250,
    'Moscow Winter': 500,
    'Tokyo Warrior': 2500,
    'Las Vegas': 10000
}

break_types = ['Power Break', 'Second-Ball Break', 'Soft Break', 'Dry Break (No Pot)']

# Generate Base Data
matches = []
current_bankroll = 50000  # Starting coin balance

for i in range(1, num_matches + 1):
    # Randomly select table and wager
    table = random.choice(list(table_tiers.keys()))
    wager = table_tiers[table]
    
    # Assign a break type with weighted probabilities
    break_type = np.random.choice(break_types, p=[0.4, 0.3, 0.1, 0.2])
    
    # Bake in the "Business Logic" - correlating break type to win probability
    if break_type == 'Second-Ball Break':
        win_prob = 0.65  # Strategic break yields highest win rate
    elif break_type == 'Power Break':
        win_prob = 0.50  # Chaotic layout, 50/50 chance
    elif break_type == 'Soft Break':
        win_prob = 0.40  # Poor spread, lower win chance
    else: # Dry Break
        win_prob = 0.30  # Opponent gets the table, very low win chance
        
    # Determine Outcome based on probability
    outcome = np.random.choice(['Win', 'Loss'], p=[win_prob, 1 - win_prob])
    
    # Calculate coin exchange
    net_coins = wager if outcome == 'Win' else -wager
    current_bankroll += net_coins
    
    # Append row
    matches.append({
        'match_id': f"MTH-{str(i).zfill(4)}",
        'table_tier': table,
        'wager_amount': wager,
        'break_type': break_type,
        'outcome': outcome,
        'net_coins_change': net_coins,
        'running_bankroll': current_bankroll
    })

# Convert to Pandas DataFrame
df = pd.DataFrame(matches)

# Export to CSV
file_name = 'pool_match_data.csv'
df.to_csv(file_name, index=False)

print(f"Success! {num_matches} matches generated and saved to {file_name}.")
print(df.head())