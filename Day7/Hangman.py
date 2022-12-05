#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


#Step 2

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

len_of_chosen_word = len(chosen_word)

blank_list = ["_"]*len_of_chosen_word
print(blank_list)
total_lives = 6
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
count = 0
end_of_game = False
while not end_of_game:
    guess = input("Choose one letter").lower()
    if guess in blank_list:
        print("Prevoius letter")
        continue
    for letter in chosen_word:
        if letter == guess:
            #print("Right")
            blank_list[count]=letter
            count+=1
        else:
            #print("Wrong")
            count += 1
    count=0
    if guess not in chosen_word:
        total_lives-=1
        if total_lives == 0:
            end_of_game=True
            print("You Loose")
    if "_" not in blank_list:
        end_of_game=True
        print("You Win")


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(blank_list)