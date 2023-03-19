# Projeto BLACKJACK

import random
import winsound

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
        


class Casino:
    def __init__(self):
        self._players = []
        self._deck = []
        self._shops = []

    def __iadd__(player):
        if player not in Casino.players:
            Casino.players.append(player)
        else:
            print("This player is already in the Casino!")

    def __isub__(player):
        if player in Casino.players:
            Casino.players.remove(player)
        else:
            print("This player is not in the Casino!")

    def players():
        return Casino.players

    def deck():
        return Casino.deck

    def distribute(card):
        for i, gambler in enumerate(Casino.players()):
           gambler += random.choice(Casino.deck)

        


class Player:

    def __init__(self):
        hand = []
        tricks = []