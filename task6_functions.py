# write your code here
# a) Function to calculate total sales (NA + EU + JP)

def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

print(calculate_total_sales(video_game_sales[0]))


# b) Function to filter games by genre

def filter_by_genre(data, genre='Platform'):
    filtered_games = []

    for game in data:
        if game[GENRE] == genre:
            filtered_games.append(game)

    return filtered_games

# Test with default genre
print(filter_by_genre(video_game_sales))

# Test with specified genre
print(filter_by_genre(video_game_sales, 'Sports'))


# c) Function to create a formatted game summary

def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"

for game in video_game_sales:
    print(get_summary(game))
