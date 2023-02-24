#possible bugs in original project solution:
#1. global chips (won't reset between rounds)
#2. out of deck scenerio

from email.message import EmailMessage
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))
    
    def __str__(self):
        deck_print = ""
        for card in self.deck:
            deck_print += '\n' + card.__str__()
        return "The deck has:" + deck_print
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.values += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        if self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):

    global playing
    
    pass