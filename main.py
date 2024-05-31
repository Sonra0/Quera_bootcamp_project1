from Train_employee import train_employee
train_employee_dict = {} 
class Admin :
    admins_info = {} 

    def __init__(self,username,password) :
        self.username = username
        self.password = password
        Admin.admins_info[username] = password 

    def check_id(cls,username,password) : 
        if username in cls.admins_info and cls.admins_info[username] == password : 
            return True
        return False


def admin_section() :

    print("Enter your username :", end=" ")
    user = input()
    print("Enter your password :" , end=" ")
    pas = input() 
     
    
    if user in Admin.admins_info :
        if pas == Admin.admins_info[user] :
            print("Entering as the Main Admin.") 
            def admin_pannel() :
                print("1. Add an Employee")
                print("2. Delete an Employee")
                print("3. View Employees")
                print("4. Log out")
                print("Enter Your Number:", end=" ")
                your_choice = int(input())
                return your_choice

            while True :
                number1 = admin_pannel()  
                match number1 :
                    case 1 :
                        print("Enter employee nickname :",end=" ")
                        nick_name = input()
                        print("Enter employee family name:", end=" ") 
                        family_name = input()
                        print("Enter employee email:", end=" ")
                        email = input()
                        print("Enter employee username:", end=" ")
                        user_name = input()
                        print("Enter employee password:", end=" ")
                        password = input()
                        train_employee(nick_name, family_name, email, user_name, password)
                        print("Employee added!") 
                    case 2 :
                        pass
                    case 3 :
                        pass
                    case 4 :
                        print("Bye Bye 2 !") 
                        break 
        else :
            print("Username or passowrd in incorrect.")
            admin_section()
    else :
        print("Username or passowrd in incorrect.") 
        admin_section() 

Admin("Admin","12345")   
