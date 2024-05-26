class train_employee:
    def __init__(self, nick_name, family_name, email, user_name, password):
        self.nick_name = nick_name
        self.family_name = family_name
        self.email = email
        self.user_name = user_name
        self.password = password


def display_manu():
    print("1. Main Admin")
    print("2. Train Employee")
    print("3. User")
    print("4. Exit")
    print("Enter your number:", end=" ")
    q = int(input())
    return q


def section1():
    pass
def section2():
    pass
def section3():
    pass

train_employee_list = []

a = display_manu()
if a == 1:
    pass
elif a == 2:
    pass
elif a == 3:
    pass
elif a == 4:
    print("Bye Bye Nasr!")
    exit()
else:
    print ("your number was out of range. please enter again !")
    display_manu()
