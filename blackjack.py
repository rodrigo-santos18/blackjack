# Projeto BLACKJACK

import random

class Cards:
    def __init__(self):
        

class Casino:

    def __init__(self):
        _players = []
        _deck = []
        _shops = []

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

    def get_card():
        

