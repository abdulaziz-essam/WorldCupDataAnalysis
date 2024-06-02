import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def greet(df ,club):
    # Convert 'Goals' column to numeric, forcing non-numeric values to NaN
    df['Goals'] = pd.to_numeric(df['Goals'], errors='coerce')

    # Fill NaN values with 0 and convert 'Goals' column to integer
    df['Goals'] = df['Goals'].fillna(0).astype(int)

    # Print the first few values of the 'Goals' column to verify the conversion
    print(df['Goals'].head())

    # Filter the DataFrame for players in the 'Ajax' club
    filtered_df = df[df['club'] == club]

    # Sort the filtered DataFrame by 'Goals' in descending order
    filtered_df = filtered_df.sort_values(by='Goals', ascending=False)

    # Drop duplicate player names, keeping the first occurrence
    unique_players_df = filtered_df.drop_duplicates(subset=['player'])

    # Retrieve the first ten rows of unique player names and their goals
    top_players = unique_players_df[['player', 'Goals']].head(10)

    # Sort the top_players DataFrame by 'Goals' column in ascending order
    top_players = top_players.sort_values(by='Goals')

    # Create a pie chart
    plt.figure(figsize=(10, 6))

    # Use a colormap for coloring wedges
    colors = sns.color_palette('viridis', len(top_players))

    # Plot the pie chart with player names as labels and their goals as values
    plt.pie(top_players['Goals'], labels=top_players['player'], colors=colors, autopct='%1.1f%%', startangle=140)

    # Add a title to the pie chart
    plt.title('Distribution of Goals Scored by' + club + 'Players')

    # Ensure the pie chart is drawn as a circle
    plt.axis('equal')

    # Display the plot
    plt.show()

# Example usage:
# df = pd.read_csv('path_to_your_csv_file.csv')  # Load your data into a DataFrame
# greet(df)  # Call the function with your DataFrame
