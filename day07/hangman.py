#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[index]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter:\n").lower()
print(guess)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in chosen_word:
  if char == guess:
    print("Right")
  else:
    print("Wrong")  

