# Entry point for SecureDrop. Prompts registration if no users exist.

import os
from user_registration import register_user

def main():
    if not os.path.exists("users.json") or os.stat("users.json").st_size == 0:
        print("No users are registered with this client.")
        choice = input("Do you want to register a new user (y/n)? ").strip().lower()
        if choice == 'y':
            register_user()
        return

    print("User already registered. Proceed to login module (M2).")

if __name__ == "__main__":
    main()
