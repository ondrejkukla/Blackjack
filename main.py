import random
from art import logo

list_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def game_over():
  return

def deal_card():
  global your_cards, computer_cards, get_card, game, n
  while get_card == "y":
    if not len(your_cards) == n:
      your_cards.append(random.choice(list_of_cards))
    if len(your_cards) == n:
      print(f"Your cards are {your_cards}.")
      print(f"Computer's first card is {computer_cards}.")
      get_card = "n"
      comparation()

def comparation():
  global n, get_card
  if sum(your_cards) == 21 and sum(computer_cards) == 21:
    print("Draw.")
  elif sum(your_cards) == 21:
    print(f"You win. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  elif sum(your_cards) > 21:
    for ace in your_cards:
      if ace == 11:
        ace = 1
    print(f"You lose. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  elif sum(computer_cards) == 21:
    print(f"You lose. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  elif sum(computer_cards) > 21:
    print(f"You win. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  else:
    next_card = input("Do you want another card? 'y' or 'n': ")
    if next_card == "y":
      n += 1
      get_card = "y"
      deal_card()
    else:
      while sum(computer_cards) < 17:
          computer_cards.append(random.choice(list_of_cards))
      comparation_only()
      

def comparation_only():
  global n, get_card
  if sum(your_cards) == 21 and sum(computer_cards) == 21:
    print("Draw.")
  elif sum(your_cards) == 21:
    print(f"You win. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  elif sum(your_cards) > 21:
    for ace in your_cards:
      if ace == 11:
        ace = 1
    print(f"You lose. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  elif sum(computer_cards) == 21:
    print(f"You lose. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  elif sum(computer_cards) > 21:
    print(f"You win. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
  else:
    if sum(your_cards) > sum(computer_cards):
          print(f"You win. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
    elif sum(your_cards) < sum(computer_cards):
          print(f"You lose. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")
    elif sum(your_cards) == sum(computer_cards):
          print(f"Draw. Your score is {sum(your_cards)} and computer's score is {sum(computer_cards)}")

def you_win():
  return "You win"
def you_lose():
  return "You lose"
def draw():
  print("Draw.")
  

your_cards = []
computer_cards = []
get_card = "y"
n = 2

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
computer_cards.append(random.choice(list_of_cards))

if game == "y":
  get_card == "y"
  deal_card()