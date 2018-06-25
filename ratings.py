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
        for line in filename.rstrip():
            for restaurant, rating in line.split(":"):
                all_ratings[restaurant] = rating

    return all_ratings


print(all_ratings)
