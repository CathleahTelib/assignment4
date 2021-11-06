def personalDetails():
    name = input("Name:")
    age = int(input("Age:"))
    address = input("Address:")
    return name,age,address


def outputD(nameA,ageA,addressA):
    print(f"Hi my name is {nameA}. I am {ageA} years old and I live in {addressA}.")


nameQ,ageQ,addressQ = personalDetails()
output = outputD(nameQ, ageQ, addressQ)