
'''
Build a German translator

A simple German sentence has this structure

(1) Subject (2) Conjugated Verb (3) other stuff.

Ex: I have an apple. -> Ich habe ein Apfel.
Ex: You have an apple. -> Du hast ein Apfel.

Using the data structures given build a Engish to German translator

'''

personal_pronouns = {"I":"Ich",
                     "You":"Du",
                     "He": "Er",
                     "She": "Sie"}

haben_conjugated = {"Ich":"habe",
                    "Du":"hast",
                    "Er":"hat",
                    "Sie":"hat"}

article = {"an" : "einen",
           "a"  : "einen"}

nouns = {"apple":"Apfel",
         "coffee":"Kaffee"}

def english_to_german(sentence):
	sentence = sentence[:-1]
	words = sentence.split()
	translation = ""

	for word in words:
		if words.index(word) == 0:
			translation += personal_pronouns[word] + " " + haben_conjugated[personal_pronouns[word]]
		if words.index(word) == 2:
			translation += " " + article[word]
		if words.index(word) == 3:
			translation += " " + nouns[word] + "."
	return translation

	 print " ".join([personal_pronouns[words.index(word)]])

assert english_to_german("I have an apple.") == "Ich habe einen Apfel."
assert english_to_german("You have a coffee.") == "Du hast einen Kaffee."
