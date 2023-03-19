# Projeto BLACKJACK

import random

class Card:


    def __init__(self, int):
        self._id = int
        
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
        
class Pack:
    

class Player:

    def __init__(self,cash):
        self._hand = []
        self._tricks = []
        if isinstance(cash, float):
            self._chips = cash // 50
        else: 
            print("That's not cash... come on, the House is not stupid.")

    def bet(n_chips):
        Player._chips -= n_chips
        Pot += n_chips
    
    def hand():
        return self._hand

    def ask_Card():
        hand_value = 0
        for indx, card in enumerate(Player.hand()):
            card.value += hand_value

        

class Dealer(Player):


    def __init__(self):
        self._pack = []
        self._betPot = 0

    def __iadd__(bet):
        Dealer._betPot += bet 

    def __isub__(bet):
        Dealer._betPot -= bet 

    def players():
        return Dealer.players

    def pack():
        return Dealer.pack

             


class Pot:


    def __init__(self):
        self._pot = 0.0

    def __iadd__(bet):
        Pot._pot += bet

    def __isub__(bet)_
        Pot._pot -= bet

    def reset():
        Pot._pot = 0.0



        
