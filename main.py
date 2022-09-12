"""
Lab 1
Thomas Carlucci
CS 166 / Fall 2022
"""
import csv
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
        username = input("Please enter your username to begin:")
        password = input("Please enter your password:")

        for login in logins:
            if username == login.get_username() and password == login.get_password():
                temp_user = login
                valid_login = True
            else:
                print("Username or Password incorrect, please try again.")

    active_user = temp_user

    print("Welcome, " + temp_user.get_username() + "!")




if __name__ == "__main__":
    main()