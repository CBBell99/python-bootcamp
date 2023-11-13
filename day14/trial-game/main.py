from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls || clear')
print(logo)

account_a = random.choice(data)


def print_options(option_one, option_two):
    print(
        f"Compare A: {option_one['name']}, {option_one['description']}, {option_one['country']}")
    print(vs)
    print(
        f"Compare B: {option_two['name']}, {option_two['description']}, {option_two['country']}")





def game():
    score = 0
    game_over = False
    option_a = getRandomData()
    option_b = getRandomData()

    while not game_over:
      # option_a = data[0]
      # option_b = data[1]
      print(logo)
      print_options(option_a, option_b)
      
      guess = input("Who has more followers? Type 'A' or 'B': ")
      if guess.lower() == 'a':
          guess = option_a
          if guess['follower_count'] > option_b['follower_count']:
              score += 1
              print(f"You're right! current score: {score}.")
              option_b = getRandomData()

          elif guess['follower_count'] < option_b['follower_count']:
              print(f"Sorry, that's wrong. Final score: {score}")
              game_over = True

      else:
          guess = option_b 
          if guess['follower_count'] > option_a['follower_count']:
              score += 1
              print(f"You're right! current score: {score}.")
              option_a = guess
              option_b = getRandomData()

          elif guess['follower_count'] < option_a['follower_count']:
              print(f"Sorry, that's wrong. Final score: {score}")
              game_over = True
      clear()    
game()
