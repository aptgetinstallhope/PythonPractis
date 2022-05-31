from data import users
username = input('username ==> ')
passwrod = input('password ==> ')

status = 500

for keyid in users:
    userobject = users[keyid]
    if userobject['username'] == username : 
        if userobject['password'] == passwrod:
            status = 200
            print('login successfully')
            print('your first name is :' + userobject['firstname'])
            print('your last name is :' + userobject['lastname'])
            break

if status == 500:
    print('your username or password is incorrect')

