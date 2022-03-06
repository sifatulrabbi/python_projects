import random
from words import word_list
from display_hangman import display_hangman


class HangmanGame:
    tries: int
    word: str
    guessed_word_list: list[str] = []
    word_completion: str = ""

    def __init__(self):
        self.tries = 6
        self.word = self.get_word()
        self.word_completion = "_" * len(self.word)

    # Get a random word
    def get_word(self) -> str:
        word = random.choice(word_list).upper()
        return word

    def start(self):
        guess = str(input("Input your word ")).upper()

        # take in guessed letter
        if len(guess) == 1 and guess.isalpha():

            # check if the letter is used before
            if guess in self.guessed_word_list:
                print("You have already guessed the word!")
                self.tries = self.tries - 1
            # check if the letter is in the word
            elif guess not in self.word:
                print("Your guess is incorrect!")
                self.tries = self.tries - 1
            else:
                print("Good job. Perfect guess!")
                index = self.word.find(guess)
                self.word_completion[index] = guess

            self.guessed_word_list.append(guess)
            display_hangman(self.tries)


# if the letter is in the word then reveal the letter and prompt for the next user input

# else show hangman if the user still has tries then prompt for another user input

# if the letter completes the word then show the word and end the game
