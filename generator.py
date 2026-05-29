# Project: Secure Password Generator and Strength Checker.
# Data Structure: Character Strings and Randomized Arrays.
# Description: Generates secure passwords using built-in input verification guards.

import random
import string

print("=== SAFE PASSWORD GENERATOR ===")

# Define character building blocks using built-in string tools
letters = string.ascii_letters  
digits = string.digits          
symbols = string.punctuation    

# Combine all elements into a single lookup pool
all_characters = letters + digits + symbols

while True:
    user_input = input("\nEnter password length (or type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    # Safety Check: Guard against text inputs that would crash the code
    if not user_input.isdigit():
        print("Please enter a valid number!")
        continue
        
    length = int(user_input)
    
    if length < 8:
        print("Security Warning: Passwords should be at least 8 characters long.")
    
    # Generate password by picking random characters from our pool
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
        
    print(f"Your secure password is: {password}")
