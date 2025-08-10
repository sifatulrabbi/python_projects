from typing import Any


class Person:
    name: str
    age_months: int
    weight_kg: int
    height_cm: int
    gender: str
    bond: Any

    def __init__(
        self,
        name: str,
        age_months: int,
        weight_kg: int,
        height_cm: int,
        gender: str,
    ):
        self.name = name
        self.age_months = age_months
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.gender = gender
        self.bond = None

    def __str__(self):
        return f"{self.name}. {self.age_months/12} years old {self.gender}. Who is {self.height_cm} cm tall and weighs {self.weight_kg} KGs."

    def __add__(self, person):
        if not isinstance(person, Person):
            print("Can only be added to a Person.")
            return

        if self.bond is not None:
            print(f"Rejected! {self.name} is already bonded!")
            return
        bond = Bond("romantic", self, person)
        return bond

    def __mul__(self, person):
        if not isinstance(person, Person):
            print("Can only be married to a Person.")
            return

        if self.bond is None:
            print(f"Sorry, no marriage before bonding!")
            return

        bonded = False
        for p in self.bond.parties:
            if p.name == person.name:
                bonded = True
                break
        if not bonded:
            print(f"Rejected! {self.name} is already bonded!")
            return

        bond = Bond("marriage", self, person)
        return bond


class Male(Person):
    def __init__(
        self,
        name: str,
        age_months: int,
        weight_kg: int,
        height_cm: int,
    ):
        super().__init__(name, age_months, weight_kg, height_cm, "male")


class Female(Person):
    def __init__(
        self,
        name: str,
        age_months: int,
        weight_kg: int,
        height_cm: int,
    ):
        super().__init__(name, age_months, weight_kg, height_cm, "female")


class Bond:
    parties: tuple[Person, Person]
    bond_type: str

    def __init__(self, bond_type: str, p1: Person, p2: Person):
        self.bond_type = bond_type
        self.parties = (p1, p2)
        p1.bond = self
        p2.bond = self

    def __str__(self):
        return f"A {self.bond_type} bond between {self.parties[0].name} and {self.parties[1].name}"

    def break_bond(self):
        self.parties[0].bond = None
        self.parties[1].bond = None


jackson = Male("Jackson", 480, 88, 183)
emily = Female("Emily", 390, 67, 165)
julies = Male("Julies", 350, 78, 178)

print(jackson)
print(emily)
print(jackson + 2)
print(jackson + emily)
print(emily * julies)
print(jackson * emily)
