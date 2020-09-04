class Deck:

    cards = {}

    # The deck is created by filling the dictionary with each of the 81 cards to complete
    # the deck via a comprehension that assigns the key of each card to be a unique four 
    # digit code and the value is the card object itself.
    def __init__(self):
        images = {}

        for n in range(1,4):
            for s in range(1,4):
                for f in range(1,4):
                    for c in range(1,4):
                        self.cards[str(n) + str(s) + str(f) + str(c)] = Card(n,s,f,c, images[str(n) + str(s) + str(f) + str(c)])

class Card:

    def __init__(self, num, shape, fill, color, image):
        shapes = {1 : "Diamond", 2 : "Oval", 3 : "Squiggle"}
        fills = {1 : "Empty", 2 : "Full", 3 : "Striped"}
        colors = {1 : "Red", 2 : "Green", 3 : "Purple"}

        self.num = num
        self.shape = shapes[shape]
        self.fill = fills[fill]
        self.color = colors[color]


deck = Deck()
print(deck.cards['1111'].shape)