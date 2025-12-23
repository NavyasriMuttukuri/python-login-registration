import re    
import os

FILE = "users.txt"

def load_users():
    """Reads username:password from file into a dictionary."""
    users = {}
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                if ":" in line:


                    
                    user, pwd = line.strip().split(":")
                    users[user] = pwd
    return users

def save_user(username, password):
    """Appends new user to file."""
    with open(FILE, "a") as f:
        f.write(f"{username}:{password}\n")

def validate_username(username):
    """Validates email format using rules."""
    pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, username))

def validate_password(password):
    """Checks all password rules."""
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&+=!]", password):
        return False
    return True

def register():
    print("\n REGISTRATION ")
    users = load_users()
    username = input("Enter username (email): ")
    if not validate_username(username):
        print("Invalid email format!")
        return
    if username in users:
        print("Username already exists!")
        return
    password = input("Enter password: ")
    if not validate_password(password):
        print(" Weak password! Follow the rules.")
        return
    save_user(username, password)
    print("Registration Successful!")

def login():
    print("\n LOGIN ")
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login Successful!")
        return
    print("Incorrect username or password!")
    choice = input("Do you want to (1) Register or (2) Forgot Password? : ")
    if choice == "1":
        register()
    elif choice == "2":
        forgot_password()
    else:
        print("Invalid option.")

def forgot_password():
    print("\n FORGOT PASSWORD ")
    users = load_users()
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found! Please register.")
        return
    print(f"Your password is: {users[username]}")
while True:
    print("\n MENU")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid input!")
