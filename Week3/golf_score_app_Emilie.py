'''
Golf Score Calculator App

The goal of this app is for you to be able to enter scores for different players and print a leaderboard.  You are given a file with the base scores for a default course that you will need to read in (ask an instructor if you don't understand golf!).

# Example UI in the Terminal:
# How many players are in the golf tournament? 2
# How many holes are in the golf course? 18
# What is the name for player 1? Jonathan Lau
# What is the name for player 2? Jeremy Schwartz
# What are the scores for player 1? [3,3,3,3,3...]
# What are the scores for player 2? [3,3,3,3,3]
# Type p to print the leaderboard: p
# LeaderBoard
# 1 - Jonathan Lau, Overall Score: 73, +1
# 2 - Jeremy Schwartz, Overall Score: 76, +5

You will implement this idea and create a golf score calculator using classes.  

You are free to adjust the gameplaym, how the app works, and to extend it as you wish.

Here are some basic recommendations for how to design your classes:

1) A CourseLayout class:

In charge of reading in the file with the base scores for the golf course.

You will use the file given to you as the default.  

Optionally, you can allow the user to enter a filename for a different golf course.

2) A PlayerScore class:

In charge of handling player information and scores

3) A AppInterface Class:

This has a simple method that runs the game and talks to the terminal I/O.

It also has a method that uses information from the CourseLayout and PlayerScore and prints a leaderboard.

Ex:

LeaderBoard
1 - Jonathan Lau, Overall Score: 73, +1
2 - Jeremy Schwartz, Overall Score: 76, +4

Note: The last number is simply the overall score minus 72 (it's how golf works...)

'''

class CourseLayout:
    def __init__(self, holes, filename):
    	self.holes = int(holes)

        with open(filename) as course:
	        par = course.read().strip("\n").split(",")

    	self.par = map(lambda x: int(x), par)
    	self.par_score()

    def par_score(self):
    	self.par_total = reduce(lambda x,y: x+y, self.par)
    	return self.par_total


class Player:
    def __init__(self, name):
        self.name = name

    def scores(self, scores):
    	self.scores = map(lambda x: int(x), scores)
    	return self.scores

    def score_total(self, scores):
    	self.score = reduce(lambda x,y: x+y, self.scores)
    	return self.score

class AppInterface:
	def __init__(self):
		print "How good is your golf game?"

		holes = raw_input("How many holes are in this course?: ")
		while not self.__test_input(holes, int):
			holes = raw_input("Not a number. Try again: ")

		filename = raw_input("What course file would you like to load?: ")
		try:
			open(filename)
		except:
			print "WARNING: File does not exist. Using course_layout.txt as default."
			filename = "course_layout.txt"

		players = raw_input("How many players in this game?: ")
		while not self.__test_input(players, int):
			players = raw_input("Not a number. Try again: ")

		self.course = CourseLayout(holes, filename)
		self.get_players(players)
		self.get_scores()
		self.print_leaderboard()


	def __test_input(self, test_data, data_type):
		while True:
			try:
				data_type(test_data)
				return True
			except:
				return False

	def __test_score_input(self, scores, holes):
		if len(scores) != int(holes):
			print "\nWARNING: You input %i score(s) for %s holes.\n" % (len(scores), holes)
		for key,value in enumerate(scores):
			while not self.__test_input(scores[key], int):
				scores[key] = raw_input("Not a number in location: %i. Please enter correct score: " % (int(key)+1))

	def get_players(self,players):
		self.all_players = []
		for player_num in range(1,int(players)+1):
			self.all_players.append(Player(raw_input("What is the name for player %i?: " % player_num)))
		return self.all_players

	def get_scores(self):
		self.score_dictionary = {}
		for player in self.all_players:
			scores = raw_input("What are the scores for player %s?: " % player.name )
			scores = scores.strip("\n").strip("[").strip("]").split(",")
			self.__test_score_input(scores,self.course.holes)
			scores = player.scores(scores)
			score = player.score_total(scores)
			self.score_dictionary[player.name] = score
		return self.score_dictionary

	def print_leaderboard(self):
		import operator 

		print "\nLeaderBoard:"

		sorted_scores = sorted(self.score_dictionary.items(), key=operator.itemgetter(1))
		for count,each in enumerate(sorted_scores):
			print "%i - %s, Overall Score: %s, %i" % (count+1, each[0], each[1], int(each[1]) - self.course.par_total)				

app = AppInterface()





