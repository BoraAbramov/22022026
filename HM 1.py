
import time

def num_print(start, stop):
    _st_list = []
    if start < stop:
        _min = start
        _max = stop
    if start > stop:
        _min = stop
        _max = start

    i = _min
    while i < _max + 1:
        _st_list.append(i)
        i += 1

    if start < stop:
        for item in _st_list:
            print(item, end=" ")
            time.sleep(0.5)
    if start > stop:
        for item in _st_list[::-1]:
            print(item, end=" ")
            time.sleep(0.5)


print("please follow the instruction and the program will print all numbers in between")

time.sleep(1)
num1 = 0
num2 = 0

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



