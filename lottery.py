import random

def menu():
    # Ask player for numbers
    user_numbers = get_player_numbers()

    # Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()

    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {}. You won ₱{}!".format(matched_numbers, 100 ** len(matched_numbers)))


# User can pick 6 numbers
def get_player_numbers():
    number_csv = input("Enter your 6 numbers from 1 to 20, separated by commas: ")
    # Now, I want to create a set of integers from this number_csv


# Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()  # Cannot initialise like so: {}
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

#missing code - can be provided upon request.