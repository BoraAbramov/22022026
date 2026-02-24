
import time

def num_print(start, stop):
    _st_list = []
    if start < stop:
        _min = start
        _max = stop
    elif start > stop:
        _min = stop
        _max = start

    i = _min
    while i < _max + 1:
        _st_list.append(i)
        i += 1

    if start > stop:
        _st_list(reversed = True)
        print(_st_list)
    elif start < stop:
        print(_st_list)
    else:
        print(start)

print("please follow the instruction and the program will print all numbers in between")

time.sleep(2)

while True:
    num1 = input("Enter first number: ")
    if num1.isdigit():
        num2 = input("Enter second number: ")
        if num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            break
    else:
        continue

num_print(num1, num2)



