def display_manu():
    print("1. Main Admin")
    print("2. Train Employee")
    print("3. User")
    print("4. Exit")
    print("Enter your number:", end=" ")
    q = int(input())
    return q


train_employees = []

a = display_manu()
if a == 1:
    pass
elif a == 2:
    pass
elif a == 3:
    pass
elif a == 4:
    pass
else:
    pass

class User:
    def __init__(self,name,email,username,password,wallet):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.wallet = 0
                                               
    def add_to_wallet(self, user):
        amount = int(input("Enter amount to add to your wallet: "))
        self.wallet += amount
        print(f"Added {amount} to your wallet. Current balance: {self.wallet}")



    def register(self):

        name = input("Enter your name:")
        email = input("Enter your email:")
        username = input("enter your username:")
        
        print("(press 0 if you want to exit)")
        user_1 = input()
        if exit_0(user_1):
            main_menu() 
            
        for user in self.users:
            if any(user.username == username or user.email == email):
                print("Username or email already exist.Pleas try again.")

            else:
                password = input("Enter your password:")
                self.user.append(User(name, username, password, email))
                print("Registration successful")
                return
                

    def login(self):
                    
        username = input("Enter your username:")
        password = input("Enter your password:")
        
        print("(press 0 if you want to exit)")
        user_2 = input()
        if exit_0(user_2):
            main_menu() 
            
        for user in self.users:
            if user.username == username and user.password == password:
                print("Welcome to the train ticket purchase system.")
                self .user_menu(user)
                return
            else:
                print("Incorrect username or password. please try again.")
                self.login()

        
                                                        
   def purchase_pannel(self, user):

        print("Purchase Panel :") 
        print("1. Buy ticket")
        print("2. Edit user informatino")
        print("3. Logout")
        print("4. wallet")

        choice = input("Enter your choice:")
        if choice == 1 :
            self.buy_ticket(user)
        elif choice == 2 :
            self.edit_user_info(user)
        elif choice == 3 : 
            print("Logout successful")
            exit
        elif choice == 4 :
            self.add_to_wallet() 

        else:
            print("Invalid choice. Please try again")


                                                        
def edit_user_info(self, user):
    
     print("Here's your registration information :")
    print(f"Name : {globals()[user].name}, Email : {globals()[user].email}, Username : {user}, Password : {globals()[user].password}")
    while True :
            print("Edit User Information")
            print("1. Edit Name")
            print("2. Edit Email")
            print("3. Edit Password")
            print("4. Back to Buy ticket")

            choice = input("Enter your choice:")

            if choice == 1 :
                new_name = input("Enter new name:")
                globals()[user].name = new_name
                print("Name updated successfully.")
            elif choice == 2 :
                new_email = input("Enter your new email:")
                globals()[user].email = new_email
                print("Email updated successfully.")
            elif choice == 3:
                new_password = input("Enter your new password:")
                globals()[user].password = new_password
                print("Password updated successfully.")
            elif choice == 4:
                self.buy_ticket(user)
                return
            else:
                print("Invalid choice. Please try again.")
                                                                        
                                                                  
def train_list():   

    print("Available Trains:")

for i in train_list:      
                    print("train name=" ,i, "quality="globals()[i].quality "capacity="globals()[i].capacity "price="globals()[i].price)
                    print("--------------")     

                                                                         
def buy_ticket():
        print("Available Trains:")
        for i in train_list:
            print(
                f"train name = {i} quality = {globals()[i].quality} capacity = {globals()[i].capacity} price = {globals()[i].price}"
            )
        print("--------------")

        train_name = input("Enter the name of the train you want: ")

        if train_name not in train_list:
            print("Train not found. Please check the train name and try again.")
            return self.buy_ticket(user)

        num_tickets = int(input("Enter the number of tickets you want: "))

        if num_tickets > globals()[train_name].capacity and globals()[train_name].capacity != 0:
            print(
                "Insufficient capacity. Please choose a different train or reduce the number of tickets"
            )
            return self.buy_ticket(user)
        elif globals()[train_name].capacity == 0:
            print(
                f"Capacity for {train_name} is full. Choose another train or reduce the number of tickets."
            )
            return self.buy_ticket(user)
        elif globals()[user].wallet < globals()[train_name].price * num_tickets:
            print("Insufficient funds. Please add funds to your wallet.")
            return self.buy_ticket(user)
        else:
            globals()[train_name].capacity -= num_tickets
            globals()[user].wallet -= globals()[train_name].price * num_tickets
            print("Tickets purchased successfully!")

def main_menu():
            print("Main Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter you choice:")

            if choice == 1 :
                User.register()
            elif choice == 2 :
                User.login()   
            elif choice == 3 :
                print("Goodbae")
                exit
            else:
                print("Invalid choice. Please try again.")


