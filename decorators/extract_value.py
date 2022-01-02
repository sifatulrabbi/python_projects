def extract_decorator(func):
    def inner(*args, **kwargs):
        person = args[0]
        loves = [*person.get("loves"), "Python"]
        person["loves"] = loves

        func(*args, **kwargs)

    return inner


person1 = {
    "name": "Sifatul Rabbi",
    "age": 20,
    "loves": ["TypeScript"],
}


@extract_decorator
def print_person(person):
    print(f"{person}")


print_person(person1)
