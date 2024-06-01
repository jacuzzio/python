#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art as a
from replit import clear 

def eval_guess(randNum, user_guess):
  if user_guess == randNum:
    return "win"	
  elif user_guess < randNum:
    print("Too low.")
  else:
    print("Too high.")
  return "guess_again", attempts

def difficulty():
   while True: 
    mode = input("\nChoose a difficulty, [E]asy or [H]ard:  ").lower()
    if mode == 'e':
      print("You have 10 guesses.")
      return 10
    elif mode == 'h':
      print("You have 5 guesses.")
      return 5
    else:
      print("\nInvalid input. Please type 'e' for easy or 'h' for hard:  ")

def start_game():
  print(a.logo)
  print("Welcome to guess the number")
  print("Im thinking of a number from 1 to 100.")
  mode = difficulty()
  return mode

def ask_guess():
  while True:
    try:
      guess = int(input("\nMake a guess:  "))
    except ValueError:
      print("Invalid input. Please input an integer.")
    return guess
  
#this main funcation generates the number and checks the guesses until win/lose
def main(attempts): 
  #Generate number (1,100)
  randNum = random.randint(1,100)
  #ask user to keep guessing until they run out of attempts
  while attempts > 0:
    user_guess = ask_guess()
    guess_again = eval_guess(randNum, user_guess)
    if guess_again == 'win':
      print(f"You guessed it! The number is {randNum}.")
      return 'win'
    attempts -= 1
    if attempts > 0:
      print(f"\nYou have {attempts} guesses left.")
  print(f"You didn't guess the number. The number was {randNum}.")
  return 'lose'
    
#heres where its all put together
play = True
while play:
  clear()
  attempts = start_game()
  main(attempts)
  
  play_again = input("\nWould you like to play again? [Y]es or [N]o?  ").lower()
  if play_again != 'y':
    play = False
    print('Goodbye.')

    