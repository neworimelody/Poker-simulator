from Card import Card
from Deck import Deck
from Hand import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


#creates a list of hands and deals shuffled cards to that hand. then obtains winner index that will later be used to determine where the winner text shows up
#displays the game by pasting the cards in the hand together and then pasting the hands together. 
#converts int ranks to strings to display on the game image 
d = Deck()
d.shuffle()
h1 = Hand()
h2 = Hand()
h3 = Hand()
h4 = Hand()
poker_game = []
poker_game.append(h1)
poker_game.append(h2)
poker_game.append(h3)
poker_game.append(h4)

#deals 5 cards to each hand 
for i in range(5):
        h1.add_card(d.deal_cards())
        h2.add_card(d.deal_cards())
        h3.add_card(d.deal_cards())
        h4.add_card(d.deal_cards())
def win():
        winner_index = 0 #assumes player 0 is the winner for now
        for i in range(1, 4): #compares player 0 with players 1, 2, and 3
            result = poker_game[winner_index].compare(poker_game[i])
        #if player 0 looses, a new winner will be determined and will restart the comparing process
            if(result == -1):
                winner_index = i
        return winner_index
#gets the each card file for each hand respectively 
h1_im1 = Image.open(h1.fullhand[0].image_file_name())
h1_im2 = Image.open(h1.fullhand[1].image_file_name())
h1_im3 = Image.open(h1.fullhand[2].image_file_name())
h1_im4 = Image.open(h1.fullhand[3].image_file_name())
h1_im5 = Image.open(h1.fullhand[4].image_file_name())

h2_im1 = Image.open(h2.fullhand[0].image_file_name())
h2_im2 = Image.open(h2.fullhand[1].image_file_name())
h2_im3 = Image.open(h2.fullhand[2].image_file_name())
h2_im4 = Image.open(h2.fullhand[3].image_file_name())
h2_im5 = Image.open(h2.fullhand[4].image_file_name())

h3_im1 = Image.open(h3.fullhand[0].image_file_name())
h3_im2 = Image.open(h3.fullhand[1].image_file_name())
h3_im3 = Image.open(h3.fullhand[2].image_file_name())
h3_im4 = Image.open(h3.fullhand[3].image_file_name())
h3_im5 = Image.open(h3.fullhand[4].image_file_name())

h4_im1 = Image.open(h4.fullhand[0].image_file_name())
h4_im2 = Image.open(h4.fullhand[1].image_file_name())
h4_im3 = Image.open(h4.fullhand[2].image_file_name())
h4_im4 = Image.open(h4.fullhand[3].image_file_name())
h4_im5 = Image.open(h4.fullhand[4].image_file_name())

#merges the cards in each hand together to display hand and generates a blank card at the end for labels
def merge_cards(im1, im2, im3, im4, im5):
        width = 200
        total_width = im1.width + im2.width + im3.width + im4.width + im5.width + width
        im = Image.new('RGB', (total_width, im1.height), color='black')
        im.paste(im1, (0, 0))
        im.paste(im2, (im1.width, 0))
        im.paste(im3, (im1.width + im2.width, 0))
        im.paste(im4, (im1.width + + im2.width + im3.width, 0))
        im.paste(im5, (im1.width + + im2.width + im3.width + im4.width, 0))
        return im

#creates rows, each row is a different hand
hand_image1 = merge_cards(h1_im1, h1_im2, h1_im3, h1_im4, h1_im5)
hand_image2 = merge_cards(h2_im1, h2_im2, h2_im3, h2_im4, h2_im5)
hand_image3 = merge_cards(h3_im1, h3_im2, h3_im3, h3_im4, h3_im5)
hand_image4 = merge_cards(h4_im1, h4_im2, h4_im3, h4_im4, h4_im5)

#merges the hands together vertically to create full game layout    
def merge_hands(im1, im2, im3, im4):
        im = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height + im4.height))
        im.paste(im1, (0, 0))
        im.paste(im2, (0, im1.height))
        im.paste(im3, (0, im1.height + im2.height))
        im.paste(im4, (0, im1.height + im2.height + im3.height))
        return im
#creates the image that comprises of all the hands together 
game_image = merge_hands(hand_image1, hand_image2, hand_image3, hand_image4)

#gets the rank of each hand   
ranks = [h1.rank(), h2.rank(), h3.rank(), h4.rank()]
rank_names = ["High Card", "One Pair", "Two Pair", "Three of a Kind",
              "Straight", "Flush", "Full House", "Four of a Kind", 
              "Straight Flush", "Royal Flush"]
labels = []
winner_index = win()

for i in range(4):
        #sets text equal to the string version of rank (if rank is 0, rank_names would be high card because rank_names at index 0 is high card)
        text = rank_names[ranks[i]]
        if(winner_index == i):
            text += "- Winner!"
        labels.append(text)

#adds text to the blank cards beside the hands
font = ImageFont.truetype('/Users/cindy/Documents/Honors Data Structures /Python/PokerSimulator/Montserrat/Montserrat-VariableFont_wght.ttf', 15)
final_image = ImageDraw.Draw(game_image)
for i in range(4):
    x = hand_image1.width - 150
    y = i * hand_image1.height + 50
    final_image.text((x, y), labels[i], fill = 'white', font = font)
game_image.show()