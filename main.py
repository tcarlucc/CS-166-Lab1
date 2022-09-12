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


    while not valid_login:
        print("Welcome to Unsecure Company Intranet!")
        username = input("Please enter your username to begin:")
        password = input("Please enter your password:")
        print(new_user)


    pass

if __name__ == "__main__":
    main()