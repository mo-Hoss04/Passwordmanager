pwd= input('What is the master password? ')



def add():
    name = input('User Name: ')
    pwd = input('Password: ')  

    with open('passwords.txt', 'a') as f:   # 'with' will close the file after you open it. 'a' is to append, 'w' is to overwrite the file and 'r' allows you to only read the file.
        f.write(name + "|" + pwd + "\n") # this line of code will record the username and the password in the txt file 

def view():
  with open('passwords.txt', 'r') as f:
     for line in f.readlines():
        data = line.rstrip() # 'rstrip' removes the empty line in the console when viewing
        user, password = data.split('|') # the 'split' fuction will return passwords and usernames as lists so it won't be seen like in txt file
        print('User: ', user ,'| Password: ', password) 
    

while True:
    mode = input('Would you like to add a password or view existing ones? (view, add), press q to quit: ')
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
     add()
    else:
     print('Invalid request.')
     continue