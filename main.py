"""
Lab 1
Thomas Carlucci
CS 166 / Fall 2022
"""
import csv
import user

from user import User

def main():
    logins = []
    valid_login = False

    with open('userdata.csv', 'r') as f:
        database = csv.reader(f)
        for row in database:
            new_user = User(row[0], row[1], row[2])
            logins.append(new_user)

    print("Welcome to Unsecure Company Intranet!")
    while not valid_login:
        username = input("Please enter your username:")
        password = input("Please enter your password:")

        for login in logins:
            if username == login.get_username() and password == login.get_password():
                temp_user = login
                valid_login = True
        if not valid_login:
            print("Username or Password incorrect, please try again.")

    active_user = temp_user
    menu_loop = True

    while menu_loop:
        print_menu()
        option = int(input("Choose an option listed above:"))
        if option == 1:
            if active_user.get_access() == "ADMIN":
                print("!!! You have now accessed the time reporting application")
            else:
                print("!!! You are not authorized to access this area.")
        elif option == 2:
            if active_user.get_access() == "ADMIN" or active_user.get_access() == "ADVANCED":
                print("!!! You have now accessed the accounting application")
            else:
                print("!!! You are not authorized to access this area.")
        elif option == 3:
            print("!!! You have now accessed the developer environment.")
        else:
            print("Invalid option. Try again.")

    print("Welcome, " + temp_user.get_username() + "!")


def print_menu():
    print("Press a number to begin:")
    print("-------------------------")
    print("1: Time Reporting")         # ADMIN
    print("2: Accounting")             # ADVANCED
    print("3: Developer Environment")  # BASIC
    print("-------------------------")


if __name__ == "__main__":
    main()