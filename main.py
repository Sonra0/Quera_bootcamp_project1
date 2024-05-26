from copy import *
class train_employee:
    def __init__(self, nick_name, family_name, email, user_name, password):
        self.nick_name = nick_name
        self.family_name = family_name
        self.email = email
        self.user_name = user_name
        self.password = password


class line:
    def __init__(self, name, origin, destination, number_of_lines, stations):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.number = number_of_lines
        self.stations = stations

class train:
    def __init__(self,name,line,speed,stop_time,quality,price,capacity):
        self.name = name
        self.line = line
        self.speed = speed
        self.stop_time = stop_time
        self.quality = quality
        self.price = price
        self.capacity = capacity

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
    print("Enter Your Username:",end=" ")
    user = input()
    print("Enter Your Password:",end=" ")
    pas = input()

    def display_menu():
        print("1. Add a Line")
        print("2. Change Information About a Line")
        print("3. Delete a Line")
        print("4. Show List of Lines")
        print("5. Add a Train")
        print("6. Delete a Train")
        print("7. Show List of Trains")
        print("8. Log out")
        print("Enter Your Number:", end=" ")
        number = int(input())
        return number

    if user in train_employee_list:
        if(globals()[user].password==pas):
            print("User and password is correct!")
            number2 = display_menu()
            if number2 == 1:
                print("Enter name(press 0 if you want to exit):", end=" ")
                name_1 = input()
                if name_1 == '0':
                    return False
                while name_1 in line_names:
                    print("we already have this name")
                    print("Enter name(press 0 if you want to exit):", end=" ")
                    name_1 = input()
                    if name_1 == '0':
                        return False
                print("Enter origin name(press 0 if you want to exit):", end=" ")
                origin_name_1 = input()
                if origin_name_1 == '0':
                    return False
                print("Enter destination name(press 0 if you want to exit):", end=" ")
                destination_name_1 = input()
                if destination_name_1 == '0':
                    return False
                print("Enter number of lines(press 0 if you want to exit):", end=" ")
                number_of_lines_1 = input()
                if number_of_lines_1 == '0':
                    return False
                station_names = list()
                while True:
                    print("Enter station name or 0 if it's done")
                    station = input()
                    if station == '0':
                        break
                    station_names.append(station)
                line_names.append(name_1)
                globals()[name_1] = line(name_1,origin_name_1,destination_name_1,number_of_lines_1,station_names)
                print("Line Added! ")
            elif number2 == 2:
                def show_line():
                    print("Enter Line name(press 0 for exit):", end=" ")
                    line_2 = input()
                    if line_2 == '0':
                        return 0
                    if line_2 in line_names:
                        print('1. Line name:',globals()[line_2].name)
                        print('2. Line origin:',globals()[line_2].origin)
                        print('3. line Destination:',globals()[line_2].destination)
                        print('4. line number of lines:',globals()[line_2].number)
                        print('5. line stations:',globals()[line_2].stations)
                        print("6. exit")
                        print('select the number you want to change:', end=' ')
                        number3 = input()
                        if number3 == '1':
                            print("Enter your new name:",end=' ')
                            new = input()
                            line_names.remove(globals()[line_2].name)
                            line_names.append(new)
                            globals()[line_2].name = new
                            globals()[new] = copy(globals()[line_2])
                            del globals()[line_2]
                            line_2 = new
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
                        show_line()
                show_line()

            elif number2 == 3:
                def del_line():
                    print("Enter line name:",end=' ')
                    line_name = input()
                    if line_name in line_names:
                        line_names.remove(line_name)
                        del globals()[line_name]
                        print("line deleted!")
                    else:
                        print("line name is not correct")
                        del_line()
                del_line()
            elif number2 == 4:
                for i in line_names:
                    print("details of line:",i)
                    print('name:',globals()[i].name)
                    print('origin:', globals()[i].origin)
                    print('destination:', globals()[i].destination)
                    print('number of line:', globals()[i].number)
                    print('stations:', globals()[i].stations)
                    print('--------------')
            elif number2 == 5:
                def train_add():
                    print('enter train name(press 0 for exit):',end=' ')
                    name_train = input()
                    if name_train == '0':
                        return 0
                    if name_train in train_list:
                        print('we already have this train')
                        train_add()
                    else:
                        print("Enter line:",end=' ')
                        line = input()
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
                        globals()[name_train] = train(name_train,line,speed,stop,quality,price,capacity)
                        train_list.append(globals()[name_train].name)
                        print('train added!')
                train_add()
            elif number2 == 6:
                def del_train():
                    print('Enter train name(or press 0 to exit):',end=' ')
                    name = input()
                    if name == '0':
                        return 0
                    elif name in train_list:
                        del globals()[name]
                        train_list.remove(name)
                        print('train deleted')
                    else:
                        print('we dont have this train')
                        del_train()
                del_train()
            elif number2 == 7:
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

            elif number2 == 8:
                pass

        else:
            print("User or Password is wrong")
            section2()
    else:
        print("User or Password is wrong")
        section2()

def section3():
    pass


train_employee_list = list()
train_employee_list.append('ali')
train_list = list()
ali = train_employee('ali','alii','email','ali','pass')
line_names = list()
line_names.append('ali2')
ali2 = line('ali2','ali2','ali3','ali4',"ali5")
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
    print('------------------')
