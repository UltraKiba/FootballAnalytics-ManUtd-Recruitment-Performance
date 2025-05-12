# Python Code Snippet 2: Basic Shot Map Visualization

import matplotlib.pyplot as plt
import pandas as pd
# mplsoccer is a common library for drawing football pitches.
# It might need to be installed if not already in the environment: pip install mplsoccer
from mplsoccer import Pitch

# Hypothetical shot data (In a real scenario, this would be from a detailed event dataset)
# Coordinates are often in a system where (0,0) is one corner and (100,100) or (120,80) is the opposite, depending on the provider.
# For this example, let's assume a 100x100 pitch where (100,50) is the center of the goal being attacked.
shot_data = {
    'player_name': ["Højlund", "Fernandes", "Antony", "Rashford", "Garnacho", "Fernandes"],
    'x_coordinate': [85, 70, 90, 80, 92, 75],  # Distance from own goal line (attacking right)
    'y_coordinate': [50, 55, 35, 60, 48, 40],  # Distance from center line (positive is up, negative is down)
    'outcome': ["Goal", "Save", "Miss", "Goal", "Miss", "Save"],
    'xG': [0.45, 0.12, 0.08, 0.30, 0.15, 0.05] # Expected Goal value of the shot
}
shots_df = pd.DataFrame(shot_data)

# Create the pitch
# Pitch type can be specified (e.g., 'statsbomb', 'opta', 'tracab') which affects coordinate systems
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc', constrained_layout=True, tight_layout=False)
fig, ax = pitch.draw(figsize=(10, 7))
fig.set_facecolor('#22312b')

# Plotting the shots
# We will size the points by their xG value and color them by outcome.
for i, shot in shots_df.iterrows():
    if shot['outcome'] == 'Goal':
        shot_color = 'green'
        edge_color = 'white'
        marker = 'o' # Circle for goal
    elif shot['outcome'] == 'Save':
        shot_color = 'yellow'
        edge_color = 'black'
        marker = 's' # Square for save
    else: # Miss, Block, etc.
        shot_color = 'red'
        edge_color = 'black'
        marker = 'x' # X for miss

    # Note: mplsoccer's StatsBomb pitch has x from 0-120 and y from 0-80.
    # The example data might need scaling if it's from a different system.
    # For this illustrative example, we assume coordinates are compatible or have been scaled.
    # Let's assume our x_coordinate (80-95) is attacking towards x=120, and y_coordinate (35-60) is within 0-80.
    # We'll need to adjust if the data is, for example, 0-100 for x and 0-100 for y.
    # For simplicity, let's assume the coordinates are already in a StatsBomb-like system for this example.
    # A real scenario would require careful coordinate transformation.
    
    # Example: if original data is 0-100 for x and 0-100 for y, attacking right goal:
    # plot_x = shot['x_coordinate'] * 1.2 
    # plot_y = shot['y_coordinate'] * 0.8
    
    # Using direct coordinates for illustration, assuming they fit StatsBomb's 120x80 pitch
    # For attacking right goal, x should be high (e.g. > 60), y around center (e.g. 20-60)
    plot_x = shot['x_coordinate'] / 100 * 120 # Scale from 0-100 to 0-120
    plot_y = shot['y_coordinate'] / 100 * 80  # Scale from 0-100 to 0-80


    pitch.scatter(plot_x, plot_y, 
                  s=(shot['xG'] * 500) + 100,  # Size by xG (larger xG = larger point)
                  c=shot_color, 
                  edgecolors=edge_color, 
                  marker=marker,
                  alpha=0.7,
                  ax=ax,
                  label=shot['outcome'] if i == 0 else "") # Only label once per outcome for legend

# Add a title
ax.set_title("Manchester United Shot Map (Illustrative 23/24)", color="white", fontsize=18, pad=15)

# Create a legend (this part can be tricky with scatter plots of varying sizes/colors)
# A more robust legend might require creating proxy artists
handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Goal', markerfacecolor='green', markersize=10),
    plt.Line2D([0], [0], marker='s', color='w', label='Save', markerfacecolor='yellow', markersize=10),
    plt.Line2D([0], [0], marker='x', color='w', label='Miss/Other', markerfacecolor='red', markersize=10)
]
ax.legend(handles=handles, loc='upper right', labelcolor='white', facecolor='#3f564d')

plt.show()

# To save the figure:
# fig.savefig('/home/ubuntu/shot_map_visualization.png', dpi=300, facecolor='#22312b')

print("Illustrative shot map code executed. If running in a script, the plot window would appear.")
print("In a Jupyter Notebook, the plot would be displayed inline if %matplotlib inline is used.")

