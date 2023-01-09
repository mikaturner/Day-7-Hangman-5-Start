#Step 5

import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []
end_of_game = False
lives = 6

logo = hangman_art.logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.  
  
  if guessed_letters.count(guess) > 0:
    print(f"You have already entered {guess}.")
  else: 
    guessed_letters.append(guess)
    
    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      lives -= 1
    
    if lives == 0:
      end_of_game = True
      print("You lose.")

    #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
      end_of_game = True
      print("You win.")

  #TODO-2: - Import the stages from hangman_art.py and make this error go away.
  print(hangman_art.stages[lives])