
def divide(num1,num2):
    if num2 == 0:
        print("cannot divide by zero")
    else:
        answer = num1/num2
        print(answer)

#num1 = int(input("enter first number"))
#num2 = int(input("enter second number"))

#divide(num1,num2)


def even_odd(num):
    if num % 2 == 0:
        print("even number")
    else :
        print("odd number")

#num = int(input("enter a number: "))
#even_odd(num)

def age_title(list_ages, new_age):
        if max(list_ages) < new_age:
            print("oldest")
        if min(list_ages) > new_age:
            print("youngest")
        if max(list_ages) > new_age > min(list_ages):
            print("between")

#new_age = int("age please")
#age_title()

def intruders(invited_set, participants_set):
    print(f"people that not invited {participants_set - invited_set}")

invited = {
    "Alice Thompson",
    "Marcus Chen",
    "Elena Rodriguez",
    "Julian Vance",
    "Sarah Jenkins",
    "Kofi Mensah",
    "Priya Sharma",
    "Oliver Sterling",
    "Naomi Wattson",
    "Liam O'Connor"
}
paritcipants = {
    "Silas Vance",
    "Julian Vance",
    "Sarah Jenkins",
    "Maeve O'Sullivan",
    "Kofi Mensah",
    "Cassian Thorne"
}

#intruders(invited, paritcipants)

def remove_odd_even(list1, even):
    if even == True:
        for i in set(list1):
            if i % 2 == 0:
                list1.remove(i)
        print(list1)
    if even == False:
        for i in set(list1):
            if i % 2 == 1:
                list1.remove(i)
        print(list1)


def big_and_small(a: int, b: int, c: int):
    return max(a, b, c), min(a, b, c)


def get_grade_value(grade: int) -> str:
    if 80 <= grade <= 100:
        return "A"
    elif grade >= 60:
        return "B"
    elif grade >= 40:
        return "C"
    elif grade >= 0:
        return "D"


def calc_statistics(grades: list, oper: str) -> int:
    import statistics
    if oper == "maximum":
        return max(grades)
    if oper == "minimum":
        return min(grades)
    if oper == "average":
        return statistics.mean(grades)
    if oper == "sum":
        return sum(grades)
    if oper == "length":
        return len(grades)

#print(calc_statistics ([40, 50, 60], "maximum"))  # 60
#print(calc_statistics ([40, 50, 60], "minimum"))  # 40
#print(calc_statistics ([40, 50, 60], "length"))  # 3
#print(calc_statistics ([40, 50, 60], "sum"))  # 150
#print(calc_statistics ([40, 50, 60], "average"))  # 50


