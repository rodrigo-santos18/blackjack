from objects import *
from time import sleep


cash = None

while not isinstance(cash, float):
    cash = input("Welcome to the HS Casino! How much money would you like to bet?\n")
    try:
        float(cash)
    except ValueError or TypeError:
        print("\nReally? I'm not in the mood for games, pal. Let's take a deep breath and start from the beginning.")
        sleep(0.5)
    else:
        cash = float(cash)


player1 = Player(cash)
dealer = Player(7000)

if cash < 0:
    while cash < 0:
        print("Come on! Negative money? Really? What's next, you'll say you wanna bet 'sofa' euros? Be reasonable.")
        cash = float(input("Let's try again. How much money would you like to bet?\n"))

if cash < 50:
    while cash < 50:
        print("\nI'm sorry. If you're broke, you could have just said that. Minimum bet is 50, pal.")
        sleep(0.5)
        cash = float(input("Let's try again. How much money would you like to bet?\n"))

pack = Pack()
sleep(0.50)

if cash > 10000:
    print("\nGreat! I must say, that'll keep us going for a while.\n")

if (cash//50) == 1:
    print("Wow, that'll give you a grand total of... A SINGLE CHIP! I swear to god, if you turn a profit on this...")
else: 
    print("\nAlright. That's ", int(cash // 50), "chips. Let's get started, shall we?")

roundCounter = 0
while player1.chips() > 0 and dealer.chips() > 0:
    
    bet = None

    while not isinstance(bet, int):
        bet = input("\nHow many chips do you wanna put down this round?\n")
        try:
            int(bet)
        except ValueError or TypeError:
            bet = input("Please remember: you can't bet 'x' chips or anything like that. It's not funny. Let us try again.") 
        else:
            bet = int(bet)
    
    if bet > player1.chips():
        while bet > player1.chips():
            bet = input("\nYou can't bet more than you have, genius. So, again: how many will you put down?\n")
            try:
                int(bet)
            except ValueError or TypeError:
                bet = input("Please remember: you can't bet 'x' chips or anything like that. It's not funny. Let us try again.") 
            else:
                bet = int(bet)
    
    player1.bet(bet)
    sleep(0.50)
    
    print("\nOk, your chips are in the pot now. Hope you don't regret that!")
    
    pack.pull(player1)
    pack.pull(player1)
    pack.pull(dealer)

    print("Your hand: ", player1.hand())
    print("Dealer's hand: ", dealer.hand())

    sleep(0.25)

    dealerPoints = 0
    for cards in dealer.hand():
        dealerPoints += cards.value()

    playerPoints = 0
    for cards in player1.hand():
        playerPoints += cards.value()  

    if dealerPoints == 21:
        print("\nUh, looks like I'm a natural! But don't worry, you may still draw this...")
         
    if playerPoints == 21:
        print("\n A natural, hey? I can still draw this.")

    if playerPoints != 21:
        response = input("\nDo you want to pull another card? [y/n]\n")
        lowerResp = response.lower()
        possibleResp = ["y", "yes", "n", "no"]

        if lowerResp not in possibleResp:
            while lowerResp not in possibleResp:
                response = input("Come on, I don't have all day! It's a yes or no question. Do you want to draw another card? [y/n]")
                lowerResp = response.lower()

        if lowerResp == "y" or lowerResp == "yes":
                while lowerResp == ("y" or "yes"):    
                    print(random.choice(["Alright then!", "Ok!", "Alright, sure!"]))
                    pack.pull(player1)
                    sleep(0.5)
                    print("\nYour hand: ", player1.hand())

                    sleep(0.5)
                    playerPoints = 0
                    for cards in player1.hand():
                        playerPoints += cards.value() 
                    if playerPoints > 21:
                        print("Oops! Looks like it's a bust.")
                        print("Don't worry though, let's go for another round.")
                        roundCounter += 1
                        player1.hand_reset()
                        break

                    response = input(random.choice(["\nSo, wanna go again? The deck's calling [y/n]\n",
                                                    "\nOne more? [y/n]", 
                                                    "\nAnother one? [y/n]"]))
                    lowerResp = response.lower()


    dealerPoints = 0
    for cards in dealer.hand():
        dealerPoints += cards.value() 
        
    while dealerPoints < 17:
        pack.pull(dealer)
        print("The dealer has pulled a card.")
        sleep(1)        
        print("\nDealer's hand: ", dealer.hand())
        sleep(1)        
        dealerPoints = 0
        for cards in dealer.hand():
            dealerPoints += cards.value() 
        print("Dealer's hand value = ", dealerPoints)
        sleep(1)

    if dealerPoints > 21:
        print("\nDamn it! It's a bust. I'll get you next time...")
        player1.hand_reset()
        dealer.hand_reset()

    playerPoints = 0
    for cards in player1.hand():
        playerPoints += cards.value() 

    if 21 > dealerPoints > playerPoints:
        print("\n Aha! I win. Let's go for another round.")
        player1.hand_reset()
        dealer.hand_reset()
    
    if dealerPoints < playerPoints < 21:
        print("\n Beginner's luck. Another round, shall we?")
        player1.hand_reset()
        dealer.hand_reset()


              