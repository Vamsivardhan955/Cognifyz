import random
import string
import os

class Level2:
    @staticmethod
    def guessing_game():
        """
        Task 1: Guessing Game
        Generates a random number between 1 and 100. The user should guess the number, and the program provides hints.
        """
        target_number = random.randint(1, 100)
        user_guess = None
        while user_guess != target_number:
            user_guess = int(input("Guess the number between 1 and 100: "))
            if user_guess < target_number:
                print("Too low!")
            elif user_guess > target_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed it right!")

    @staticmethod
    def number_guesser():
        """
        Task 2: Number Guesser
        Generates a random number within a specified range, and the user tries to guess it. Provides feedback on guesses.
        """
        range_lower_bound = int(input("Enter the lower bound of the range: "))
        range_upper_bound = int(input("Enter the upper bound of the range: "))
        target_number = random.randint(range_lower_bound, range_upper_bound)
        user_guess = None
        while user_guess != target_number:
            user_guess = int(input(f"Guess the number between {range_lower_bound} and {range_upper_bound}: "))
            if user_guess < target_number:
                print("Too low!")
            elif user_guess > target_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed it right!")

    @staticmethod
    def password_strength_checker():
        """
        Task 3: Password Strength Checker
        Evaluates the strength of a password based on length, uppercase, lowercase letters, digits, and special characters.
        """
        user_password = input("Enter a password to check its strength: ")
        is_long_enough = len(user_password) >= 8
        has_uppercase = any(char.isupper() for char in user_password)
        has_lowercase = any(char.islower() for char in user_password)
        has_digit = any(char.isdigit() for char in user_password)
        has_special_char = any(char in string.punctuation for char in user_password)

        if is_long_enough and has_uppercase and has_lowercase and has_digit and has_special_char:
            print("Strong password")
        else:
            print("Weak password")

    @staticmethod
    def fibonacci_sequence():
        """
        Task 4: Fibonacci Sequence
        Generates the Fibonacci sequence up to a given number of terms and displays it.
        """
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        previous, current = 0, 1
        fibonacci_list = []
        for _ in range(num_terms):
            fibonacci_list.append(previous)
            previous, current = current, previous + current
        print("Fibonacci sequence:", fibonacci_list)

    @staticmethod
    def file_manipulation():
        """
        Task 5: File Manipulation
        Reads a text file and counts the occurrences of each word, displaying the results in alphabetical order.
        """
        file_path = input("Enter the filename to read (including extension): ").strip('\"\'')
        if os.path.isdir(file_path):
            print("The path provided is a directory. Please provide a file path.")
            return     
        word_count = {}
        try:
            with open(file_path, 'r') as file:
                file_content = file.read().lower()
                word_list = file_content.split()
                for word in word_list:
                    word_count[word] = word_count.get(word, 0) + 1
            sorted_word_count = sorted(word_count.items())
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")
        except PermissionError:
            print("Permission denied. Please check the file permissions and try again.")
        except OSError as os_error:
            print(f"OS error: {os_error}")

print("TASK 1:")
Level2.guessing_game()
print()
print("TASK 2:")
Level2.number_guesser()
print()
print("TASK 3:")
Level2.password_strength_checker()
print()
print("TASK 4:")
Level2.fibonacci_sequence()
print()
print("TASK 5:")
Level2.file_manipulation()
