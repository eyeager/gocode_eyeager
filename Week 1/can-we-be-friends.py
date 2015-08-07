
points = 0
answers = []

answers.append(raw_input("What's my name? : ").lower() == "emilie")
answers.append(raw_input("Do you like adventures? : ").lower() == "true")
answers.append(raw_input("Are you having fun in Costa Rica? : ").lower() == "true")
answers.append(raw_input("What's my favorite color? : ").lower() == "blue")
answers.append(raw_input("Do you like ice cream? : ").lower() == "true")
answers.append(raw_input("Where am I from? : ").lower() == "texas")

for answer in answers:
	if answer == True:
		points += 1

print points

if points > 3:
	print "Let's be friends!"
else:
	print "Let's work on our relationship!"