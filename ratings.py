"""Restaurant rating lister."""
from random import choice

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
            all_ratings[restaurant] = rating

    return all_ratings


def print_ratings(all_ratings):
    """
    Print out restaurant and rating pairs in alphabetical order
    """
    print("Here is the current list of all ratings:")
    for restaurant, rating in sorted(all_ratings.items()):
        print(f'{restaurant} is rated at {rating}.')


def add_restaurant_ratings(restaurant_ratings):
    """
    Allows the user to add new ratings and view full list"
    """

    new_restaurant = (input("what is the restaurant you want to judge? ")).title()

    while True:
        new_rating = input("what is your rating? ")
        try:
            new_rating = int(new_rating)
        except ValueError:
            print('You gotta enter a number!')
        else:
            if 0 < new_rating < 6:
                break
            else:
                print('You gotta enter a number from 1 to 5!')

    restaurant_ratings[new_restaurant] = new_rating


def open_menu():
    """
    Displays a menu for the user to view ratings, add rating, or quit.
    """

    print("Main Menu:")
    print("""
        What would you like to do?
        1: View all current ratings
        2: Add a new rating
        3: Update a random rating
        4: QUIT
        """)
    answer = input("> ")

    return answer


def random_rating(restaurant_ratings):
    """
    Picks a random restaurant for the user to review
    """
    rests = list(restaurant_ratings.keys())
    random_restaurant = choice(rests)

    print(f"""
        the chosen restaurant is {random_restaurant}
        with the rating {restaurant_ratings[random_restaurant]}
        """)

    new_rating = input("what should the new rating be? ")
    restaurant_ratings[random_restaurant] = new_rating


def exit_game(restaurant_ratings):
    """
    Says goodbye to the user and quits game
    """
    print('Thanks for rating restaurants! Final rating list:')
    print_ratings(restaurant_ratings)
    quit()


restaurant_ratings = get_ratings('scores.txt')

menu_action = {"1": print_ratings,
               "2": add_restaurant_ratings,
               "3": random_rating,
               "4": exit_game
               }

while True:
    # Print the menu and get user choice
    menu_choice = open_menu()
    menu_action[menu_choice](restaurant_ratings)
