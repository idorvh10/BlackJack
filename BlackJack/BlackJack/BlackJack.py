#possible bugs in original project solution:
#1. global chips (won't reset between rounds)
#2. out of deck scenerio
#3. play again part will stop the game with invalid input

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
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        if self.value > 21 and self.aces:
            self.value -= 10
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

    print(f"Currently you have {player_chips.total} chips.")

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?\n"))
            print("")
        except:
            print("\nSorry please provide a positive integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            elif chips.bet < 0:
                print("Sorry please provide a positive integer")
            else:
                break

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):

    global playing
    
    while True:

        x = input("Hit or stand? Type h or s\n")
        print("")
        if x.lower() == 'h':
            hit(deck,hand)
        elif x.lower() == 's':
            print ("Player stands, Dealer's turn")
            playing = False
        else:
            print ("I didn't understand that. Type 'h' to hit or 's' to stand")
            continue
        break

def show_some(player,dealer):

    print("Dealer's hand:")
    print("First card hidden")
    print(dealer.cards[1])

    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print("")

def show_all(player,dealer):

    print("Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print(f"Dealer's total value is: {dealer.value}")

    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print(f"Player's total value is: {player.value}\n")

def player_busts(chips):
    print("Player Busted! Dealer Wins")
    chips.lose_bet()

def player_wins(chips):
    print("Player Wins!")
    chips.lose_bet()

def dealer_busts(chips):
    print("Dealer Busted! Player Wins")
    chips.lose_bet()

def dealer_wins(chips):
    print("Dealer Wins")
    chips.lose_bet()

def push():
    print("It's a Tie!")


while True:

    print("Welcome to BlackJack!")
        
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    hit(deck,player_hand)
    hit(deck,player_hand)
    dealer_hand = Hand()
    hit(deck,dealer_hand)
    hit(deck,dealer_hand)
    
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
    
    # Inform Player of their chips total
    print(f"You now have {player_chips.total} chips\n")
    
    # Ask to play again
    new_game = input("Would you like to play another hand? y/n\n")
    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
    break