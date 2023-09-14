import random

# generates a unique seed based off the users month of birth to be used in generating a cypher

def random_seeded(month):
    random.seed(month)
    seed = random.randrange(0, 10, 1)
    return seed
