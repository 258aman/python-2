uname = 'Admin'
pwd = 'admin123'

attempt = 0
while True:
    username = input('enter username:')
    password = input('enter password:')
        if attempt == 3:
        print('too many attempt')
    if username != uname:
        print('💔 Invalid username')
    if password != pwd:
        print('💔 Invalid password')
    if username == uname and password == pwd:
        print('✔ Login successful')
        break

