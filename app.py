print('hello world')
print("Learning Git is fun!")
print("Branching is awesome!")
print("Practicing on feature-1 branch!")

# ====== Greeting experiments ======
def greet(name):
    print(f"Hello, {name}!")

greet("Git Learner")


# ====== Math experiment ======
def add_numbers(a, b):
    print(f"{a} + {b} = {a + b}")

add_numbers(5, 7)


# ====== If/Else + Loop practice ======
def check_number(n):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

for i in range(1, 6):
    check_number(i)


import random
import string

def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    password = "".join(random.choice(chars) for _ in range(length))
    return password

print(generate_password())
