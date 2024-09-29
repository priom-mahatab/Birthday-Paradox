import random

#generates random birthdays
def random_birthdays():
    month = random.randint(1, 12)
    thirty_ones = [1, 3, 5, 7, 8, 10, 12]
    if month == 2:
        date = random.randint(1, 28)
    elif month in thirty_ones:
        date = random.randint(1, 31)
    else:
        date = random.randint(1, 30)
    birthday = f"{month}/{date}"
    return birthday

#checks if a birthday has a higher frequency than 1
def birthday_matched(n):
    birthdays = [random_birthdays() for _ in range(n)]
    return len(birthdays) != len(set(birthdays))

#calculates probability by having test cases from 5-100 and 1000 simulations per case
def birthday_paradox_simulation():
    test_cases = list(range(5, 105, 5))
    simulations = 1000

    print("n\tProbability of at least one match")

    for n in test_cases:
        match_count = 0
        for _ in range(simulations):
            if birthday_matched(n):
                match_count += 1

        probability = match_count / simulations
        print(f"{n}\t{probability:.2f}")

birthday_paradox_simulation()
