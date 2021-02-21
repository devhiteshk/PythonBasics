# Friday: Creating blackjack and weekly challenges

from random import randint


# Creating game class


class Blackjack(object):
    def __init__(self):
        self.deck = []
        self.suit = ("Spades", "Hearts", "Diamonds", "Clubs")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

        # # create a method that creates a deck of 52 cards, each card
        # should be a tuple with a value and suit

    def makeDeck(self):
        for suit in self.suit:
            for value in self.values:
                self.deck.append((value, suit))

    # method to pop a card from deck using a random index value

    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


# print(game.deck)          # remove this line after it prints out correctly
# print(game.pullCard(), len(game.deck))


# Creating a player class for the dealer and players objects

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.currency = [1000000]

    # take in a tuple and append it to the hand

    def addCards(self, card):
        self.hand.append(card)

    # if not dealer's turn then only show one of his cards, otherwise show all

    def showHands(self, dealer_start=True):
        print("\n{}".format(self.name))
        print("============")
        for i in range(len(self.hand)):
            if self.name == "Dealer" and i == 0 and dealer_start:
                print("- of -")  # hide first card
            else:
                card = self.hand[i]
                print("{} of {}".format(card[0], card[1]))
            print("Total = {}".format(self.calcHand(dealer_start)))

    # if not dealer's turn then only give back total of second card
    def calcHand(self, dealer_start=True):
        total = 0
        aces = 0  # calculate aces afterwards
        card_values = {1: 1., 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10,
                       "A": 11}
        if self.name == "Dealer" and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]

        for card in self.hand:
            if card[0] == "A":
                aces += 1

            else:
                total += card_values[card[0]]

        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11

        return total


cho = 0
while cho != "quit":
    cho = input("What you want to do \n1. Play\n2. quit:\t").lower()
    if cho == "play":

            game = Blackjack()
            game.makeDeck()
            name = input("What is your name? ")
            player = Player(name)
            dealer = Player("Dealer")
            tot = input("how much money you have:")
            player.currency = int(tot)
            amt = input("How much money you want to wage:")
            wage = int(amt)
            print("now you have {} in total".format(player.currency-wage))
            # print(player.name, dealer.name)

            # Add two cards to dealer and player hand
            for i in range(2):
                player.addCards(game.pullCard())
                dealer.addCards(game.pullCard())
                # print("Player Hand: {} \nDealer Hand: {}".format(player.hand, dealer.hand))
            player.showHands()
            dealer.showHands()


            player_bust = False
            # variable to keep track of player going over 21

            while input("Would you like to stay or hit?").lower() != "stay":
                # pull card and put into player's hand
                player.addCards(game.pullCard())
                # show both hands using method
                player.showHands()
                dealer.showHands()
                # check if over 21
                if player.calcHand() > 21:
                    player_bust = True      # player busted, keep track for later
                    # print("You lose!")      # remove after running correctly
                    break                     # break out of the player's loop

            # handling the dealer's turn, only run if player didn't bust

            dealer_bust = False
            if not player_bust:
                while dealer.calcHand(False) < 17:          # pass False to calculate all cards
                    # pull card and put into player's hand
                    dealer.addCards(game.pullCard())
                    # check if over 21
                    if dealer.calcHand(False) > 21:
                        # pass False to calculate all cards
                        dealer_bust = True
                        print("You win!")           # remove after running correctly
                        player.currency += wage
                        print("and got Rs{} new total is {}".format(2*wage, player.currency))
                        break           # break out of the dealer's loop

            # show both hands using method
            player.showHands()
            dealer.showHands(False)

            # pass False to calculate and show all cards, even when there are
            # calculate a winner

            if player_bust:
                print("You busted, better luck next time!")
                print("new total is Rs.{}".format(player.currency))

            elif dealer_bust:
                print("The dealer busted, you win!")
                player.currency += wage
                print("and got Rs{} new total is {}".format(2 * wage, player.currency))

            elif dealer.calcHand(False) > player.calcHand():
                print("Dealer has higher cards, you lose!")
                player.currency -= wage
                print("and lost Rs{} new total is {}".format(wage, player.currency))

            elif dealer.calcHand(False) < player.calcHand():
                print("You beat the dealer! Congrats!")
                player.currency += wage
                print("and got Rs{} new total is {}".format(2 * wage, player.currency))

            else:
                print("You pushed, no one wins!")

    elif cho == "quit":
        print("Thanks for using our software")

    else:
        print("This is not an option try again!")
