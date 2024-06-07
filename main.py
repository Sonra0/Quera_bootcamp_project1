def display_manu():  # a function to show main menu of program
    print("1. Main Admin")
    print("2. Train Employee")
    print("3. User")
    print("4. Exit")
    print("Enter your number:", end=" ")
    q = int(input())
    print("------------------")
    return q

def exit_0(a):  # a function to exit the program if input == '0'
    if a == '0':
        return True

class User:
    def __init__(self, name, email, username, password, wallet):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.wallet = wallet

        # کیف پول

    def add_to_wallet(self):
        amount = int(input("Enter amount to add to your wallet: "))
        self.wallet += amount
        print(f"Added {amount} to your wallet. Current balance: {self.wallet}")

        # ثبت نام کاربر

    def register(self):

        name = input("Enter your name(press 0 to exit):")
        if exit_0(name):
            user_pannel()
        email = input("Enter your email(press 0 to exit):")
        if exit_0(email):
            user_pannel()
        username = input("enter your username(press 0 to exit):")
        if exit_0(username):
            user_pannel()

        if username in blah or any(globals()[user].email == email for user in users_list):
            print("object name or email already exist.Pleas try again.")
            return self.register()

        password = input("Enter your password(press 0 to exit):")
        if exit_0(password):
            user_pannel()
        globals()[username] = User(name, email, username, password, wallet=0)
        users_list.append(username)
        blah.append(username)
        print("Registration successful")
        user_pannel()

        # ورود کاربر

    def login(self):
        while True:
            username = input("Enter your username(press 0 to exit):")
            if exit_0(username):
                user_pannel()
            password = input("Enter your password(press 0 to exit):")
            if exit_0(password):
                user_pannel()
            if username in users_list and globals()[username].password == password:
                print("Welcome to the train ticket purchase system.")
                self.purchase_pannel(username)
                return

            else:
                print("Incorrect username or password. please try again.")

                # منو کاربر

    def purchase_pannel(self, user):

        while True:
            print("Purchase Panel:")
            print("1. Buy ticket")
            print("2. Edit user information")
            print("3. Logout")
            print("4. Wallet")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.buy_ticket(user)
            elif choice == 2:
                self.edit_user_info(user)
            elif choice == 3:
                print("Logout successful")
                return
            elif choice == 4:
                globals()[user].add_to_wallet()
            else:
                print("Invalid choice. Please try again.")

            # ویرایش اطلاعات کاربری

    def buy_ticket(self, user):

        print("Available Trains:")
        for i in train_list:
            print(
                f"train name= {i} quality= {globals()[i].quality} capacity= {globals()[i].capacity} price= {globals()[i].price}")
        print("--------------")

        train_name = input("Enter the name of the train you want:")

        if train_name not in train_list:
            print("Train not found. Please check the train name and try again.")
            self.buy_ticket(user)
        else:

            num_tickets = int(input("Enter the number of tickets you want:"))

            if num_tickets > globals()[train_name].capacity and globals()[train_name].capacity != 0:
                print("Insufficient capacity. Please choose a different train or reduce the number of tickets")
                return self.buy_ticket(user)

            total_cost = globals()[train_name].price * num_tickets
            if total_cost > globals()[user].wallet:
                print("Insufficient finds in your wallet.")
                return

            elif globals()[train_name].capacity == 0:
                print(
                    f"Capacity for {globals()[train_name].name} is full. choose another train or reduce the number of tickets.")
                return self.buy_ticket(user)
            else:
                globals()[train_name].capacity -= num_tickets
                globals()[user].wallet -= total_cost
                print("Tickets purchased successfully")
                print(f"Remaining wallet balance:{globals()[user].wallet}")

    def edit_user_info(self, user):

        print("Here's your registration information :")
        print(
            f"Name : {globals()[user].name}, Email : {globals()[user].email}, Username : {user}, Password : {globals()[user].password}")
        while True:
            print("Edit User Information")
            print("1. Edit Name")
            print("2. Edit Email")
            print("3. Edit Password")
            print("4. Back to the purchase pannel")

            choice = int(input("Enter your choice:"))

            if choice == 1:
                new_name = input("Enter new name(press 0 to return to Purchase Panel):")
                if new_name == "0":
                    self.purchase_pannel(user)
                globals()[user].name = new_name
                print("Name updated successfully.")
            elif choice == 2:
                new_email = input("Enter your new email(press 0 to return to Purchase Panel):")
                if new_email == "0":
                    self.purchase_pannel(user)
                globals()[user].email = new_email
                print("Email updated successfully.")
            elif choice == 3:
                new_password = input("Enter your new password(press 0 to return to Purchase Panel):")
                if new_password == "0":
                    self.purchase_pannel(user)
                globals()[user].password = new_password
                print("Password updated successfully.")
            elif choice == 4:
                self.purchase_pannel(user)
            else:
                print("Invalid choice. Please try again.")


def user_pannel():
    while True:
        print("User Panel:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        user = User("", "", "", "", 0)
        if choice == 1:
            user.register()
        elif choice == 2:
            user.login()
        elif choice == 3:
            print("Bye Bye")
            return 0
        else:
            print("Invalid choice. Please try again.")
