from words import Words
from random import randint


class Game:
    __chances: int = 6

    def __init__(self) -> None:
        pass

    def create_hint(self, word: str) -> str:
        length = len(word)
        rand_1 = randint(0, (length / 3).__floor__())
        rand_2 = randint((length / 3).__floor__(), ((2 * length) / 3).__floor__())
        rand_3 = -1
        rand_4 = -1

        if length > 5:
            rand_3 = randint(((2 * length) / 3).__floor__(), length - 1)

        if length > 8:
            rand_4 = randint(0, length - 1)

        new_word: list[str] = []

        i = 0
        while i < length:
            if rand_1 == i:
                new_word.append(word[i])
            elif rand_2 == i:
                new_word.append(word[i])
            elif rand_3 == i:
                new_word.append(word[i])
            elif rand_4 == i:
                new_word.append(word[i])
            else:
                new_word.append("_")

            i = i + 1

        return new_word

    def start(self) -> None:
        words = Words()

        while self.__chances != 0:
            if len(words.get_words_list()) == 0:
                print("\nYou have won the game!\n")
                return

            word = words.get_random_word()
            print(word)
            guess_word = self.create_hint(word)

            print(guess_word)
            user_guess = input("Guess the word: ")

            if words.validate_word(user_guess.upper()):
                print("Good work!")
            else:
                self.__chances = self.__chances - 1
                print("\nIncorrect guess\n")

        print("\nYou have lost the game!\n")
