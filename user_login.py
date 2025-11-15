from getpass import getpass
from utils import verify_password
from user_registration import load_users

def user_login():
    users = load_users()
    verify_loop = True
    
    while verify_loop:
        email = input("Enter Email Address: ")
        password = getpass("Enter Password: ")
        if email not in users or not verify_password(password, users[email]['password_hash']):
            print("Email and Password Combination Invalid.\n")
        else:
            print("Welcome to SecureDrop.\nType \"help\" for Commands.")
            verify_loop = False
            
    while True:
        command = input("secure_drop> ")
        if command.strip().lower() == "help":
            print("  \"add\" -> Add a new contact\n  \"list\" -> List all online contacts")
            print("  \"send\" -> Transfer file to a contact\n  \"exit\" -> Exit SecureDrop")
        elif command.strip().lower() == "add":
            print("Add contact functionality not yet implemented.")
        elif command.strip().lower() == "list":
            print("List contacts functionality not yet implemented.")
        elif command.strip().lower() == "send":
            print("Send file functionality not yet implemented.")
        elif command.strip().lower() == "exit":
            exit(0)