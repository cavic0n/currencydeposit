import sys

while True:
    try:
        print('                                    WELCOME TO CEE CURRENCY DEPOSIT SYSTEM')
        account = int(input('1. Login\n2. Register\n3. Exit\nREPLY: '))
        if account == 1:
            print()
            while True:
                try:
                    username = str(input('USERNAME: '))
                    userdata = open('username.txt', 'r')
                    userdataread = userdata.read()
                    userdata.close()
                    user = open('username.txt', 'w')
                    user.write(username)
                    user.close()
                    while True:
                        try:
                            password = str(input('PASSWORD: '))
                            confirmpassword = str(input('Confirm password: '))
                            if password == confirmpassword:
                                print()
                                passdata = open('password.txt', 'r')
                                passdataread = passdata.read()
                                passdata.close()
                                protection = open('password.txt', 'w')
                                protection.write(password)
                                protection.close()
                                break
                            else:
                                print('Passwords don\'t match. Try again!\n')
                            break
                        except NameError:
                            print()
                        except ValueError:
                            print('Numbers only please')
                    if username == userdataread and password == passdataread:
                        print('Login successful.')
                        break
                    else:
                        print('Username and password dont match with what is in database. Please register')
                        fullname = str(input('Your full name: '))
                        username = str(input('Username: '))
                        userdata = open('username.txt', 'r')
                        userdataread = userdata.read()
                        userdata.close()
                        user = open('username.txt', 'w')
                        user.write(username)
                        user.close()
                        while True:
                            try:
                                age = int(input('How old are you?  '))
                                if age > 18:
                                    print()
                                elif age < 18:
                                    m = 18 - age
                                    print('You are too young to use this platform. Come back in the next', m, 'years\n')
                                    sys.exit()
                                password = str(input('password: '))
                                confirmpassword = str(input('Confirm password: '))
                                if password == confirmpassword:
                                    print(username, ',your account has been created successfully\n')
                                    passdata = open('password.txt', 'r')
                                    passdataread = passdata.read()
                                    passdata.close()
                                    protection = open('password.txt', 'w')
                                    protection.write(password)
                                    protection.close()
                                    break
                                else:
                                    print('Passwords don\'t match. Try again!\n')
                                break
                            except NameError:
                                print()
                            except ValueError:
                                print('Numbers only please\n')
                        break
                except ValueError:
                    print('Numbers only please\n')
                except NameError:
                    print('Retry')
            break
        elif account == 2:
            print()
            while True:
                try:
                    fullname = str(input('Your full name: '))
                    if fullname == "":
                        print('PLease input your full name')
                        continue
                    break
                except ValueError:
                    print('Please enter the right input')
                except NameError:
                    print('Please enter the right input')
            while True:
                try:
                    username = str(input('Username: '))
                    if username == "":
                        print('Please input your username')
                        continue
                    userdata = open('username.txt', 'r')
                    userdataread = userdata.read()
                    userdata.close()
                    user = open('username.txt', 'w')
                    user.write(username)
                    user.close()
                    break
                except ValueError:
                    print('Please enter the right input')
                except NameError:
                    print('Please enter the right input')
            while True:
                try:
                    age = int(input('How old are you?  '))
                    if age > 18:
                        print()
                    elif age < 18:
                        m = 18 - age
                        print('You are too young to use this platform. Come back in the next', m, 'years')
                        sys.exit()
                    password = str(input('password: '))
                    confirmpassword = str(input('Confirm password: '))
                    if password == confirmpassword:
                        print(username, ',your account has been created successfully.\n')
                        passdata = open('password.txt', 'r')
                        passdataread = passdata.read()
                        passdata.close()
                        protection = open('password.txt', 'w')
                        protection.write(password)
                        protection.close()
                    else:
                        print('Passwords don\'t match. Try again!\n')
                    break
                except ValueError:
                    print('Numbers only please')
            break
        elif account == 3:
            print('Thank you for using our software.')
            sys.exit()
    except ValueError:
        print('Numbers only please')

while True:
    try:
        deposit = int(input('1. Dollar account\n2. Pound account\n3. Euro account\n4. Exit\nREPLY: '))
        if deposit == 1:
            print()
            while True:
                try:
                    dollar = int(input('1. Deposit to dollar account\n2. Check Account balance\n3. Back\nREPLY: '))
                    if dollar == 1:
                        print()
                        while True:
                            try:
                                amount = int(input('How much Naira do you want to deposit?(1 dollar = 360 Naira)\n'))
                                total = amount/360
                                while True:
                                    try:
                                        print('You are about depositing ', total, ' dollars.\n')
                                        question = int(input('Are you sure you want to continue with the transaction?\n1. Yes\n2. No\nREPLY: '))
                                        if question == 1:
                                            print()
                                            while True:
                                                passkey = str(input('Confirm password before deposit\n'))
                                                if passkey == password:
                                                    print('Deposit successful\n')
                                                    write = open('dollar.txt', 'w')
                                                    write.write(str(total))
                                                    write.close()
                                                    break
                                                else:
                                                    print('Wrong password. Try again\n')
                                            break
                                        elif question == 2:
                                            print('Transaction terminated!\n')
                                            break
                                        else:
                                            print('Please follow the correct instruction\n')
                                    except ValueError:
                                        print('Numbers only please\n')
                                    except NameError:
                                        print('Follow the instructions please\n')
                                break
                            except ValueError:
                                print('Numbers only please\n')
                            except NameError:
                                print('Follow the instructions please\n')
                        break
                    elif dollar == 2:
                        print()
                        read = open('dollar.txt', 'r')
                        balance = read.read()
                        print('Your balance ==', balance, '\n')
                        read.close()
                    elif dollar == 3:
                        print()
                        break
                    else:
                        print('Please follow the correct instruction\n')
                except ValueError:
                    print('Numbers only please\n')
                except NameError:
                    print('Follow the instructions please\n')

        elif deposit == 2:
            print()
            while True:
                try:
                    pound = int(input('1. Deposit to pound account\n2. Check Account balance\n3. Back\nREPLY: '))
                    if pound == 1:
                        print()
                        while True:
                            try:
                                amount = int(input('How much Naira do you want to deposit?(1 pound = 420 Naira)\n'))
                                total = amount/420
                                while True:
                                    try:
                                        print('You are about depositing ', total, ' pounds.\n')
                                        question = int(input('Are you sure you want to continue with the transaction?\n1. Yes\n2. No\nREPLY: '))
                                        if question == 1:
                                            print()
                                            while True:
                                                passkey = str(input('Confirm password before deposit: '))
                                                if passkey == password:
                                                    print('Deposit successful\n')
                                                    write = open('pound.txt', 'w')
                                                    write.write(str(total))
                                                    write.close()
                                                    break
                                                else:
                                                    print('Wrong password. Try again!\n')
                                            break
                                        elif question == 2:
                                            print('Transaction terminated!\n')
                                            break
                                        else:
                                            print('Please follow the correct instruction\n')
                                    except ValueError:
                                        print('Numbers only please\n')
                                    except NameError:
                                        print('Follow the instructions please\n')
                                break
                            except ValueError:
                                print('Numbers only please\n')
                            except NameError:
                                print('Follow the instructions please\n')
                        break
                    elif pound == 2:
                        print()
                        read = open('pound.txt', 'r')
                        balance = read.read()
                        print('Your balance ==', balance, '\n')
                        read.close()
                    elif pound == 3:
                        print()
                        break
                    else:
                        print('Please follow the correct instruction\n')
                except ValueError:
                    print('Numbers only please\n')
                except NameError:
                    print('Follow the instructions please\n')

        elif deposit == 3:
            print()
            while True:
                try:
                    euro = int(input('1. Deposit to euro account\n2. Check Account balance\n3. Back\nREPLY: '))
                    if euro == 1:
                        print()
                        while True:
                            try:
                                amount = int(input('How much Naira do you want to deposit?(1 euro = 480 Naira)\nREPLY: '))
                                total = amount/480
                                while True:
                                    try:
                                        print('You are about depositing ', total, ' euros.\n')
                                        question = int(input('Are you sure you want to continue with the transaction?\n1. Yes\n2. No\nREPLY: '))
                                        if question == 1:
                                            print()
                                            while True:
                                                passkey = str(input('Confirm password before deposit: '))
                                                if passkey == password:
                                                    print('Deposit successful\n')
                                                    write = open('euro.txt', 'w')
                                                    write.write(str(total))
                                                    write.close()
                                                    break
                                                else:
                                                    print('Wrong password. Try again!\n')
                                            break
                                        elif question == 2:
                                            print('Transaction terminated!\n')
                                            break
                                        else:
                                            print('Please follow the correct instructions\n')
                                    except ValueError:
                                        print('Numbers only please\n')
                                    except NameError:
                                        print('Follow the instructions please\n')
                                break
                            except ValueError:
                                print('Numbers only please\n')
                            except NameError:
                                print('Follow the instructions please\n')
                        break
                    elif euro == 2:
                        print()
                        read = open('euro.txt', 'r')
                        balance = read.read()
                        print('Your balance ==', balance, '\n')
                        read.close()
                    elif euro == 3:
                        print()
                        break
                    else:
                        print('Please follow the correct instruction\n')
                except ValueError:
                    print('Numbers only please\n')
                except NameError:
                    print('Follow the instructions please\n')      
        elif deposit == 4:
            print('Thank you for using our platform')
            break      
        else:
            print('Please follow the correct instruction\n')    
    except ValueError:
        print('Numbers only please\n')
    except NameError:
        print('Follow instructions please\n')