import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
nr_letters = int(input("How many letters? "))
nr_numbers = int(input("How many numbers? "))
nr_symbols = int(input("How many symbols? "))

password = []
password.extend(random.choice(letters) for _ in range(nr_letters))
password.extend(random.choice(numbers) for _ in range(nr_numbers))
password.extend(random.choice(symbols) for _ in range(nr_symbols))

random.shuffle(password)
print("Your strong password:", ''.join(password))