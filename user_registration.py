# Handles user registration: collects user info, hashes password, stores data in users.json.

import json
import os
from getpass import getpass
from utils import hash_password
from cert_generator import generate_self_signed_cert

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def register_user():
    users = load_users()

    full_name = input("Enter Full Name: ").strip()
    email = input("Enter Email Address: ").strip().lower()

    if email in users:
        print("User already exists.")
        return

    while True:
        password = getpass("Enter Password: ")
        confirm = getpass("Re-enter Password: ")
        if password == confirm:
            break
        print("Passwords do not match. Try again.")

    hashed = hash_password(password)
    users[email] = {
        "full_name": full_name,
        "password_hash": hashed
    }

    save_users(users)
    generate_self_signed_cert(email)
    print("User Registered. Exiting SecureDrop.")
