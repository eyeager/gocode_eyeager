'''

BlackJack Game

User Stories:

1) User can play the blackjack game in terminal against the dealer
2) Dealer automatically plays his hand with a fixed algorithm (If it's 16 or below they hit, if it's above 16, they stay)
3) User can play the blackjack game repeatedly
4) User can choose to hit or stay
5) User can see what cards they have been dealt
6) User can only see one dealer card, not the bottom card

Tips:
1) Aces can count as an eleven or a one - but it only counts as a one if your score is over 21
2) Research random.shuffle()
3) You are not allowed to code until you design your program!
4) Research __radd__ - it is a built-in method in Python

Extension:
1) Multiple users can play blackjack game in terminal in a turn-based game
2) Consider using the stack data structure
3) User can bet dollar amounts in the blackjack game


'''
import random

suits = ('c','s','h','d')
ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

class Card:
    def __init__(self,suit,rank):
        self.rank = rank
        self.each_card = rank + suit
        self.card_value = self.value()

    # Needed to pop()
    def __str__(self):
        return self.each_card

    # Needed to return card to card_deck
    def __repr__(self):
        return self.each_card

    # I'm not sure how to use this... when i'm trying to add an array of cards
    #def __radd__(self,other):
    #    return self.card_value + other.card_value

    # Returns and saves the card value. Need to figure out what to do with 'A'
    def value(self,ace_bust = False):
        if self.rank in 'J' 'Q' 'K':
            card_value = 10
        elif self.rank == 'A':
            if ace_bust:
                card_value = 1
            else:
                card_value = 11
        else:
            card_value = int(self.rank)

        return card_value


class Deck:
    def __init__(self):
        self.card_deck = [Card(x,y) for x in suits for y in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.card_deck)
        return self.card_deck

    def one(self):
        "get one card"
        if len(self.card_deck) == 0:
            print "ERROR: No cards left in deck."
        else:
            return self.card_deck.pop()


class Player(object):
    def __init__(self,name,bet = 0):
        self.name = name
        self.bet = bet
        self.cards = []

    def __str__(self):
        "optional"
        return "Player: " + self.name

    def __lt__(self,other):
        if self.hand_value < other.hand_value:
            return True
        else:
            return False

    def __eq__(self,other):
        if self.hand_value == other.hand_value:
            return True
        else:
            return False

    def get(self,card):
        "adds a card to the users hand"
        self.cards.append(card)
        self.hand()

    def choose(self):
        "ui, ask user to hit or stand"
        hit_or_stay = raw_input("Player: %s  Pick an option (stay/hit): " % self.name).lower()

        while hit_or_stay != "hit" and hit_or_stay != "stay":
            hit_or_stay = raw_input("Not a valid option. Pick an option (stay/hit): ").lower()

        return hit_or_stay

    def hand(self):
        "calculate the number value of the users hand"
        aces = []
        self.hand_value = 0
        for card in self.cards:
            if card.rank != "A":
                self.hand_value += card.card_value
            else:
                aces.append(card)

        for card in aces:
            if self.hand_value > 10:
                self.hand_value += card.value(True)
            else:
                self.hand_value += card.card_value

        return self.hand_value

    def bust(self):
        "did the user bust"
        if self.hand_value > 21:
            return True
        else:
            return False

    def won(self):
        "do they have 21"
        if self.hand_value == 21:
            return True
        else:
            return False

class Dealer(Player):
    def __init__(self,name):
       Player.__init__(self,name)

    def __str__(self):
        "optional"
        return "Dealer: " + self.name

    def __repr__(self):
        return "Dealer"

    def choose(self):
        "computer logic to decide to hit or stay"
        if self.hand_value < 16:
            return "hit"
        else:
            return "stay"
        
class Game:
    def __init__(self):
        self.card_deck = Deck()

    def __game_setup__(self):
        self.all_players = []
        print "\nOkay, let's setup our game."
        self.game_dealer = Dealer("Jimmy")
        player_count = self.__test_int__(raw_input("How many players in this game?: "))

        for count in range(1,int(player_count)+1):
            player_name = raw_input("Player %i name: " % count)
            player_bet = self.__test_int__(raw_input("How much would Player %i like to bet? (5-50): " % count))

            while player_bet < 5 or player_bet > 50:
                player_bet = self.__test_int__(raw_input("Bet must be between $5-50: "))

            self.all_players.append(Player(player_name, player_bet))

        self.deal()
        self.deal()
        
        print "********* DEALING *********"
        self.print_table()

    def __test_int__(self,number):
        while type(number) != int:
            try:
                number = int(number)
            except:
                number = raw_input("Invalid input. Must be a number: ")
        return number

    def print_table(self):
        "helper method to print out all the players hands"
        for player in self.all_players:
            print str(player) + "\n" + ", ".join([str(x) for x in player.cards])

        print str(self.game_dealer) + "\n--, " + ", ".join([str(x) for x in self.game_dealer.cards[1:]])

    
    def deal(self):
        "deal to all players"
        for player in self.all_players:
            player.get(self.card_deck.one())

        self.game_dealer.get(self.card_deck.one())    

    # This is ugly... Figure this one out
    def final_scores(self):
        winning_count = 0

        print "********* Game over *********"
        self.print_table()
        print

        for player in self.all_players:
            if player.bust():
                print "%s\nScore: %i\nBusted and lost: $%i\n" % (str(player), player.hand_value, player.bet)
            elif player.won():
                print "%s\nScore: %i\nHas Blackjack! and won: $%.2f\n" % (str(player), player.hand_value, player.bet * 2.5)
            elif player.hand_value > self.game_dealer.hand_value and self.game_dealer.bust() == False or self.game_dealer.bust() == True:
                print "%s\nScore: %i\nBeat the dealer and won: $%i\n" % (str(player), player.hand_value, player.bet * 2)
                winning_count += 1
            elif player.hand_value == self.game_dealer.hand_value:
                print "%s\nScore: %i\nTied the dealer and won: $%i\n" % (str(player), player.hand_value, player.bet)
                winning_count += 1
            elif player.hand_value < self.game_dealer.hand_value:
                print "%s\nScore: %i\nLost to the dealer and lost: $%i\n" % (str(player), player.hand_value, player.bet)

        if self.game_dealer.bust() == True:
            print str(self.game_dealer) + " busted with the score of " + str(self.game_dealer.hand_value)
        elif winning_count == 0:
            print str(self.game_dealer) + " wins all with score of " + str(self.game_dealer.hand_value)
        else:
            print str(self.game_dealer) + " : " + str(self.game_dealer.hand_value)


    def play(self):
        "top level, manages the game"
        play_loop = None
        print "********* Most Awesomest Blackjack EEEEVER *********"

        while play_loop != "n":
            self.__game_setup__()

            # Player loop
            for player in self.all_players:
                while player.choose() == "hit":
                    player.get(self.card_deck.one())
                    print "********* DEALING *********"
                    self.print_table()

                    if player.won() == True:
                        print str(player) + " has BlackJack!"
                        break
                    elif player.bust() == True:
                        print str(player) + " has busted. Loser."
                        break

            # Dealer loop
            while self.game_dealer.choose() == "hit":
                self.game_dealer.get(self.card_deck.one())

            self.final_scores()

            play_loop = (raw_input("\nWould you like to play again? (y/n): ")).lower()

        print "\nThanks for playing.\n"

new_game = Game()
new_game.play()

    
