from Train_employee import train_employee 
class Admin :
    #admins_info = {} 
    def __init__(self,username,password) :
        self.username = username
        self.password = password
        #Admin.admins_info[username] = password 
    def check_id(self,entered_username,entered_password) :
        if self.username == entered_username and self.password == entered_password :
            return True
        return None

def main_menu() :
    print("1. Admin")
    print("2. Train Employee")
    print("3. User") 
    print("4. Exit")
    print("Enter your number:", end=" ")
    return int(input()) 

def admin_section() :

    print("Enter your username : ")
    entered_username = input()
    print("Enter your password : ")
    entered_pass = input() 
    admin  = Admin.check_id(entered_username,entered_pass)

    def admin_pannel() :
        print("1. Add an Employee")
        print("2. Delete an Employee")
        print("3. View Employees")
        print("4. Log out")
        print("Enter Your Number:", end=" ")
        your_choice = int(input())
        return your_choice 
    
     
    if admin :
        print("Entering as the Main Admin....")  
        number1 = admin_pannel()
        while True :
            
            match number1 :
                case 1 :
                    print("Enter employee nickname : ")
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
                    break 
def login() :
    Admin("Admin","12345")    
