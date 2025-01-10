 import getpass


users_db = {
    "admin": "admin123",
    "kasir": "kasir123",
    "manager": "manager123",
}

def login():
    print("Login")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    
    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password!")
        return None

def logout(username):
    print(f"{username} logged out successfully.")

def main():
    logged_in_user = None

    while True:
        if logged_in_user:
            print("\nYou are logged in as:", logged_in_user)
            action = input("Do you want to logout? (yes/no): ").lower()
            if action == 'yes':
                logout(logged_in_user)
                logged_in_user = None
        else:
            print("\nNot logged in.")
            action = input("Do you want to login? (yes/no): ").lower()
            if action == 'yes':
                logged_in_user = login()
        
        if logged_in_user is None:
            action = input("Do you want to exit the program? (yes/no): ").lower()
            if action == 'yes':
                print("Exiting program.")
                break

if __name__ == "__main__":
    main()
