#for players in self.players:
#	player_score = raw_input("What's the score for player: %s" % (player.name))
#	player.get_score(player_score)

#	string.append("word")

#	player.get_score()

string_input = raw_input("scores: ")

print string_input
print type(string_input)

array = string_input.split(",")

print type(array[0])

for index,number in enumerate(array):
	array[index] = int(number)

print array
print type(array[0])