# Lab 1 - CS 166 OL
## by Thomas Carlucci

### Description
Python program that simulates a login and menu
to a company intranet system that requires employees to
enter a username and password in order to view a menu of applications
to use, each with their own access level.

The programs are: Time Reporting (ADMIN Clearance), Accounting (ADVANCED Clearance), and Developer Environment (BASIC Clearance).
### Testing Instructions
Logins are as follows:

| Username     | Password | Access   |
|--------------|----------|----------|
| root         | alpine   | ADMIN    |
| cybersecguru | password | ADVANCED |
| temp         | temp     | BASIC    |

There are three "programs" each with their own
level of clearance. To use the program, run it using Python 3
and enter any of the logins listed above. You will then be prompted with
a menu of applications to choose from. Your success in gaining "entry" to these
applications depends on which login was chosen. Either way you will be returned to the menu 
prompt but the text that follows your option shows that the access functionality
works. 