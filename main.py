# Today I am creating a password Generator program
import random
import string # I will be working with characters to strings

def create_password(length:int) -> str: #returns string
    if length < 4:
        raise ValueError('Password is too short!')
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    password.append(random.choice(string.ascii_lowercase)) # Start to add
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    password += random.choice(characters, k=length -4) 
    random.shuffle(password) # For a more stronger password
    return "".join(password) # As a single string hence join()

def main() -> None: # void
    try:
        length = int(input('[PASSWORD LENGTH]: ')
        
    except (TypeError, ValueError) as err:
         print(f'[ERROR] {err}')
