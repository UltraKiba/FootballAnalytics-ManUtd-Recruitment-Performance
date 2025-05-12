# Python Code Snippet 1: Player Cost-Effectiveness Analysis

import pandas as pd

# Hypothetical player data (In a real scenario, this would be loaded from a CSV, database, or API)
data = {
    'player_name': ['Antony', 'Rasmus Højlund', 'Bruno Fernandes', 'Lisandro Martínez', 'Jadon Sancho', 'Marcus Rashford', 'Casemiro'],
    'transfer_fee_millions': [85, 72, 55, 57, 73, 0, 70], # Rashford is an academy graduate, fee is 0
    'goals_23_24': [1, 10, 10, 1, 3, 8, 1], # Example data from pasted_content or hypothetical
    'assists_23_24': [1, 4, 8, 0, 0, 2, 1], # Example data
    'minutes_played_23_24': [1500, 2000, 3000, 1000, 500, 2500, 1800], # Example data
    'position': ['Winger', 'Forward', 'Midfielder', 'Defender', 'Winger', 'Forward', 'Midfielder']
}
player_df = pd.DataFrame(data)

# Calculate total goal contributions (Goals + Assists)
player_df['total_goal_contributions'] = player_df['goals_23_24'] + player_df['assists_23_24']

# Calculate cost per goal contribution in millions
# Handle cases where contributions are zero to avoid division by zero error
player_df['cost_per_contribution_millions'] = player_df.apply(
    lambda row: row['transfer_fee_millions'] / row['total_goal_contributions'] if row['total_goal_contributions'] > 0 else float('inf'),
    axis=1
)

# Calculate goal contributions per 90 minutes played
player_df['contributions_per_90'] = player_df.apply(
    lambda row: (row['total_goal_contributions'] / row['minutes_played_23_24']) * 90 if row['minutes_played_23_24'] > 0 else 0,
    axis=1
)

print("Player Cost-Effectiveness Analysis (Illustrative):")
# Display relevant columns, sorted by cost-effectiveness (lower cost per contribution is better)
# and then by contributions per 90 (higher is better)
print(player_df[['player_name', 'position', 'transfer_fee_millions', 'total_goal_contributions', 'cost_per_contribution_millions', 'contributions_per_90']].sort_values(by=['cost_per_contribution_millions', 'contributions_per_90'], ascending=[True, False]))

# Further analysis could involve:
# - Benchmarking these values against league averages for different positions.
# - Visualizing these metrics (e.g., scatter plot of fee vs. contributions_per_90).
# - Incorporating wages for a more complete Total Cost of Ownership (TCO) analysis.

