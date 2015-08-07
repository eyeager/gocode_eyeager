# Part A.  Open-book

#1) What is the purpose of object-oriented programming (in english in your own words - one or two sentences)?
# Non-object oriented is based around actions/functions. 
# Object-oriented is based around "object" data types on which you can perform actions and save attributes and reuse in various programs. 

#2) What are the three key features of object-oriented programming?
# Encapsulation: keeps data and functions separate/safe from other scripts/programs
# Polymorphism: Classes can be used in multiple programs for different purposes.
# Inheritance : Classes can inherit each other in order to extend/overwrite Class functions for a specific purpose

#3) Describe the stack data structure.  When would you use it?
# Useful when needing to keep order of the last few actions- such as browser history (or any other kind of action history).
# Stacks in Python are lists utilized as stacks. It's a Last In, First Out(LIFO) list. 
# Only 2 actions can be performed on the stack- appending and popping (adding a last element and removing the last element).

#4) Describe the binary tree data structure.  When would you use it?
# Binary tree is good for quick sort and search. It is a nested object. 
# Each instance of the object contains the parent value and 2 child values. 
# The left value is always less and the right value always more.
# The right and left children can be other instances of the object. 
# The tree continues until the right and left children are integers, not object instances.


# Part B. SQL - Open-book

#1) Write SQL code to create a table called "dogs" with two columns - id (primary key) and name (string)
# CREATE TABLE dogs(id INTEGER PRIMARY KEY, name TEXT);

#2) Write SQL code to insert two new dogs into the database (one called Ernest, the other called Erny)
# INSERT INTO dogs(name) VALUES ("Ernest"),("Erny");

#3) Write SQL code to retrieve all the records in the database with name "Ernest"
# SELECT * FROM dogs WHERE name="Ernest";

# Part C. Open-book

#1) Describe an OOP design for a blackjack game using object-oriented programming
# Hint: What classes would you have?  Would you use inheritance?  What instance variables would you have?  What types of methods would each class have?
# No need to write the code - just describe in english.
# Classes: Card, Deck, Player, Dealer(inherits Player)
# Card: what is on the card, the value of the card, ability to add card values
# Deck: initiates 52 Card object instances, ability to shuffle, ability to deal and remove card from deck
# Player: player name, cards in hand
# Dealer: same as player, ability to make "hit" decision in the background based off of hand and blackjack rules
# 
# UI function loop- keeps the game running, interacts with player to get information on the game: number of players, names, hit/stay choice, 

#2) What does HTTP stand for?  Describe the HTTP request-response cycle where a user clicks on a page to display a blog.
# Hyper Text Transfer Protocol. 
# 1. User types in URL into browser
# 2. Computer resolves the DNS for the domain to an IP, first using internal routes, then using external DNS server set on the router.
# 3. Browser makes TCP connection with server via IP. Browser tries to initiate a hand-shake, server can then connect or refuse.
# 4. After connection is made, server searches for content for the requested page inside the requested domain.
# 5. Server sends content or error if page is not found.
# 6. Browser process content received and displays it in the browser.
# 7. Connection is closed

#3) Regex:
import re

a = "Why so serious: 22034"

regex = r"\w+: (\d{5})"

assert re.search(regex,a).groups()[0] == '22034'
