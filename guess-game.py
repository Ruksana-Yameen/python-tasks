import random
min_num = 1
max_num = 100

random_number = random.randint(min_num, max_num)

print("Guess a number between", min_num, "and", max_num)
guess = int(input("Enter your guess: "))

if guess == random_number:
    print("Congratulations! Your guess is correct.")
else:
    print("Sorry, your guess is incorrect. The number was:", random_number)
