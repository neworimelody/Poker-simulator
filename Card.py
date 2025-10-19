class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        if(self.value > 10):
            if(self.value == 11):
                return f"Jack of {self.suit}"
            elif(self.value == 12):
                return f"Queen of {self.suit}"
            elif(self.value == 13):
                return f"King of {self.suit}"
            elif(self.value == 14):
                return f"Ace of {self.suit}"
        return f"{self.value} of {self.suit}"

    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def get_name(self):
        if(self.value > 10):
            if(self.value == 11):
                return f"Jack of {self.suit}"
            elif(self.value == 12):
                return f"Queen of {self.suit}"
            elif(self.value == 13):
                return f"King of {self.suit}"
            elif(self.value == 14):
                return f"Ace of {self.suit}"
        return f"{self.value} of {self.suit}"
    
    def image_file_name(self):
        file = "/Users/cindy/Documents/Honors Data Structures /Python/PokerSimulator/cards/"
        if(self.suit == "Clubs"):
            if(self.value >= 2 and self.value <= 10):
                return f"{file}{self.value}_of_{self.suit}.png"
            elif(self.value == 11):
                return f"{file}jack_of_clubs.png"
            elif(self.value == 12):
                return f"{file}queen_of_clubs.png"
            elif(self.value == 13):
                return f"{file}king_of_clubs.png"
            elif(self.value == 14):
                return f"{file}ace_of_clubs.png"
        elif(self.suit == "Diamonds"):
            if(self.value >= 2 and self.value <= 10):
                return f"{file}{self.value}_of_{self.suit}.png"
            elif(self.value == 11):
                return f"{file}jack_of_diamonds.png"
            elif(self.value == 12):
                return f"{file}queen_of_diamonds.png"
            elif(self.value == 13):
                return f"{file}king_of_diamonds.png"
            elif(self.value == 14):
                return f"{file}ace_of_diamonds.png"
        elif(self.suit == "Hearts"):
             if(self.value >= 2 and self.value <= 10):
                return f"{file}{self.value}_of_{self.suit}.png"
             elif(self.value == 11):
                return f"{file}jack_of_hearts.png"
             elif(self.value == 12):
                return f"{file}queen_of_hearts.png"
             elif(self.value == 13):
                return f"{file}king_of_hearts.png"
             elif(self.value == 14):
                return f"{file}ace_of_hearts.png"
        else:
            if(self.value >= 2 and self.value <= 10):
                return f"{file}{self.value}_of_{self.suit}.png"
            elif(self.value == 11):
                return f"{file}jack_of_spades.png"
            elif(self.value == 12):
                return f"{file}queen_of_spades.png"
            elif(self.value == 13):
                return f"{file}king_of_spades.png"
            elif(self.value == 14):
                return f"{file}ace_of_spades.png"
# card = Card("Spades", "", 3 )
# print(card.get_name())
