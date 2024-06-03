def exit_0(a):  
    if a == '0':
        return True

def admin_pannel() :
    print("1. Add an Employee")
    print("2. Delete an Employee")
    print("3. View Employees list")
    print("4. Exit") 
    print("Enter Your Number:", end=" ") 
    your_choice = int(input())
    return your_choice    

train_employee_list = list() 

def section1() :

    print("Enter your username(enter 0 to exit) :", end=" ")
    user = input()
    if exit_0(user) :
        display_menu()
    print("Enter your password(enter 0 to exit) :" , end=" ")
    pas = input() 
    if exit_0(pas) :
        display_menu()  
    print("------------------")
    if user == "Admin" and pas == "12345" :
        print("Entering as the Main Admin....") 
        while True :
            number1 = admin_pannel()
            match number1 :
                case 1 :
                    while True :
                        print("Enter employee nickname(enter 0 to exit):",end=" ") 
                        nick_name = input()
                        if exit_0(nick_name) :
                            break

                        print("Enter employee family name(enter 0 to exit):", end=" ") 
                        family_name = input()
                        if exit_0(family_name) :
                            break

                        print("Enter employee email(enter 0 to exit):", end=" ")
                        email = input()
                        if exit_0(email) :
                            break 
                        if any(globals()[obj1].email == email for obj1 in train_employee_list) : 
                            print("We already have this email!") 
                            print("Please enter a new email.")  
                            continue

                        print("Enter employee username(enter 0 to exit):", end=" ")
                        user_name = input() 
                        if exit_0(user_name) : 
                            break 
                        if any(globals()[obj2].user_name == user_name for obj2 in train_employee_list) : 
                            print("We already have this username!") 
                            print("Please enter a new username.")  
                            continue

                        print("Enter employee password(enter 0 to exit):", end=" ")
                        password = input()
                        if exit_0(password) :
                            continue

                        employee = train_employee(nick_name, family_name, email, user_name, password)
                        globals()[user_name] = employee
                        train_employee_list.append(user_name) 
                        print("Employee added!") 
                        break

                case 2 :
                    print("Enter username of the employee you want to delete(enter 0 to exit):",end=" ") 
                    del_user = input() 
                    if exit_0(del_user) :
                        continue 
                    if del_user in train_employee_list :
                        del globals()[del_user]  
                        train_employee_list.remove(del_user) 
                        print('Employee deleted')
                    else :
                        print("The username doesn't exist is employee list!") 
                        continue
                case 3 :
                    print("Here's employees list :") 
                    for emp in train_employee_list :
                        employee = globals()[emp] 
                        print(f"Nickname : {employee.nick_name}")
                        print(f"Family name : {employee.family_name}")
                        print(f"Email : {employee.email}")
                        print(f"Username : {employee.user_name}")
                        print(f"Password : {employee.password}")
                case 4 :
                    print("Bye Bye 2 !") 
                    return 0
    else :
        print("Username or passowrd in incorrect.") 
        section1()  
   

def display_menu(): 
    while True : # a function to show main menu of program
        print("1. Main Admin")
        print("2. Train Employee")
        print("3. User")
        print("4. Exit")
        print("Enter your number:", end=" ")
        number = int(input())
        print("------------------")
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

display_menu()
