import random

avengers = ["Iron man", "Thor", "Spindelmannen", "Hulken", "Captian America" ]
dc = ["Batman", "Superman", "Flash", "Aquaman", "Superwoman"]

hjältar = avengers + dc

def select_random_Ns(hjältar, n)
    random.shuffle(hjältar)
    result = []
    for i in range(0, len(hjältar), n):
    result.append(hjältar[i:i + n])
    return result


print(select_random_Ns(hjältar, 2))
