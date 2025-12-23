#Importing Modules
import re    
import os

## File name to store user data
FILE = "users.txt"

def load_users():
    """Reads username:password from file into a dictionary."""
    users = {}
    # Check if file exists
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                # Check if line contains username and password separator
                if ":" in line:
                    
                    # Remove extra spaces and split username & password
                    user, pwd = line.strip().split(":")
                    users[user] = pwd
    return users

def save_user(username, password):
    """Appends new user to file."""
    with open(FILE, "a") as f:
        # Store username and password in file
        f.write(f"{username}:{password}\n")

def validate_username(username):
    """Validates email format using rules."""
    pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, username))

def validate_password(password):
    """Checks all password rules."""
    
    # Password length check
    if len(password) < 6 or len(password) > 16:
        return False
    # At least one uppercase letter
    if not re.search("[A-Z]", password):
        return False
    # At least one lowercase letter    
    if not re.search("[a-z]", password):
        return False
    # At least one number
    if not re.search("[0-9]", password):
        return False
    # At least one special character
    if not re.search("[@#$%^&+=!]", password):
        return False
    return True

def register():
    """
    Handles user registration
    """
    print("\n REGISTRATION ")
    users = load_users()
    
    #Get username from user
    username = input("Enter username (email): ")
    # Validate email format
    if not validate_username(username):
        print("Invalid email format!")
        return
    # Check if user already exists
    if username in users:
        print("Username already exists!")
        return
    # Get password from user
    password = input("Enter password: ")
    # Validate password rules
    if not validate_password(password):
        print(" Weak password! Follow the rules.")
        return
    # Save new user
    save_user(username, password)
    print("Registration Successful!")

def login():
     """
    Handles user login
    """
    print("\n LOGIN ")
    users = load_users()
    # Take login credentials
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check username and password
    if username in users and users[username] == password:
        print("Login Successful!")
        return
    #If Login fails
    print("Incorrect username or password!")
    #Ask user next action
    choice = input("Do you want to (1) Register or (2) Forgot Password? : ")
    if choice == "1":
        register()
    elif choice == "2":
        forgot_password()
    else:
        print("Invalid option.")

def forgot_password():
    """
    Displays password if username exists
    """
    print("\n FORGOT PASSWORD ")
    users = load_users()
    # Take username input
    username = input("Enter your username: ")
    # Check if username exists
    if username not in users:
        print("Username not found! Please register.")
        return
     # Display password
    print(f"Your password is: {users[username]}")
# Main menu loop
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

