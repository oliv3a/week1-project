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




# ====== Tiny Log Analyzer ======

def count_errors(log_file):
    count = 0
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    return count

error_count = count_errors("logs.txt")
print(f"Total ERROR entries: {error_count}")


# ====== Improved Log Analyzer ======

def analyze_logs(log_file):
    stats = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(log_file, "r") as file:
        for line in file:
            for level in stats:
                if level in line:
                    stats[level] += 1

    return stats


results = analyze_logs("logs.txt")

for level, count in results.items():
    print(f"{level}: {count}")
