import random

class Card:
    face = {}
    def _init_(self, **kwargs):
        self.face = kwargs


    def getCard(self):
        return self.face

class Deck:
    cards = []
    def getCards(self):
        return self.cards
    def shuffle(self, shuffles=1):
        # for more realism you could pick random indexes and for loop
        # ranges to keep card series as previous like suffle 2 cards
        # under on card or something but not really necessary more human erro
        # simulated

        # random.shuffle(self.cards)
        for shuffle in range(shuffles):
            cards = self.cards
            if len(cards) > 1:
                halfDeck1 = cards[:len(cards)//2]
                halfDeck2 = cards[len(cards)//2:]
                shuffledDeck = []
                halfshuffledGroup1= []
                halfshuffledGroup2= []
                shuffledDeck1 = 0
                shuffledDeck2 = 0
                switch = False

                while (shuffledDeck1 < len(halfDeck1)):
                    variance = random.randint(1, 6)
                    if(variance + shuffledDeck1 > len(halfDeck1)):
                        variance = len(halfDeck1) - shuffledDeck1
                    if(switch): halfshuffledGroup1 += halfDeck1[shuffledDeck1:shuffledDeck1 + variance]
                    else: halfshuffledGroup2 += halfDeck1[shuffledDeck1:shuffledDeck1 + variance]
                    shuffledDeck1 += variance

                    switch = not switch
                switch = False

                while (shuffledDeck2 < len(halfDeck2)):
                    variance = random.randint(1, 6)
                    if(variance + shuffledDeck2 > len(halfDeck1)):
                        variance = len(halfDeck2) - shuffledDeck2
                    if(switch): halfshuffledGroup2 += halfDeck2[shuffledDeck2:shuffledDeck2+variance]
                    else: halfshuffledGroup1 += halfDeck2[shuffledDeck2:shuffledDeck2 +variance]
                    shuffledDeck2 += variance
                    switch = not switch
                shuffledDeck = []
                shuffledDeck+= halfshuffledGroup1 +  halfshuffledGroup2
                self.cards = shuffledDeck



    def drawCards(self,cardsToDraw):
        # this could atomatically add drawn cards to bottom of deck when they are drawn
        drawnCards = self.cards[:cardsToDraw]
        del self.cards[:cardsToDraw]
        self.cards.append(drawnCards)
        return drawnCards

class Deck52(Deck):
    _suit = ['hearts','diamonds','clubs', 'spades' ]
    _rank = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    def _init_(self):
        for suit in self._suit:
            for rank in self._rank:

                self.cards.append(Card(suit=suit, rank=rank))
        self.shuffle(10)


class Game:         #players, deck, dealer, hands, turns, actions(hit, stand) 
    def _init_(self, deck):
        pass

    players = []
    def addPlayer(self, player):
        self.players.append(player)
    
    activePlayers = []

    turns = 0

    actions = []

    
    def addActivePlayer(self, player):
        self.activePlayers.append(player)


class BlackJack(Game):
    def _init_(self, deck):
        self.deck = deck
        self.dealer = Dealer(deck)
        self.players = []
        self.activePlayers = []
        self.turns = 0
        self.actions = ['hit', 'stand']

    def addPlayer(self, player):
        s_PlayerName = input(f'Player {len(self.players) + 1} name: ')
        self.players.append(s_PlayerName)
    

    def deal(self):
        for player in self.activePlayers:
            player.hand = []
            player.hand.append(self.deck.drawCards(2))

    def hit(self, player):
        player.hand.append(self.deck.drawCards(1))

    def stand(self, player): #when a player says they need to poop but have no poop to poop
        pass

    def checkWin(self):
        pass

    def checkBust(self):
        pass

    def checkBlackJack(self):
        pass

    def checkTurn(self):
        pass

    def checkActions(self):
        pass

    def checkGame(self):
        pass

    def checkGameOver(self):
        pass

    def checkGameWinner(self):
        pass

    def checkGameLoser(self):
        pass

    def checkGameTie(self):
        pass

    def checkGamePush(self):
        pass

    def checkGameWin(self):
        pass

class Player: 
    name = ''
    hand = []
    
    def _init_(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def setHand(self, hand):
        self.hand = hand