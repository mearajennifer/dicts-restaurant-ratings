"""Restaurant rating lister."""
from random import choice
from statistics import mean
import os


# put your code here
def get_ratings(filename):
    """
    Reads file and returns restaurants and ratings in a dictionary.
    """

    all_ratings = {}

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            restaurant, rating = line.split(":")
            all_ratings[restaurant] = int(rating)

    return all_ratings


def get_user_rating():
    """
    Asks user for new rating, verifies it is a number and from 1 to 5.
    """
    while True:
        new_rating = input("\nNEW RATING: ")
        try:
            new_rating = int(new_rating)
        except ValueError:
            print('You gotta enter a number!')
        else:
            if 0 < new_rating < 6:
                break
            else:
                print('You gotta enter a number from 1 to 5!')

    return new_rating


def print_ratings(all_ratings):
    """
    Print out restaurant and rating pairs in alphabetical order
    """
    print("\nRESTAURANT RATINGS:")
    for restaurant, rating in sorted(all_ratings.items()):
        print(f'        {restaurant} is rated at {rating}.')


def add_restaurant_ratings(restaurant_ratings):
    """
    Allows the user to add new ratings and view full list"
    """

    new_restaurant = (input("\nNEW RESTAURANT: ")).title()

    new_rating = get_user_rating()

    restaurant_ratings[new_restaurant] = new_rating


def open_menu():
    """
    Displays a menu for the user to view ratings, add rating, or quit.
    """

    print("""\nMAIN MENU:
        1: View all current ratings
        2: Add a new rating
        3: Update a random rating
        4: Choose a rating to update
        5: QUIT
        """)
    answer = input("> ")

    return answer


def random_rating(restaurant_ratings):
    """
    Picks a random restaurant for the user to review
    """
    all_rests = list(restaurant_ratings.keys())
    rand_rest = choice(all_rests)

    rand_rest_text = """
    RESTAURANT: {}
    CURRENT RATING: {}"""

    print(rand_rest_text.format(rand_rest, restaurant_ratings[rand_rest]))

    new_rating = get_user_rating()

    restaurant_ratings[rand_rest] = new_rating


def choose_rating(restaurant_ratings):
    """
    Allows user to select a restaurant and update the rating.
    """

    # Enter into loop asking for user choice until they enter a value in the dict
    while True:
        user_rest_choice = (input("\nRESTAURANT: ")).title()

        if user_rest_choice in restaurant_ratings:
            break
        else:
            print("You gotta put in a restaurant that is in the list!")

    print(f"CURRENT RATING: {restaurant_ratings[user_rest_choice]}")

    new_rating = get_user_rating()

    restaurant_ratings[user_rest_choice] = new_rating


def exit_game(restaurant_ratings):
    """
    Says goodbye to the user and quits game
    """
    goodbye = """
    Thanks for rating restaurants!
    You've rated {} restaurants with an average rating of {:.2}.
    """

    num_rests = len(restaurant_ratings.keys())
    average = mean(restaurant_ratings.values())

    # Print goodbye message and customize with number of reviews and their average score
    print(goodbye.format(num_rests, average))
    quit()


# Start main program
print("WELCOME TO RATE-O-MATIC\n")
print("Please choose a restaurant rating file:")

# List all text files in currect directory
for file in os.listdir():
    if file[-3:] == 'txt':
        print(f"-- {file}")

# Get user file choice and use to create ratings dictionary
ratings_txt = input("> ")
restaurant_ratings = get_ratings(ratings_txt)

menu_action = {"1": print_ratings,
               "2": add_restaurant_ratings,
               "3": random_rating,
               "4": choose_rating,
               "5": exit_game
               }

while True:
    # Print the menu, get user choice, use menu_action dictionary to complete action
    menu_choice = open_menu()
    menu_action[menu_choice](restaurant_ratings)
