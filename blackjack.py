# Objetos do Blackjack (cartas, jogador e pack - o conjunto de cartas, o deck)


import random


class Card:

    def __init__(self, id):
        self._id = id
        
        if self._id / 13 <= 1:
            self._suit = "clubs"
            self._idFactor = 0 
        
        elif 1 < self._id / 13 <= 2:
            self._suit = "diamonds"
            self._idFactor = 1
        
        elif 2 < self._id / 13 <= 3:
            self._suit = "hearts"
            self._idFactor = 2  
        
        else:
            self._suit = "spades"
            self._idFactor = 3

        self._value = self._id - self._idFactor * 13
        
    def suit():
        return Card._suit
    
    def value():
        return Card._value
    
    def id():
        return Card._id


class Pack:

    def __init__(self) -> None:
        self._pack = set()
        count = 0
        while count < 7:
            for i in range(1, 53):
                self._pack.add(Card(i))
            count += 1

    def packIds():
        packIds = []
        for card in Pack._pack:
            packIds.append(card.id())
        return packIds
    
    def pack():
        return Pack._pack
            

class Player:

    def __init__(self,cash):
        self._hand = []
        self._handValue = sum([card.Value for card in self._hand])
        self._tricks = []
        if isinstance(cash, float):
            self._chips = cash // 50
        else: 
            print("That's not cash... come on, the House is not stupid.")

    def bet(n_chips):
        Player._chips -= n_chips
        Pot += n_chips
    
    def hand():
        return Player._hand
    
    def hand_reset():
        Player._hand = []

    def hand_value():
        return Player._handValue

    def ask_card():
        id = random.choice(Pack.packIds())
        for card in Pack.pack():
            if card.id() == id:
                Pack.remove(card)
                Player._Hand.append(card)
                break
