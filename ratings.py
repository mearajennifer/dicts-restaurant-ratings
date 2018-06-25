"""Restaurant rating lister."""


# put your code here
# Read the ratings from the file
# Store them in a dictionary
# Spit out the ratings in alphabetical order

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


def add_view_restaurant_ratings():
    """
    Allows the user to add new ratings and view full list"
    """

    restaurant_ratings = get_ratings('scores.txt')

    new_restaurant = (input("what is the restaurant you want to judge? ")).title()
    new_rating = input("what is your rating? ")

    restaurant_ratings[new_restaurant] = new_rating
    print_ratings(restaurant_ratings)


add_view_restaurant_ratings()