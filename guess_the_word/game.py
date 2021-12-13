from words import Words
from random import randint


class Game:
    __chances: int = 6
    __test: bool

    def __init__(self, test: bool) -> None:
        self.__test = test

    def create_hint(self, word: str) -> str:
        length = len(word)
        rand_1 = randint(0, (length / 3).__floor__())
        rand_2 = randint((length / 3).__floor__(), ((2 * length) / 3).__floor__())
        rand_3 = -1
        rand_4 = -1

        if length > 8:
            rand_3 = randint(((2 * length) / 3).__floor__(), length - 1)

        if length > 12:
            rand_4 = randint(0, length - 1)

        new_word: list[str] = []

        i = 0
        while i < length:
            if rand_1 == i:
                new_word.append("_")
            elif rand_2 == i:
                new_word.append("_")
            elif rand_3 == i:
                new_word.append("_")
            elif rand_4 == i:
                new_word.append("_")
            else:
                new_word.append(word[i])

            i = i + 1

        return new_word

    def start(self) -> None:
        words = Words(self.__test)

        while self.__chances > 0:
            if len(words.get_words_list()) == 0:
                print("\nYou have won the game!\n")
                return

            word = words.get_random_word()

            if self.__test:
                print(word)

            guess_word = self.create_hint(word)
            user_guess: str = ""

            while (
                words.validate_word(user_guess.upper()) is not True
                and self.__chances > 0
            ):
                print(f"\n{guess_word}")
                user_guess = input("Guess the word: ")

                if words.validate_word(user_guess.upper()):
                    break

                self.__chances = self.__chances - 1
                print(f"\nIncorrect guess!\nChances left: {self.__chances}\n")

            print("Good work!")

        print("\nYou have lost the game!\n")
