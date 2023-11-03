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
play(data)