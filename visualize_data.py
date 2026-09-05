"""
8 Ball Pool Data Visualization
Author: Dhruv
Description: Connects to the SQLite database and generates a dual-chart dashboard 
showing win rates and long-term bankroll trajectory.
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Connect to the database and pull the data
conn = sqlite3.connect('pool_analytics.db')

# Pull win rates for the bar chart
query_win_rates = """
SELECT 
    break_type, 
    ROUND(SUM(CASE WHEN outcome = 'Win' THEN 1.0 ELSE 0.0 END) / COUNT(match_id) * 100, 2) AS win_percentage 
FROM match_history 
GROUP BY break_type 
ORDER BY win_percentage DESC;
"""
df_win = pd.read_sql_query(query_win_rates, conn)

# Pull running bankroll for the line chart (using the built-in rowid for chronological order)
query_bankroll = "SELECT rowid AS match_number, running_bankroll FROM match_history;"
df_bankroll = pd.read_sql_query(query_bankroll, conn)

conn.close()

# 2. Set up the visual dashboard layout (1 row, 2 columns)
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 3. Chart 1: Bar Chart (Win Rates)
sns.barplot(data=df_win, x='break_type', y='win_percentage', ax=axes[0], palette='Blues_r')
axes[0].set_title('Win Percentage by Break Strategy', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Win Rate (%)', fontsize=12)
axes[0].set_xlabel('Break Type', fontsize=12)
axes[0].tick_params(axis='x', rotation=15) # Tilt labels for readability

# Add exact numbers on top of the bars
for i in axes[0].containers:
    axes[0].bar_label(i, fmt='%.1f%%', label_type='edge', padding=3)

# 4. Chart 2: Line Chart (Bankroll Trajectory)
sns.lineplot(data=df_bankroll, x='match_number', y='running_bankroll', ax=axes[1], color='forestgreen', linewidth=2)
axes[1].set_title('Coin Bankroll Over 1,000 Matches', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Total Coins', fontsize=12)
axes[1].set_xlabel('Match Number', fontsize=12)
# Add a dashed line showing the starting bankroll
axes[1].axhline(y=50000, color='red', linestyle='--', alpha=0.7, label='Starting Balance')
axes[1].legend()

# 5. Polish and save the dashboard
plt.tight_layout()
plt.savefig('pool_analytics_dashboard.png', dpi=300)
print("Dashboard successfully saved as 'pool_analytics_dashboard.png'.")
plt.show()
