import random

print("Hello! Im going to try to guess your age.)
name = input(Whats your name? ")

while True:
    age_guess = random.randint(15, 30)
    answer = input(f"Is your age {age_guess}? (y/n): ").strip().lower()

    if answer == y:
        print(f"Hooray! {name} is {age_guess} years old.")
        break
    else:
        print("Rats.")
