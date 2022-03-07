import random
from words import word_list
from display_hangman import display


class HangmanGame:
    tries: int
    word: str = ""
    guessed_word_list: list[str] = []
    word_completion: str = ""
    gameover = False

    def __init__(self):
        self.tries = 6
        self.word = self.get_word()

    # Get a random word
    def get_word(self) -> str:
        word = random.choice(word_list).upper()

        while word == self.word:
            word = random.choice(word_list).upper()

        self.word_completion = "_" * len(word)
        return word

    def start(self):
        display(self.tries)
        print("Your word: {}".format(self.word_completion))
        guess = str(input("Input your word: ")).upper()

        # take in guessed letter
        if len(guess) == 1 and guess.isalpha():
            # check if the letter is used before
            if guess in self.guessed_word_list:
                print("\nYou have already guessed the word!")
                self.tries -= 1
            # check if the letter is in the word
            elif guess not in self.word:
                print("\nYour guess is incorrect!")
                self.tries -= 1
            else:
                print("\nGood job. Perfect guess!")
                word_as_list = list(self.word_completion)
                indices = [
                    i for i, letter in enumerate(self.word) if letter == guess
                ]

                for index in indices:
                    word_as_list[index] = guess

                self.word_completion = "".join(word_as_list)

            self.guessed_word_list.append(guess)

            if self.tries == 0:
                self.gameover = True
                print("\nYou have lost! Try again next time")

    def reset(self):
        self.tries = 6
        self.gameover = False
        self.word = self.get_word()
        self.guessed_word_list = []


def main():
    game = HangmanGame()

    while not game.gameover:
        game.start()

        if "_" not in game.word_completion:
            print("\nCongrats you have guessed the word: {}".format(game.word))
            play_again = str(input("\nDo you want to play again? ")).upper()

            if play_again == "YES":
                game.reset()
            else:
                print("\nThanks for playing")
                break


main()
