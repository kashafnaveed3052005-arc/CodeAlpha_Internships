import random
words=["apple","pizza","python","chair","phone"]

word=random.choice(words)

guessed_word=["_"]*len(word)

attempts=6

print("Welcome to Hangman Game!")

print("Guess the word: ")

while attempts>0:

    print("\n Word:", " ".join(guessed_word))
    print("Remaining chances: ",attempts)

    guess=input("Enter a letter: ").lower()

    if guess in word:
        print("Correct Guess!")
        for i in range(len(word)):
            if word[i]==guess:
                guessed_word[i]=guess
    else:
                attempts=attempts-1
                print("Wrong guess!")

    if "_" not in guessed_word:
                    print("\nYou Win! ")
                    print("Word was: ",word)
                    break
                
if "_" in guessed_word:
                    print("Game over")
                    print ("Word was: ",word)
