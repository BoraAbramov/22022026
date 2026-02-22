
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
        for i in list1:
            if i % 2 == 0:
                list1.remove(i)
        print(list1)
    if even == False:
        for i in list1:
            if i % 2 != 0:
                list1.remove(i)
        print(list1)

remove_odd_even([1, 3, 5, 6, 8, 9], True)