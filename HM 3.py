
import random

def get_random_between_1_10():
    return random.randint(1, 10)

def get_random_operation():
    return random.choice(['+', '-', '*', '%'])

def calc_result(a, b, c):
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    elif b == '%':
        return a % c


num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = int(input('whats the result? '))

if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")