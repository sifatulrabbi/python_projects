import stories


def main() -> None:
    noun: str = input("Write a noun: ")
    plural_noun_1: str = input("Write a plural noun: ")
    plural_noun_2: str = input("Write a plural noun: ")
    plural_noun_3: str = input("Write a plural noun: ")
    plural_noun_4: str = input("Write a plural noun: ")
    adjective_1: str = input("Write an adjective: ")
    adjective_2: str = input("Write an adjective: ")
    adjective_3: str = input("Write an adjective: ")
    adjective_4: str = input("Write an adjective: ")
    number: str = input("Write a number: ")
    verb: str = input("Write a verb: ")
    place_1: str = input("Write a place: ")
    place_2: str = input("Write a place: ")
    occupation: str = input("Write a occupation: ")
    body_part_1: str = input("Write a body part name: ")
    body_part_2: str = input("Write a body part name: ")
    verb_with_ing_1: str = input("Write a verb ends with ing: ")
    verb_with_ing_2: str = input("Write a verb ends with ing: ")

    stories.template_1(
        noun=noun,
        plural_noun_1=plural_noun_1,
        plural_noun_2=plural_noun_2,
        plural_noun_3=plural_noun_3,
        plural_noun_4=plural_noun_4,
        adjective_1=adjective_1,
        adjective_2=adjective_2,
        adjective_3=adjective_3,
        adjective_4=adjective_4,
        number=number,
        verb=verb,
        place_1=place_1,
        place_2=place_2,
        occupation=occupation,
        body_part_1=body_part_1,
        body_part_2=body_part_2,
        verb_with_ing_1=verb_with_ing_1,
        verb_with_ing_2=verb_with_ing_2,
    )


main()
