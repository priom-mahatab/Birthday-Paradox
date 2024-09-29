# Birthday Paradox Simulation

This Python script simulates the **Birthday Paradox**, which explores the probability that, in a group of people, at least two will share the same birthday.

## How It Works

The script simulates the birthdays of people in groups of varying sizes and calculates the probability of at least one match (i.e., two people having the same birthday).

### Functions

1. **`random_birthdays()`**:
   - Generates a random birthday in the format `MM/DD`.
   - Takes into account the number of days in each month.
   - February is capped at 28 days (ignoring leap years for simplicity).

2. **`birthday_matched(n)`**:
   - Simulates `n` people and their birthdays.
   - Returns `True` if at least two people share the same birthday; otherwise, `False`.

3. **`birthday_paradox_simulation()`**:
   - Runs simulations for different group sizes (`n` ranging from 5 to 100 in steps of 5).
   - Runs 1000 simulations for each group size.
   - Calculates and prints the probability of at least one match for each group size.

### Output

The script prints the following table:

```
n    Probability of at least one match 
5     0.03 
10    0.12 
15    0.25 
...
```

Where `n` represents the group size and the probability is the estimated chance of two people sharing a birthday.

## Usage

To run the script, simply execute it using Python:

```bash
python birthday_paradox_simulation.py
```

If you're using Python 3 specifically, the command might need to be:

```bash
python3 birthday_paradox_simulation.py
```

### Dependencies

This script uses the built-in random module, so no external libraries are required.

### Concepts Covered

1. Birthday Paradox: The probability that in a group of n randomly chosen people, some pair of them will have the same birthday.
  
2. Probability Simulation: Uses Monte Carlo simulations to estimate the likelihood of shared birthdays.
