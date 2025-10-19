from Card import Card
from Deck import Deck
#The Hand class is a players hand in a poker game, in which a hand contains 5 cards
#Hand consists of add_card which adds a card to the hand in descending order, 
#rank, which returns a number for each hand rank in poker, 
#and compare which compares these ranks to determine a winner by returning either 1(object calling the method wins), -1(other object wins), or 0(tie)
class Hand: 
    def __init__(self):
        self.fullhand = []
        # d = Deck()
        # d.shuffle()
        # self.fullhand.append(d.deal_cards(5))
        
    def get_hand(self):
        return self.fullhand
    
    def print_hand(self):
        for c in self.fullhand:
            print(c)
    #adds a card to a players hand in descending order.
    #if the hand has no cards, it will just add the card
    #otherwise, it will loop through the hand and if the cards value is greater than the cards value at that index, the card will be placed there
    def add_card(self, card):

        if(len(self.fullhand) == 0):
            self.fullhand.append(card)
            return

        for i in range(len(self.fullhand)):
            if card.get_value() >= self.fullhand[i].get_value():
                self.fullhand.insert(i, card)
                return
        self.fullhand.append(card)
    
    #Assigns an integer to each poker rank
    def rank(self):

        for i in range(len(self.fullhand)):
            #royal flush
            #if the first card of the hand is the highest, it will check all the other cards to make sure its in descending order by one and checks that 
            #all the suits are the same
            if(self.fullhand[0].get_value == 14):
                if((self.fullhand[0].get_value()+1) == self.fullhand[1].get_value() and (self.fullhand[0].get_suit() == self.fullhand[1].get_suit())):
                    if((self.fullhand[1].get_value()+1) == self.fullhand[2].get_value and (self.fullhand[1].get_suit() == self.fullhand[2].get_suit())):
                        if((self.fullhand[2].get_value()+1) == self.fullhand[3].get_value and (self.fullhand[2].get_suit() == self.fullhand[3].get_suit())):
                            if((self.fullhand[3].get_value()+1) == self.fullhand[4].get_value and (self.fullhand[3].get_suit() == self.fullhand[4].get_suit())):
                                return 9
            #straight flush
            #if the top card is the highest (less than royal flush cards) it will check to make sure the other cards in the hand are in descending order by one
            # and checks that all the suits are the same
            if(self.fullhand[0].get_value == 11):
                if((self.fullhand[0].get_value()+1) == self.fullhand[1].get_value() and (self.fullhand[0].get_suit() == self.fullhand[1].get_suit())):
                    if((self.fullhand[1].get_value()+1) == self.fullhand[2].get_value and (self.fullhand[1].get_suit() == self.fullhand[2].get_suit())):
                        if((self.fullhand[2].get_value()+1) == self.fullhand[3].get_value and (self.fullhand[2].get_suit() == self.fullhand[3].get_suit())):
                            if((self.fullhand[3].get_value()+1) == self.fullhand[4].get_value and (self.fullhand[3].get_suit() == self.fullhand[4].get_suit())):
                                return 8
            #four of a kind aaaab/baaaa
            #checks to see if there are four of the same cards in a row
            if(self.fullhand[0].get_value() == self.fullhand[1].get_value() == self.fullhand[2].get_value() == self.fullhand[3].get_value()) or (
                self.fullhand[1].get_value() == self.fullhand[2].get_value() == self.fullhand[3].get_value() == self.fullhand[4].get_value()):
                return 7
            #full house aaabb/bbaaa
            #checks to see that there are three of the same cards in a row and then two of the same cards in a row
            #or the other way around
            if(self.fullhand[0].get_value() == self.fullhand[1].get_value() == self.fullhand[2].get_value() 
               and self.fullhand[3].get_value() == self.fullhand[4].get_value()) or (
                   self.fullhand[0].get_value() == self.fullhand[1].get_value() 
                   and self.fullhand[2].get_value() == self.fullhand[3].get_value() == self.fullhand[4].get_value()):
                return 6
            #flush 
            #Checks that all of the suits are the same
            if(self.fullhand[0].get_suit() == self.fullhand[1].get_suit()):
                if(self.fullhand[1].get_suit() == self.fullhand[2].get_suit()):
                    if(self.fullhand[2].get_suit() == self.fullhand[3].get_suit()):
                        if(self.fullhand[3].get_suit() == self.fullhand[4].get_suit()):
                            return 5
            #straight
            #Checks to see that the cards go in descending order by one 
            if((self.fullhand[0].get_value()+1) == self.fullhand[1].get_value()):
                if((self.fullhand[1].get_value()+1) == self.fullhand[2].get_value):
                    if((self.fullhand[2].get_value()+1) == self.fullhand[3].get_value):
                        if((self.fullhand[3].get_value()+1) == self.fullhand[4].get_value):
                            return 4
            #ace leading straight
            #Ace playing down, checks to see all the cards go in descending order by one
            if(self.fullhand[0] == 14):
                if(self.fullhand[1] == 2):
                    if(self.fullhand[2] == 3):
                        if(self.fullhand[3] == 4):
                            if(self.fullhand[4] == 5):
                                return 4
            #three of a kind aaabc/cbaaa
            #Checks that there are three of the same cards in a row and that the other two cards are different
            if(self.fullhand[0].get_value() == self.fullhand[1].get_value() == self.fullhand[2].get_value()
               and self.fullhand[3].get_value()!= self.fullhand[4].get_value()) or(
                   self.fullhand[0].get_value() != self.fullhand[1].get_value()
                   and self.fullhand[2].get_value() == self.fullhand[3].get_value() == self.fullhand[4].get_value()):
                return 3
            #two pair aabbc/caabb
            #checks that there are two cards in a row that are the same and then checks for another two cards in a row that are the same
            #making the counter = 2
            count = 0
            for i in range(len(self.fullhand)):
                if(self.fullhand[i].get_value() == self.fullhand[i-1].get_value()):
                    count+=1
            if(count == 2):
                return 2
            #one pair aabcd/abbcd/abccd/abcdd
            #Checks that there is one pair in the hand, counter = 1 and that all the other cards are different from the pair
            count = 0
            for i in range(len(self.fullhand)):
                if(self.fullhand[i].get_value() == self.fullhand[i-1].get_value()):
                    count+=1
            if(count == 1):
                return 1
            #high card 
            #finds the biggest card in the hand (the first card)
            if(self.fullhand[0].get_value() != self.fullhand[1].get_value() != self.fullhand[2].get_value() != self.fullhand[3].get_value() != self.fullhand[4].get_value()):
                return 0
    
    #compare method that compares the ranks of two hands to determine a winner and also checks for ties
    #object that calls the method wins - returns 1
    #other_hand wins - returns -1
    #tie - returns 0
    def compare(self, other_hand):
        #a situation where there is no tie, simply compares the ranks and the biggest one is the winner
        if(self.rank() > other_hand.rank()):
            return 1
        if(other_hand.rank() > self.rank()):
            return -1
        
        #if ranks tie
        if(self.rank() == other_hand.rank()):

            #royal flush 
            if(self.rank() == 9 and other_hand.rank() == 9):
                return 0
            
            #straight flush and straight
            #checks which hand has the highest leading card and returns a winner based on that 
            if(self.rank() == 8 and other_hand.rank() == 8) or (
                self.rank() == 4 and other_hand.rank() == 4):
                if(self.fullhand[0] > other_hand.fullhand[0]):
                    return 1
                elif(other_hand.fullhand[0] > self.fullhand[0]):
                    return -1
                else:
                    return 0
                
            #high card and flush
            #Compares the highest cards between the two hands if they are both high card or if they are both flush
            if(self.rank() == 0 and other_hand.rank() == 0) or (
                self.rank() == 5 and other_hand.rank() == 5):
                for i in range(len(self.fullhand)):
                    highest1 = self.fullhand[i].get_value()
                    highest2 = other_hand.fullhand[i].get_value()
                    if(highest1 > highest2):
                        return 1
                    elif(highest2 > highest1):
                        return -1
                else:
                    return 0
            
            #checks when both have one pair
            #Checks which pair is the largest 
            if(self.rank() == 1 and other_hand.rank() == 1):
                pair1_value = None
                pair2_value = None
                for i in range(len(self.fullhand)-1):
                    if(self.fullhand[i].get_value() == self.fullhand[i+1].get_value()):
                        pair1_value = self.fullhand[i].get_value()
                for i in range (len(other_hand.fullhand)-1):
                    if(other_hand.fullhand[i].get_value() == other_hand.fullhand[i+1].get_value()):
                        pair2_value = other_hand.fullhand[i].get_value()
                if(pair1_value > pair2_value):
                    return 1
                elif(pair2_value > pair1_value):
                    return -1
                
                #if the pairs tie
                #the remaining cards will be checked and a winner will be determined based on which card is the highest
                else:
                    remaining1 = []
                    remaining2 = []
                    for card in self.fullhand:
                        if(card.get_value() != pair1_value):
                            remaining1.append(card.get_value())
                    for card in other_hand.fullhand:
                        if(card.get_value() != pair2_value):
                            remaining2.append(card.get_value())
                    remaining1.sort(reverse = True)
                    remaining2.sort(reverse = True)

                    if(remaining1[0] > remaining2[0]):
                        return 1
                    if(remaining2[0] > remaining1[0]):
                        return -1
                    else:
                        return 0
                    
            #checks when both are three of a kind
            #will check which card triplet is the highest
            if(self.rank() == 3 and other_hand.rank() == 3):
                triple1_value = None
                triple2_value = None

                for i in range (len(self.fullhand)-1):
                    if(self.fullhand[i].get_value() == self.fullhand[i+1].get_value() == self.fullhand[i+2].get_value):
                        triple1_value = self.fullhand[i].get_value()
                for i in range (len(other_hand)-1):
                    if(other_hand.fullhand[i].get_value() == other_hand.fullhand[i+1].get_value() == other_hand.fullhand[i+2].get_value):
                        triple2_value = other_hand.fullhand[i].get_value()
                if(triple1_value > triple2_value):
                    return 1
                elif(triple2_value > triple1_value):
                    return -1
                
            #checks when both are four of a kind
            #checks which card quad is the highest
            if(self.rank() == 7 and other_hand.rank() == 7):
                quad1_value = None
                quad2_value = None

                for i in range (len(self.fullhand)-1):
                    if(self.fullhand[i].get_value() == self.fullhand[i+1].get_value() == self.fullhand[i+2].get_value  == self.fullhand[i+3].get_value):
                        quad1_value = self.fullhand[i].get_value()
                for i in range (len(other_hand)-1):
                    if(other_hand.fullhand[i].get_value() == other_hand.fullhand[i+1].get_value() == other_hand.fullhand[i+2].get_value == other_hand[i+3].get_value):
                        quad2_value = other_hand.fullhand[i].get_value()
                if(quad1_value > quad2_value):
                    return 1
                elif(quad2_value > quad1_value):
                    return -1
                else:
                    return 0
            
            #checks when both are full houses
            #compares the highest 3 of a kind cards for the highest one
            if(self.rank() == 6 and other_hand.rank() == 6):
                fullhouse1_value = None
                fullhouse2_value = None

                for i in range (len(self.fullhand)-1):
                    if(self.fullhand[i].get_value() == self.fullhand[i+1].get_value() == self.fullhand[i+2].get_value):
                        fullhouse1_value = self.fullhand[i].get_value()
                for i in range (len(other_hand)-1):
                    if(other_hand.fullhand[i].get_value() == other_hand.fullhand[i+1].get_value() == other_hand.fullhand[i+2].get_value):
                        fullhouse2_value = other_hand.fullhand[i].get_value()
                if(fullhouse1_value > fullhouse2_value):
                    return 1
                elif(fullhouse2_value > fullhouse1_value):
                    return -1
                else:
                    return 0
            
            #checks when both have two pairs
            #compares the two highest pairs from each hand
            if(self.rank() == 2 and other_hand.rank() == 2):
                highest_pair1 = None
                highest_pair2 = None

                for i in range (len(self.fullhand)-1):
                    if(self.fullhand[i].get_value() == self.fullhand[i+1].get_value()):
                        highest_pair1 = self.fullhand[i].get_value()
                for i in range (len(other_hand)-1):
                    if(other_hand.fullhand[i].get_value() == other_hand.fullhand[i+1].get_value()):
                        highest_pair2 = other_hand.fullhand[i]
                if(highest_pair1 > highest_pair2):
                    return 1
                elif(highest_pair2 > highest_pair1):
                    return -1
                
                #checks the second pair if highest pair is tied
                elif(highest_pair1 == highest_pair2):
                    
                    lowest_pair1 =[]
                    lowest_pair2 = []
                    for card in self.fullhand:
                        if(card.get_value() != pair1_value):
                            lowest_pair1.append(card.get_value())
                    for card in other_hand.fullhand:
                        if(card.get_value() != pair2_value):
                            lowest_pair2.append(card.get_value())
                    lowest_pair1.sort(reverse = True)
                    lowest_pair2.sort(reverse = True)
                    if(lowest_pair1[0].get_value() > lowest_pair2[0].get_value()):
                        return 1
                    elif(lowest_pair2[0].get_value() > lowest_pair1[0].get_value()):
                        return -1
                    
                    #checks the single card if both pairs are tied
                else:
                    if(self.fullhand[4].get_value > other_hand.fullhand[4].get_value()):
                        return 1
                    if(self.fullhand[4].get_value < other_hand.fullhand[4].get_value()):
                        return -1
                    else:
                        return 0
        else:
            return 0
        

# deck = Deck()   
# deck.shuffle()        
# h1 = Hand()

# h1.add_card(deck.deal_cards())
# h1.add_card(deck.deal_cards())
# h1.add_card(deck.deal_cards())
# h1.add_card(deck.deal_cards())
# h1.add_card(deck.deal_cards())
# h1.print_hand()
# print(h1.rank())

# # h1.print_hand()
# h2 = Hand()

# print("")
# # h2.print_hand()
# h2.add_card(deck.deal_cards())
# h2.add_card(deck.deal_cards())
# h2.add_card(deck.deal_cards())
# h2.add_card(deck.deal_cards())
# h2.add_card(deck.deal_cards())
# h2.print_hand()
# print(h2.rank())

# print("")
# print(h1.compare(h2))