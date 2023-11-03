from random import choice
from art import logo, vs
from game_data import data
import os

final_score = 0

def play(data):
    def celebritie_a(data):
        choice_a = choice(data)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
        return choice_a['follower_count']
    followers_a = celebritie_a(data)
    
    def celebritie_b(data):
        choice_b = choice(data)
        print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
        return choice_b['follower_count']
    followers_b = celebritie_b(data)
    
    def comparison(followers_a,followers_b):
        global final_score
        user_choice = input('Who has more followers? "A" or "B"?')
        if user_choice == 'A':
            if followers_a > followers_b:
                final_score += 1
                os.system('clear')
                print(logo)
                print(f"You are right! Final score: {final_score}")
            elif followers_a < followers_b:
                os.system('clear')
                print(logo)
                print(f"Sorry, you are wrong. Final score: {final_score}")
        elif user_choice == 'B':
            if followers_b > followers_a:
                final_score += 1
                os.system('clear')
                print(logo)
                print(f"You are right! Final score: {final_score}")
            elif followers_b < followers_a:
                os.system('clear')
                print(logo)
                print(f"Sorry, you are wrong. Final score: {final_score}")
    comparison(followers_a=followers_a, followers_b=followers_b)
 
print(logo)
continue_play = True
while continue_play: 
    f = final_score  
    play(data)
    if f == final_score:
        break