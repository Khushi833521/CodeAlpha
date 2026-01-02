import random

words = ["apple", "banana", "grapes", "orange", "mango"]


word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")


while attempts > 0:
    display_word = ""


    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word.strip())

    
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    
    if guess not in word:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")
    else:
        print("✅ Good guess!")


if attempts == 0:
    print("\n💀 Game Over! You ran out of attempts.")
    print("The word was:", word)