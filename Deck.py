from Card import Card
import random
#Deck object is a standard card of 52 decks. 
#Contains the methods get deck which returns the deck, print_deck which prints the deck in the terminal.
#It also contains shuffle, which randomly mixes up the cards for playing
#Lastly, it contains deal_cards which will deal the top card of the deck. 
class Deck:
    def __init__(self):
        suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.fulldeck = []
        for values in value:
            for suits in suit:
                c = Card(suits, values)
                self.fulldeck.append(c)
   
    def get_deck(self):
        return self.fulldeck
    
    def print_deck(self):
      for c in self.fulldeck:
          print(c.get_name())
    #shuffles the deck (seven times) by splitting it unevenly (to insure an imperfect shuffle) and putting each section into a different list
    #then loops through each deck and takes the card at that index and adds it into the shuffled deck (list). there is a 50% chance that deck1 is used or deck2 is used for this
    #the different counters are to insure there is no out of bounds error. 
    #eventually if one deck runs out before the other, it will just place the rest of the deck that still has cards into the shuffled deck
    #then the original deck will be set to the shuffled deck and the process will restart
    def shuffle(self):
        new_deck = self.fulldeck.copy()
        deck1 = []
        deck2 = []
        # print(type(self.deck))
        
        for cards in range(7):
            deck1 = new_deck[:30]
            deck2 = new_deck[30:]
            shuffled = []
            final_shuffled = []
            
            i = 0 #counter for deck1
            j = 0 #counter for deck2
            for cards in range(52):
                if(i < len(deck1) and j < len(deck2)):
                    if(random.random() < 0.5):
                        shuffled.append(deck1[i])
                        i+=1
                    else:
                        shuffled.append(deck2[j])
                        j+=1
                #if either deck1 or deck2 is empty
                elif(i < len(deck1)): 
                    shuffled.append(deck1[i])
                    i+=1
                elif(j < len(deck2)):
                    shuffled.append(deck2[j])
                    j+=1
            new_deck = shuffled
        for x in range(52):
            final_shuffled.extend(self.fulldeck[x].get_name())
            self.fulldeck = shuffled
        self.fulldeck.reverse()
    #removes the top card from a players deck and returns it
    def deal_cards(self):
        if(self.fulldeck != None):
            return self.fulldeck.pop(0)
        return None
                
            
# d1 = Deck()
# # # d1.print_deck()
# # # d1.print_deck()
# d1.shuffle()
# print("")
# d1.print_deck()
# # print("")


