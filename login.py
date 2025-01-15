from api import verify_karyawan_login

def login():
    print("=== Login ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    karyawan = verify_karyawan_login(username, password)
    if karyawan:
        print(f"\nLogin berhasil sebagai {karyawan['Posisi_Jabatan']}!")
        return karyawan["Username"]
    
    print("\nUsername atau password salah!")
    return None

def logout():
    print("Anda telah keluar dari sistem")

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
