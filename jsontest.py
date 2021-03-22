import json

with open('database2.json') as d:
    data = json.load(d)

names = list(data['cpus'].keys())
print(names[0])

game_input1 = "Grand Theft Auto V"
game_1 = data['games'].get(game_input1)
print(game_1)