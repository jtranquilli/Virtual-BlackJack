#Tasks

 #Bets are placed at the start of each round, the payoff ratio per bet is 2:1
 #Player is randomly dealt two cards
 #KING, QUEEN, JACK are each worth 10 points
 #ACE cards are worth 1 or 11 points, the more favourable valuation for your hand is automatically chosen
 #Player is offered the choice of HIT or STAND after cards are dealt
 #If the value of the player's hand exceeds 21, the round and wager are lost
 #If the player chooses to stand, their hand is evaluated against a randomly generated dealer's hand

import random as r

VALUES = {'ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,
            'SEVEN':7,'EIGHT':8,'NINE':9,'TEN':10,'JACK':10,
            'QUEEN':10,'KING':10,'ACE':11}

DECK = ['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE',
            'TEN','JACK','QUEEN','KING','ACE']



def main(current_money):
    

    def place_bet():
        
        bet = input("Enter your bet:$")
        
        if int(bet) < 0:
            
            raise ValueError("Bet must be a positive integer")
        
        
        if int(bet) > current_money:
            
            print("You can not bet more money than you have. You currently have $",current_money)
            
            place_bet()
            
        return bet
        
        
    def deal_cards(num):
        
        hand = []
        
        for i in range(num):
            
            hand.append(r.choice(DECK))
            
            
        return hand

    def deal_new_card(hand):
        
        
        hand.append(r.choice(DECK))
            
            
        return hand


    def hit_or_stand(current_hand,bet,current_money):
        
        choice = input("Would you like to hit or stand?")
        
        if choice == 'stand':
            
            score = hand_value(current_hand)
            
            dealer_score = r.randint(2,21)
            
            print("The dealer's hand:",dealers_hand(dealer_score))
                  
            print("Your score is",score,"and the dealer's score is",dealer_score)
            
            
            if 21 - dealer_score < 21 - score:
                
                print("You lose!")
                
                current_money -= int(bet)
                
                print("You now have $", current_money)
                
                return current_money
                
            if 21 - dealer_score > 21 - score:
                
                print("You win!")
                
                current_money += int(bet)
                
                print("You now have $",current_money)
                
                return current_money
                
            if 21 - dealer_score == 21 - score:
                
                print("Dealer wins in a tie, you lose")
                
                current_money -= int(bet)
                
                print("You now have $",current_money)
                
                return current_money
                     
                
        if choice == 'hit':
            
            deal_new_card(current_hand)
            
            print("Your current hand is",current_hand)
            
            if hand_value(current_hand) > 21 and "ACE" not in current_hand:
                
                print("You lose!")
                
                print("You now have $0")
                
            if hand_value(current_hand) > 21 and "ACE" in current_hand:
                
                ACE = 1
                
                if hand_value(current_hand) > 21:
                    
                    print("You hit",hand_value(current_hand),".You lose")
                else:
                    
                    hit_or_stand(current_hand,bet,current_money)
            
            else:
                
        
                hit_or_stand(current_hand,bet,current_money)
               
        
    def hand_value(current_hand):
        
        value = 0
        
        for card in current_hand:
            
            card_val = VALUES.get(card)
            
            value += card_val
            
        return value
    
    def dealers_hand(score):
        
        hand =[]
        
        while score != 0:
        
            if score % 11 != score:
                
                hand.append("ACE")
                
                score = score - 11
                
            if score % 10 != score:
                
                hand.append("TEN")
                
                score = score - 10
                
            if score % 9 != score:
                
                hand.append("NINE")
                
                score = score - 9
                
            if score % 8 != score:
                
                hand.append("EIGHT")
                
                score = score - 8
                
            if score % 7 != score:
                
                hand.append("SEVEN")
                
                score = score - 7
                
            if score % 6 != score:
                
                hand.append("SIX")
                
                score = score - 6
                
            if score % 5 != score:
                
                hand.append("FIVE")
                
                score = score - 5
                
            if score % 4 != score:
                
                hand.append("FOUR")
                
                score = score - 4
                
            if score % 3 != score:
                
                hand.append("THREE")
                
                score = score - 3
                
            if score % 2 != score:
                
                if len(hand) < 2:
                    hand.append("ACE")
                    
                    hand.append("ACE")
                    
                else:
                    
                    hand.append("TWO")
                
                score = score - 2
                
            if score % 1 != score:
                
                hand.append("ACE")
                
                score = score - 1
                
            return hand
                            

    def run_machine():
        
        bet = place_bet()
        
        current_hand = deal_cards(2)
        
        print("You have been dealt",current_hand)
        
        hit_or_stand(current_hand,bet,current_money)
        
        restart = input("Would you like to play again?")
        
        if restart == "yes":
            
            
            
            run_machine()
            
        else:
            print("You have $",current_money,". Goodbye")
    
            exit
    
    

    if __name__ == "__main__":
        run_machine()
        
main(100)

