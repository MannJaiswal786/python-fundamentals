# import random

# def guess_random_number(tries, start, stop):
#     target_number = random.randint(start, stop)

#     while tries != 0:
#         print(f"\nTries left: {tries}")
#         try:
#             guess = int(input("Enter your guess: "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

#         if guess == target_number:
#             print("Congratulations! You guessed the correct number!")
#             return
#         elif guess < target_number:
#             print("Guess Higher")
#         else:
#             print("Guess Lower")

#         tries -= 1  # This should be outside the if-else block

#     # This should also be outside the while loop
#     print(f"Sorry, you are out of tries. The number was {target_number}")

# guess_random_number(5, 1, 10)

# import random

# def guess_random_num_linear(tries, start, stop):
#     target_number = random.randint(start, stop)

#     for guess in range(start, stop + 1):
#         if tries == 0:
#             print("Out of tries! Pc failed to guess the number")
#             print(f"The number was {target_number}")
#             return
        
#         print(f"computer guesses: {guess}")
#         tries -= 1

#         if guess == target_number:
#             print("The computer successfully guessed the number!")
#             return
        
#     print("Computer did not guess the number")
#     print(f"The number was {target_number}")

# guess_random_num_linear(5, 1, 10)

import random

def guess_random_num_binary(tries, start, stop):
    target_num = random.randint(start, stop)
    print(f"Target number (hidden): {target_num}")

    low = start
    high = stop

    while tries > 0 and low <= high:
        guess = (low + high) // 2
        print(f"Computer guesses: {guess}")
        tries -= 1

        if guess == target_num:
            print(f"The computer successfully guessed the number")
            return
        
        elif guess < target_num:
            print("Guess is low")
            low = guess + 1
        else:
            print("Guess is high")
            high = guess - 1

        print("The computer failed to guess the number within the allowed tries.")
        print(f"The number was {target_num}")

guess_random_num_binary(5, 1, 100)