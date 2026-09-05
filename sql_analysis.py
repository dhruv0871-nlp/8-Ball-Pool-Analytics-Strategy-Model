"""
8 Ball Pool SQL Analytics
Author: Dhruv
Description: Executes SQL queries against the SQLite database to extract 
win rates and profitability metrics.
"""

import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('pool_analytics.db')

print("--- QUERY 1: Win Percentage by Break Type ---")
# This query calculates the win rate by counting total matches and conditional wins
query_1 = """
SELECT 
    break_type,
    COUNT(match_id) AS total_matches,
    SUM(CASE WHEN outcome = 'Win' THEN 1 ELSE 0 END) AS total_wins,
    ROUND(SUM(CASE WHEN outcome = 'Win' THEN 1.0 ELSE 0.0 END) / COUNT(match_id) * 100, 2) AS win_percentage
FROM match_history
GROUP BY break_type
ORDER BY win_percentage DESC;
"""
df_win_rates = pd.read_sql_query(query_1, conn)
print(df_win_rates.to_string(index=False))
print("\n" + "="*50 + "\n")


print("--- QUERY 2: Total Profitability by Break Type ---")
# This query sums up the net coin change to see which break actually makes money
query_2 = """
SELECT 
    break_type,
    SUM(net_coins_change) AS total_profit_loss
FROM match_history
GROUP BY break_type
ORDER BY total_profit_loss DESC;
"""
df_profit = pd.read_sql_query(query_2, conn)
print(df_profit.to_string(index=False))

# Close the connection
conn.close()