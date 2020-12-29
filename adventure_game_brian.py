import time
# must import time to use time.sleep() function throughout the program
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# adapted from breakfast bot refactoring 4
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("\nSorry, I don't understand.")
            print_pause("Please enter a valid input: \n")
    return response


def game_intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    print_pause(" ")
    print_pause("Where does your adventure take you? ... ")
    print_pause(" ")


def house(items, monster):  # things player can encounter at the house
    print_pause("You cautiously walk toward the door of the house.")
    print_pause("You are about to knock when the door opens and "
                f"out steps a {monster}!")
    print_pause(f"Ahhh! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    print_pause(" ")
# From instructions number (4):
# Recall the data type in which the input() functions stores the user input,
# and add code accordingly.
# I think I accomplished this by naming a variable and doing a variable = input
    response = valid_input("Do you want to (1) fight or (2) run away? \n",
                           "1", "2")
    if response == '1':
        fight(items, monster)

    elif response == '2':
        print_pause(" ")
        print_pause("You run back into the field ... ")
        print_pause(" ")
        field(items, monster)


def cave(items, monster):  # things player can encounter at cave
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff.\n"
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        print_pause(" ")
        field(items, monster)
    else:
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        items.append("sword")
        print_pause("You walk back out to the field.")
        print_pause(" ")
        field(items, monster)


def fight(items, monster):  # if user chooses to fight, what happens
    if "sword" in items:
        print_pause(f"As the {monster} moves toward you to attack, "
                    "you unsheath your new sword.")
        print_pause("The sun gleams brightly on the Sword of Ogoroth.\n"
                    "And, you brace yourself for a fight.")
        print_pause(f"But, the {monster}, knowing the power of the Sword of "
                    "Ogoroth, \ntakes one look at your legendary weapon "
                    "and runs away!")
        print_pause(" ")
        print_pause(f"You have rid the town of the {monster}.\n"
                    "You are victorious!")
        print_pause(" ")
        print_pause("YOU WIN!")
        print_pause(" ")
        play_again()

    else:
        print_pause("You feel a bit under-prepared for this, "
                    "considering you only have a tiny dagger.")
        print_pause("You do your best... ")
        print_pause(f"but your dagger is no match for the {monster}.")
        print_pause("You have been defeated!")
        print_pause(" ")
        play_again()


def field(items, monster):  # things that happen in the field
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n")
    # just printing the options, user input is defined in adventure_choices
    adventure_choices(items, monster)


def adventure_choices(items, monster):
    response = valid_input("1. House\n"
                           "2. Cave\n\n",
                           "1", "2")

    if response == '1':
        house(items, monster)
    elif response == '2':
        cave(items, monster)


def play_game():
    items = []
    monsters = ["dragon", "minotaur", "troll", "vampire",
                "werewolf", "yeti", "zombie"]
    # this list helps define monsters
    monster = random.choice(monsters)
    # it seems placing this monster variable here allows for random choice
    # but also keeps the monster consistent throughout each play_game instance
    game_intro(monster)
    field(items, monster)
    adventure_choices(items, monster)


def play_again():
    response = valid_input("Do you want to play again?\n"
                           "y - Play again\n"
                           "n - Quit game \n\n",
                           "y", "n").lower()

    if response == "y":
        print_pause("Great! Let's go on another adventure!")
        play_game()

    elif response == "n":
        print_pause("GAME OVER")
        print_pause(" ")
        print_pause("See you next time!")
        exit()  # exit not break here to exit the program completely


def play_adventure_game():
    play_game()
    play_again()


play_adventure_game()
