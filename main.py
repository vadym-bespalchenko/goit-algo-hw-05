#Завдання 1

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()

print(fib(5))
print(fib(10))

#Завдання 2

import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total_profit = sum(numbers_generator)
    return total_profit

# Приклад використання
text = "Profit for this quarter: 100.25  -10.5 8.75 120.6"
total_profit = sum_profit(text, generator_numbers)
print("Total profit:", total_profit)

#Завдання 4

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid input."
        except IndexError:
            return "Error: Insufficient arguments."
    return wrapper

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def close_bot():
    return "Good bye!"

@input_error
def greet():
    return "How can I help you?"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(close_bot())
            break
        elif command == "hello":
            print(greet())
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

