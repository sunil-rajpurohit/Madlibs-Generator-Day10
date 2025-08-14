import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def mad_libs():
    print("Welcome to Mad Libs!")
    # ask the user for words
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    animal = input("Enter an animal: ")

    # story 
    story = f"""
    Today I went to the {place} and saw a {adjective} {noun}.
    It started to {verb} right in front of me!
    Then, a {animal} joined the fun. What a day!
    """
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    clear_screen()
    mad_libs()
