#Blackjack Capstone Project

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#Hint 5: Deal the user and computer 2 cards each using deal_card()
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from os import remove
import random
import re
import os
from art import blackjack_logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
user_card = []
computer_card = []
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
#print(user_card)
#print(computer_card)
def calculate_score(cards):
    return sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        remove.cards[11]
        cards.append(1)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "user loses"
    elif user_score == 0:
        return "user wins"
    elif user_score>21:
        return "user loses"
    elif computer_score>21:
        return "computer loses"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(blackjack_logo)
    game_end = False
    while not game_end:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                user_card.append(deal_card())
                #print(user_card)
                user_score = calculate_score(user_card)
                #print(user_score)
            else:
                game_end = True
    while computer_score!=0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ") == 'y':
    os.system('cls')
    play_game()








    


