import random
import time

def generate_secret_number(difficulty):
    if difficulty == "easy":
        return random.randint(1, 50)
    elif difficulty == "medium":
        return random.randint(1, 100)
    else:
        return random.randint(1, 200)

def main():
    print("Welcome to the Enhanced Number Guessing Game!")
    rounds = 0
    total_attempts = 0

    while True:
        difficulty = input("\nChoose a difficulty level (easy/medium/hard): ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")
            continue

        secret_number = generate_secret_number(difficulty)
        attempts = 0
        max_attempts = 7 if difficulty == "easy" else 5 if difficulty == "medium" else 3
        start_time = time.time()

        print(f"\nI'm thinking of a number between 1 and 100 (for {difficulty} mode).")
        while True:
            try:
                guess = int(input("Can you guess the number? Enter your guess: "))
                attempts += 1

                if guess < secret_number:
                    print("The number is higher. Try again.")
                elif guess > secret_number:
                    print("The number is lower. Try again.")
                else:
                    end_time = time.time()
                    elapsed_time = int(end_time - start_time)
                    print(f"Congratulations! You've guessed the number ({secret_number}) in {attempts} attempts.")
                    total_attempts += attempts
                    rounds += 1
                    print(f"Time taken: {elapsed_time} seconds")
                    break

                if attempts >= max_attempts:
                    print("You've reached the maximum number of attempts. The secret number was", secret_number)
                    break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"\nYou played {rounds} round(s) with an average of {total_attempts / rounds:.2f} attempts per round.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
