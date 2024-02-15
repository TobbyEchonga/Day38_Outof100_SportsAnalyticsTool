import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load basketball game data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def analyze_game_statistics(data):
    """
    Analyze and visualize basketball game statistics.
    """
    if data is None:
        return

    # Calculate total points for each team
    data['TotalPoints'] = data['Team1Points'] + data['Team2Points']

    # Display basic statistics
    print("\nBasic Game Statistics:")
    print(data.describe())

    # Visualize total points over games
    plt.figure(figsize=(10, 6))
    plt.plot(data['GameID'], data['TotalPoints'], marker='o', linestyle='-', color='b')
    plt.title('Total Points in Each Game')
    plt.xlabel('Game ID')
    plt.ylabel('Total Points')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Sample basketball game data (replace with your own dataset)
    file_path = 'basketball_game_data.csv'
    
    # Load and analyze game statistics
    game_data = load_data(file_path)
    analyze_game_statistics(game_data)
