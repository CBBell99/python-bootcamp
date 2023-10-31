import os
from art import logo

def clear():
  os.system('clear')

clear()
print(logo)
print("Welcome to the secret auction program.")

bids = {} 
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner =''
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")    

while not bidding_finished:
  name = input("What is your name?:")
  price = int(input("Whats your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == 'no':
    bidding_finished = True
  elif should_continue == 'yes':
    clear()

find_highest_bidder(bids)

# game_over = False

  # name = input("What is your name?:")
  # max_bid = int(input("Whats your bid?: $"))
  # bidders[name] = max_bid
  # add_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  # if add_bidders == 'no':
  #   game_over = True
  #   highest_bid = 0
  #   for bid in bidders:
  #     if bidders[bid] > highest_bid:
  #       highest_bid = bidders[bid]
  #     # if bidders[bid] == highest_bid:
  #       # print("a",bid)  
  #   if bid == highest_bid:
  #     print('b',bidders[bid])

  #   print 
  #   # print("high",highest_bid)        
    
  # # clear()

