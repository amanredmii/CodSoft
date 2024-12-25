import random
import string

print("\n-Random Password Generator-")

def gen_pass(len):
    if len < 4:
        return "\nPc : Minimun length should be 4 to generate a random password..!!"
    
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_characters, k=len - 4)

    random.shuffle(password)
    
    return ''.join(password)

try:
    len = int(input("\nPc : Enter the length of the password..!!\nUser : "))
    if len<4:
        print(gen_pass(len))
    else:
        print(f"\nPc : Generated Password is {gen_pass(len)}")

except ValueError:
    print("\nPc : Enter a valid integer for the password length..!!")