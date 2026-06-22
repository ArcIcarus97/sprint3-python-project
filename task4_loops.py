# write your code here
# a) Print games with more than 25M global sales

for game in video_game_sales:
    if game[GLOBAL_SALES] > 25:
        print(game[NAME], game[GLOBAL_SALES])


# b) Count games released before 2000

pre_2000_count = 0

for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count += 1

print(pre_2000_count)


# c) Total NA and Japan sales

total_na_sales = 0
total_jp_sales = 0

for game in video_game_sales:
    total_na_sales += game[NA_SALES]
    total_jp_sales += game[JP_SALES]

print(f"North America Sales: {total_na_sales}")
print(f"Japan Sales: {total_jp_sales}")

if total_na_sales > total_jp_sales:
    print("North America had higher sales")
elif total_jp_sales > total_na_sales:
    print("Japan had higher sales")
else:
    print("Sales were equal")


# d) Nintendo games

nintendo_games = []

for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(nintendo_games)
print(len(nintendo_games))
