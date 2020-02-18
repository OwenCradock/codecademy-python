import random

money = 100


#Write your game of chance functions here
def coin_flip(guess, bet):
    print("====================\nCOIN FLIP\n====================")
    print("Your balance is $" + str(money))
    
    if guess != ("Heads" and "Tails"):
        print("You did not enter 'Heads' or 'Tails' as your guess. Game aborted")
        return 0
    else:
        print("Your bet is $" + str(bet))
        if bet > money:
            print("You do not have enough money to play this game. Game aborted")
            return 0
        elif bet < 0:
            print("Please enter a positive number bet. Game aborted")
            return 0
        else:
            print("Your call is " + guess)
            print("Performing coin flip...")
            flip = random.randint(1, 2)
           
            if flip == 1:
                print("...HEADS")
            else:
                print("...TAILS")
                
            if guess == "Heads" and flip == 1:
                print("Successful Heads call!")
                return bet
            elif guess == "Tails" and flip == 2:
                print("Successful Tails call!")
                return bet
            else:
                bet = bet - (2 * bet)
                print("Hard luck!")
                return bet
        

def cho_han(guess, bet):
    print("\n====================\nCHO HAN\n====================")
    print("Your balance is $" + str(money))
    
    if guess != ("Odd" and "Even"):
        print("You did not enter 'Odd' or 'Even' as your guess. Game aborted")
        return 0
    else:
        print("Your bet is $" + str(bet))
        
        if bet > money:
            print("You do not have enough money to play this game. Game aborted")
            return 0
        elif bet < 0:
            print("Please enter a positive number bet. Game aborted")
            return 0
        else:
            print("Your call is " + guess)
            print("Rolling 2 dice...")
            cho = random.randint(1, 6) + random.randint(1, 6)
            print("...they add up to " + str(cho) + "!")
            
            if cho % 2 == 0 and guess == "Even":
                print("Successful Even call!")
                return bet
            elif cho % 2 != 0 and guess == "Odd":
                print("Successful Odd call!")
                return bet
            else:
                bet = bet - (2 * bet)
                print("Hard luck!")
                return bet
    
    
def pick_a_card(bet):
    print("\n====================\nHIGHER CARD\n====================")
    print("Your balance is $" + str(money))
    print("Your bet is $" + str(bet))
    
    if bet > money:
        print("You do not have enough money to play this game. Game aborted")
        return 0
    elif bet < 0:
        print("Please enter a positive number bet. Game aborted")
        return 0
    else:     
        print("You pick a card...")
        user_card = random.randint(1, 13)
        print("..." + str(user_card))
        print("The computer picks a card...")
        comp_card = random.randint(1, 13)
        print("..." + str(comp_card))
        
        if user_card > comp_card:
            print(str(user_card) + " is higher than " + str(comp_card))
            print("You win!")
            return bet
        elif user_card < comp_card:
            print(str(comp_card) + " is higher than " + str(user_card))
            print("Hard luck!")
            bet = bet - (2 * bet)
            return bet
        else:
            print("It's a tie!")
            return 0
    
    
def roulette(guess, bet):
    print("\n====================\nROULETTE\n====================")
    print("Your balance is $" + str(money))
    print("Your bet is $" + str(bet))
    
    if bet > money:
        print("You do not have enough money to play this game. Game aborted")
        return 0
    elif bet < 0:
        print("Please enter a positive number bet. Game aborted")
        return 0
    else:
        try:
            tile = random.randint(0, 37)
            
            if tile == 37:
                
                if str(guess) == "00":
                    print("Your call is " + str(guess))
                    print("Performing a roulette spin...")
                    print("...and the tile is 00!")
                    bet = bet * 35
                    print("Congrats! You landed on the exact tile and made $" + str(bet) + "!")
                    return bet
                
                elif str(guess) == "Even":
                    print("Your call is " + str(guess))
                    print("Performing a roulette spin...")
                    print("...and the tile is 00!")
                    print("Hard luck this time - you lose $" + str(bet))
                    bet = bet - (2 * bet)
                    return bet
            
                elif str(guess) == "Odd":
                    print("Your call is " + str(guess))
                    print("Performing a roulette spin...")
                    print("...and the tile is 00!")
                    print("Hard luck this time - you lose $" + str(bet))
                    bet = bet - (2 * bet)
                    return bet    
                        
                elif int(guess) > -1 and int(guess) < 37:
                    print("Your call is " + str(guess))
                    print("Performing a roulette spin...")
                    print("...and the tile is 00!")
                    print("Hard luck this time - you lose $" + str(bet))
                    bet = bet - (2 * bet)
                    return bet  
                              
            elif str(guess) == "Even":
                print("Your call is " + str(guess))
                print("Performing a roulette spin...")
                print("...and the tile is " + str(tile) + "!")
                if tile % 2 == 0 and tile != 0:
                    print("Successful Even call - you made $" + str(bet) + "!")
                    return bet
                else:
                    print("Hard luck this time - you lose $" + str(bet))
                    bet = bet - (2 * bet)
                    return bet
            
            elif str(guess) == "Odd":
                print("Your call is " + str(guess))
                print("Performing a roulette spin...")
                print("...and the tile is " + str(tile) + "!")
                if tile % 2 != 0 and tile != 37:
                    print ("Successful Odd call - you made $" + str(bet) + "!")
                    return bet
                else:
                    print("Hard luck this time - you lose $" + str(bet))
                    bet = bet - (2 * bet)
                    return bet    
                    
            elif int(guess) > -1 and int(guess) < 37:
                print("Your call is " + str(guess))
                print("Performing a roulette spin...")
                print("...and the tile is " + str(tile) + "!")
                if int(guess) == tile:
                    bet = bet * 35
                    print("Congrats! You landed on the exact tile and made $" + str(bet) + "!")
                    return bet
                else:
                    print("Hard luck this time - you lose $" + str(bet))
                    bet = bet - (2 * bet)
                    return bet
                     
            else:
                print("You did not enter a valid roulette option ('Odd', 'Even', '00', '0', '1', '2'...'35', '36') Game aborted")
                return 0
        
        except ValueError:
            print("You did not enter a valid roulette option ('Odd', 'Even', '00', '0', '1', '2'...'35', '36') Game aborted")
            return 0
                    
                    
                    
#Call your game of chance functions here
money_changed = coin_flip("Tails", 20)
if money_changed == 0:
    money = money + money_changed
    print("Your balance remains at $" + str(money))
else:
    money = money + money_changed
    print("Your new balance is $" + str(money))


money_changed = cho_han("Even", 20)
if money_changed == 0:
    money = money + money_changed
    print("Your balance remains at $" + str(money))
else:
    money = money + money_changed
    print("Your new balance is $" + str(money))
    
    
money_changed = pick_a_card(-20)
if money_changed == 0:
    money = money + money_changed
    print("Your balance remains at $" + str(money))
else:
    money = money + money_changed
    print("Your new balance is $" + str(money))
    
    
money_changed = roulette("s0df", 100)
if money_changed == 0:
    money = money + money_changed
    print("Your balance remains at $" + str(money))
else:
    money = money + money_changed
    print("Your new balance is $" + str(money))
