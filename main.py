from copy import *


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
class train_employee:  # a class to define train employee
    def __init__(self, nick_name, family_name, email, user_name, password):
        self.nick_name = nick_name
        self.family_name = family_name
        self.email = email
        self.user_name = user_name
        self.password = password


class line:  # a class to define lines
    def __init__(self, name, origin, destination, number_of_lines, stations):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.number = number_of_lines
        self.stations = stations


class train:  # a class to define train
    def __init__(self, name, line2, speed, stop_time, quality, price, capacity):
        self.name = name
        self.line = line2
        self.speed = speed
        self.stop_time = stop_time
        self.quality = quality
        self.price = price
        self.capacity = capacity


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# functions for sections :
# functions for sections :


def admin_pannel():
    print("1. Add an Employee")
    print("2. Delete an Employee")
    print("3. View Employees list")
    print("4. Exit")
    print("Enter Your Number:", end=" ")
    your_choice = int(input())
    return your_choice


def display_manu():  # a function to show main menu of program
    print("1. Main Admin")
    print("2. Train Employee")
    print("3. User")
    print("4. Exit")
    print("Enter your number:", end=" ")
    q = int(input())
    print("------------------")
    return q


def display_menu_s2():  # a function to show main menu of program section2 (sonra)
    print("1. Add a Line")
    print("2. Change Information About a Line")
    print("3. Delete a Line")
    print("4. Show List of Lines")
    print("5. Add a Train")
    print("6. Delete a Train")
    print("7. Show List of Trains")
    print("8. Log out")
    print("Enter Your Number:", end=" ")
    number3 = int(input())
    print("------------------")
    return number3


def exit_0(a):  # a function to exit the program if input == '0'
    if a == '0':
        return True


def show_line():  # a function to show all lines we have
    print("Enter Line name(press 0 for exit):", end=" ")
    line_2 = input()
    exit_0(line_2)  # for the part we said press 0 for exit
    if line_2 in line_names:  # if line was in list of lines we defined before, run this :
        print('1. Line name:', globals()[line_2].name)
        print('2. Line origin:', globals()[line_2].origin)
        print('3. line Destination:', globals()[line_2].destination)
        print('4. line number of lines:', globals()[line_2].number)
        print('5. line stations:', globals()[line_2].stations)
        print("6. exit")
        print('select the number you want to change:', end=' ')
        number3 = input()  # the number of up menu
        if number3 == '1':
            print("Enter your new name:", end=' ')
            new = input()  # new name we want to replace
            line_names.remove(globals()[line_2].name)  # remove the name from our list
            line_names.append(new)  # append new name to list
            globals()[line_2].name = new  # change name in class
            globals()[new] = copy(globals()[line_2])  # just ignore this line
            del globals()[line_2]  # delete previous class name ( we changed the name of class )
            line_2 = new  # just ignore this line
        if number3 == '2':
            print("Enter your new origin:", end=' ')
            new = input()
            globals()[line_2].origin = new
        if number3 == '3':
            print("Enter your new destination:", end=' ')
            new = input()
            globals()[line_2].destination = new
        if number3 == '4':
            print("Enter your new number of lines:", end=' ')
            new = input()
            globals()[line_2].number = new
        if number3 == '5':
            print("Enter your new station:", end=' ')
            new = input()
            globals()[line_2].stations = new
        if number3 == '6':
            pass
    else:
        print("we don't have this line yet")
        show_line()  # run all this function again if we didn't had the line


def del_line():  # a function to delete a line
    print("Enter line name:", end=' ')
    line_name = input()
    if line_name in line_names:  # if the line name given was in our line names list run :
        line_names.remove(line_name)  # remove name of line from our list
        del globals()[line_name]  # remove class of that line name
        print("line deleted!")
    else:
        print("line name is not correct")
        del_line()  # run all the function again if the line name was not in our list


def train_add():  # a function to add train
    print('enter train name(press 0 for exit):', end=' ')
    name_train = input()
    exit_0(name_train)  # exit if input == 0
    if name_train in train_list:  # if the train name given was in our train names list run :
        print('we already have this train')
        train_add()  # run all the function again
    else:
        print("Enter line:", end=' ')
        line2 = input()
        print("Enter speed:", end=' ')
        speed = input()
        print("Enter stop:", end=' ')
        stop = input()
        print("Enter quality:", end=' ')
        quality = input()
        print("Enter price:", end=' ')
        price = input()
        print("Enter capacity:", end=' ')
        capacity = input()
        # define a new class with name_train value as name:
        globals()[name_train] = train(name_train, line2, speed, stop, quality, price, capacity)
        # add name of train to train list
        train_list.append(globals()[name_train].name)
        print('train added!')


def del_train():  # function to delete a train
    print('Enter train name(or press 0 to exit):', end=' ')
    name = input()
    exit_0(name)  # exit if input == 0
    if name in train_list:  # if name was in the train list run :
        del globals()[name]  # delete the class of that name
        train_list.remove(name)  # remove the name of train from our list
        print('train deleted')
    else:
        print('we dont have this train')
        del_train()  # run all the function again


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# main body of section 1 ( Anahita )
# main body of section 1 ( Anahita )

def section1():
    print("Enter your username(enter 0 to exit) :", end=" ")
    user = input()
    if exit_0(user):
        display_manu()
    print("Enter your password(enter 0 to exit) :", end=" ")
    pas = input()
    if exit_0(pas):
        display_manu()
    print("------------------")
    if user == "Admin" and pas == "12345":
        print("Entering as the Main Admin....")
        while True:
            number1 = admin_pannel()
            match number1:
                case 1:
                    while True:
                        print("Enter employee nickname(enter 0 to exit):", end=" ")
                        nick_name = input()
                        if exit_0(nick_name):
                            break

                        print("Enter employee family name(enter 0 to exit):", end=" ")
                        family_name = input()
                        if exit_0(family_name):
                            break

                        print("Enter employee email(enter 0 to exit):", end=" ")
                        email = input()
                        if exit_0(email):
                            break
                        if any(globals()[obj1].email == email for obj1 in train_employee_list):
                            print("We already have this email!")
                            print("Please enter a new email.")
                            continue

                        print("Enter employee username(enter 0 to exit):", end=" ")
                        user_name = input()
                        if exit_0(user_name):
                            break
                        if any(globals()[obj2].user_name == user_name for obj2 in train_employee_list):
                            print("We already have this username!")
                            print("Please enter a new username.")
                            continue

                        print("Enter employee password(enter 0 to exit):", end=" ")
                        password = input()
                        if exit_0(password):
                            continue

                        employee = train_employee(nick_name, family_name, email, user_name, password)
                        globals()[user_name] = employee
                        train_employee_list.append(user_name)
                        print("Employee added!")
                        break
                case 2:
                    print("Enter username of the employee you want to delete(enter 0 to exit):", end=" ")
                    del_user = input()
                    if exit_0(del_user):
                        continue
                    if del_user in train_employee_list:
                        del globals()[del_user]
                        train_employee_list.remove(del_user)
                        print('Employee deleted')
                    else:
                        print("The username doesn't exist is employee list!")
                        continue
                case 3:
                    print("Here's employees list :")
                    for emp in train_employee_list:
                        employee = globals()[emp]
                        print('----------------------------')
                        print(f"Nickname : {employee.nick_name}")
                        print(f"Family name : {employee.family_name}")
                        print(f"Email : {employee.email}")
                        print(f"Username : {employee.user_name}")
                        print(f"Password : {employee.password}")
                        print('----------------------------')
                case 4:
                    print("Bye Bye 2 !")
                    return 0
    else:
        print("Username or passowrd in incorrect.")
        section1()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# main body of section 2 ( Sonra )
# main body of section 2 ( Sonra )
def section2():
    # login process:
    print("Enter Your Username:", end=" ")
    user = input()
    print("Enter Your Password:", end=" ")
    pas = input()
    if user in train_employee_list and (globals()[user].password == pas):
        print("User and password is correct!")
        number2 = display_menu_s2()  # display the menu of section2
        if number2 == 1:
            print("Enter name(press 0 if you want to exit):", end=" ")
            name_1 = input()
            exit_0(name_1)  # exit if input == 0
            while name_1 in line_names:  # run the program until user give a new name(we can't define old names again)
                print("we already have this name")
                print("Enter name(press 0 if you want to exit):", end=" ")
                name_1 = input()
                exit_0(name_1)
            print("Enter origin name(press 0 if you want to exit):", end=" ")
            origin_name_1 = input()
            exit_0(origin_name_1)
            print("Enter destination name(press 0 if you want to exit):", end=" ")
            destination_name_1 = input()
            exit_0(destination_name_1)
            print("Enter number of lines(press 0 if you want to exit):", end=" ")
            number_of_lines_1 = input()
            exit_0(number_of_lines_1)
            station_names = list()  # a list for stations ( we can have more than a station )
            while True:
                print("Enter station name or 0 if it's done")
                station = input()
                if station == '0':
                    break
                station_names.append(station)
            line_names.append(name_1)  # add line name to our list
            # define a class for this name with given details:
            globals()[name_1] = line(name_1, origin_name_1, destination_name_1, number_of_lines_1, station_names)
            print("Line Added! ")
        elif number2 == 2:  # show all the lines and change the details
            show_line()

        elif number2 == 3:  # delete a line
            del_line()

        elif number2 == 4:  # show all the lines with their information
            for i in line_names:
                print("details of line:", i)
                print('name:', globals()[i].name)
                print('origin:', globals()[i].origin)
                print('destination:', globals()[i].destination)
                print('number of line:', globals()[i].number)
                print('stations:', globals()[i].stations)
                print('--------------')
        elif number2 == 5:  # add train
            train_add()
        elif number2 == 6:  # delete the train
            del_train()
        elif number2 == 7:  # show all the trains with their information
            for i in train_list:
                print("details of train:", i)
                print('name:', globals()[i].name)
                print('line:', globals()[i].line)
                print('speed:', globals()[i].speed)
                print('stop time:', globals()[i].stop_time)
                print('quality:', globals()[i].quality)
                print('price:', globals()[i].price)
                print('capacity:', globals()[i].capacity)
                print('--------------')

        elif number2 == 8:  # log out
            pass
    else:  # run the program again if user pass was wrong
        print("User or Password is wrong")
        section2()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# main body of section 3 ( Fatemeh )
# main body of section 3 ( Fatemeh )

def section3():
    pass


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# main body of all the program


train_employee_list = list()  # list of employs
# train_employee_list.append('ali')  # it just for test and it will be deleted
train_list = list()  # list of trains
# ali = train_employee('ali', 'ali', 'email', 'ali', 'pass')  # it just for test and it will be deleted
line_names = list()  # list of line names
# line_names.append('ali2')  # it just for test and it will be deleted
# ali2 = line('ali2', 'ali2', 'ali3', 'ali4', "ali5")  # it just for test and it will be deleted
while True:
    number = display_manu()
    if number == 1:
        section1()
    elif number == 2:
        section2()
    elif number == 3:
        section3()
    elif number == 4:
        print("Bye Bye Nasr!")
        exit()
    else:
        print("your number was out of range. please enter again !")
        display_manu()
