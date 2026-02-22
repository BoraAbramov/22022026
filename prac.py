
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
    for i in list_ages:
        if max(i) < new_age:
            print("oldest")
        if min(i) > new_age:
            print("youngest")
        if max(i) > new_age > min(i):
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

