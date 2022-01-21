import random

avengers = ["Iron man", "Thor", "Spindelmannen", "Hulken", "Captian America" ]
dc = ["Batman", "Superman", "Flash", "Aquaman", "Superwoman"]

hjältar = avengers + dc

def select_random_Ns(hjältar, n)
    random.shuffle(hjältar)
    result = []