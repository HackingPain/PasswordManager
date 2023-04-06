import os.path

# checks to see if the info file exists in the directory where the
# python file is located. If not it creates one.

def checkExistence():
    if  os.path.exists('info.txt'):
        pass
    else:
        file = open('info.txt', 'w')
        file.close()

# Write to file

def appendNew():

    # adds new password in the text file.

    file = open('info.txt', 'a')

    print()
    print()

    # takes input from the user about their username, password, and the website

    userName = input('Enter your user name: ')
    password = input('Enter your password: ')
    website = input('Enter the website address (URL): ')

# extra spacing

    print()
    print()

# 3 string variables to store the username, password, and website

    usrnm = 'UserName: ' + userName + '\n'
    pwd = 'Password' + password + '\n'
    web = 'Website' + website + '\n'

# writes to the file 
    file.write('----------\n')
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write('----------\n')
    file.write('\n')
    file.close

# Output the password
# opens the file and reads it
# creates a new variable to store the contents of the file

def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)