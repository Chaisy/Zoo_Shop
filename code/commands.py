import os
from getpass import getpass
from colorama import Fore
from database import Database
from models import User
from tabulate import tabulate


def emphasis(content):
    return Fore.BLUE + content + Fore.RESET


def error(content):
    return Fore.RED + content + Fore.RESET


def hello():
    Database.connect()

    while True:
        os.system('clear')
        print('Welcome to ' + emphasis('Zoo Shop\n'))

        print('What do you want?\n' +
              emphasis('1') + ' Login\n' +
              emphasis('2') + ' Register\n' +
              emphasis('3') + ' Exit\n')

        while True:
            choice = input('Enter ' + emphasis('here: '))

            if choice == '1' or choice == '2' or choice == '3':
                break
            else:
                print(error('\nInvalid data. Try again!\n'))

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            Database.disconnect()
            break


def login():
    os.system('clear')

    while True:
        username = input('Enter ' + emphasis('login') + ': ')
        password = getpass('Enter ' + emphasis('password') + ': ')

        user = Database.get_user(username, password)

        if user is None:
            print(error('\nInvalid data. Try again!'))
            e = input('Do you want exit? (1) ')
            if e == '1':
                break
            print('')
        else:

            if user.role_id == 1:
                client(user)
            elif user.role_id == 2:
                moderator(user)
            elif user.role_id == 3:
                admin(user)

            break


def register():
    os.system('clear')

    while True:
        username = input('Enter ' + emphasis('login ') + ': ')
        name = input('Enter ' + emphasis('Name') + ': ')
        password = getpass('Enter ' + emphasis('password') + ': ')
        user = Database.add_client(username, name, password)

        if user is None:
            print(error('\nInvalid data. Try again!'))
            e = input('Do you want exit? (1) ')
            if e == '1':
                break
            print('')
        else:
            print('\nYou were successfully ' + emphasis('registered') + '!\n')
            input('\n')
            break


def client(user: User):
    while True:
        os.system('clear')
        print('Hello, ' + emphasis('client') + '!\n')

        # print(user.login)
        if Database.is_banned(user.login):
            print('You were ' + emphasis('banned') + '!\n')
            input('\n')
            break

        print('What do you want?\n' +
              emphasis('1') + ' View all goods\n' +
              emphasis('2') + ' View all firms\n' +
              emphasis('3') + ' View some goods by category\n' +
              emphasis('4') + ' View some goods by animal\n' +
              emphasis('5') + ' View good\n' +
              emphasis('6') + ' Create order\n' +
              emphasis('7') + ' Edit your profile\n' +
              emphasis('8') + ' Exit\n')

        while True:
            choice = input('Enter ' + emphasis('here: '))

            if choice == '1' or choice == '2' or choice == '3' or \
                    choice == '4' or choice == '5' or choice == '6' or \
                    choice == '7' or choice == '8':
                break
            else:
                print(error('\nInvalid data. Try again!'))
                e = input('Do you want exit? (1) ')
                if e == '1':
                    break
                print('')

        if choice == '1':
            os.system('clear')
            print(emphasis('View all goods...\n'))

            chats = Database.get_goods_with_category()
            headers = ['Id', 'Good', 'Category']
            print(tabulate(chats, headers=list(map(emphasis, headers))))
            input('\n')

        elif choice == '2':
            os.system('clear')
            print(emphasis('View all firms...\n'))

            firms = Database.get_firms()
            headers = ['Id', 'Firm']
            print(tabulate(firms, headers=list(map(emphasis, headers))))
            input('\n')

        elif choice == '3':
            os.system('clear')
            print(emphasis('View some goods by category...\n'))
            category = input('Enter ' + emphasis('category(Home, Food,...)') + ': ')
            goods = Database.get_good_specific_category(category)
            headers = ['Id', 'Good', 'Category']
            print(tabulate(goods, headers=list(map(emphasis, headers))))
            input('\n')

        elif choice == '4':
            os.system('clear')
            print(emphasis('View some goods by animal...\n'))
            animal = input('Enter ' + emphasis('animal(dogs, cats,...)') + ': ')
            goods = Database.get_good_by_animal(animal)
            headers = ['Id', 'Good', 'Animal']
            print(tabulate(goods, headers=list(map(emphasis, headers))))
            input('\n')

        elif choice == '6':
            os.system('clear')
            print(emphasis('Create order...\n'))
            # animal = input('Enter ' + emphasis('animal(dogs, cats,...)') + ': ')
            goods = Database.add_order(user)
            print('\nYou were successfully ' + emphasis('create order') + '!')
            input('\n')

        elif choice == '5':
            os.system('clear')
            print(emphasis('View good...\n'))

            added = False

            while True:
                if added:
                    input('')
                    break

                good_name = input('Enter ' + emphasis('good\'s title') + ': ')
                good = Database.get_good_specific_name(good_name)

                if good is None:
                    print(error('\nInvalid data. Try again!'))
                    e = input('Do you want exit? (1) ')
                    if e == '1':
                        break
                    print('')
                else:
                    while True:
                        if added:
                            input('')
                            break

                        headers = ['Id', 'Good', 'Category']
                        print(tabulate(good, headers=list(map(emphasis, headers))))

                        print('\nWhat do you want?\n' +
                              emphasis('1') + ' Add to cart\n' +
                              emphasis('2') + ' Exit\n')

                        while True:
                            choice = input('Enter ' + emphasis('here: '))

                            if choice == '1' or choice == '2':
                                break
                            else:
                                print(error('\nInvalid data. Try again!'))
                                e = input('Do you want exit? (1) ')
                                if e == '1':
                                    break
                                print('')

                        if choice == '1':
                            while True:
                                good = Database.get_good(good_name)
                                result = Database.add_to_cart(user, good)

                                if result is False:
                                    print(error('\nInvalid data. Try again!'))
                                    e = input('Do you want exit? (1) ')
                                    if e == '1':
                                        break
                                    print('')
                                else:
                                    added = True
                                    break
                        elif choice == '2':
                            break

        elif choice == '7':
            os.system('clear')
            print(emphasis('Edit your profile...\n'))

            while True:
                print('What you don\'t want to change, just ' + emphasis('skip!\n'))

                username = input('Enter ' + emphasis('login') + ': ')
                name = input('Enter ' + emphasis('name') + ': ')
                password = getpass('Enter ' + emphasis('password') + ': ')

                result = Database.edit_client(user, username, password, name)

                if result is None:
                    print(error('\nInvalid data. Try again!'))
                    e = input('Do you want exit? (1) ')
                    if e == '1':
                        break
                    print('')
                else:
                    print('\nYou were successfully ' + emphasis('edited profile') + '!')
                    input('\n')
                    break

        elif choice == '8':
            break


def moderator(user: User):
    while True:
        os.system('clear')
        print('Hello, ' + emphasis('moderator') + '!\n')

        print('What do you want?\n' +
              emphasis('1') + ' View all clients\n' +
              emphasis('2') + ' Ban/unban some client\n' +
              emphasis('3') + ' View all actions\n' +
              emphasis('4') + ' View some client\'s actions\n' +
              emphasis('5') + ' Create good\n' +
              emphasis('6') + ' Edit good\n' +
              emphasis('7') + ' Exit\n')

        while True:
            choice = input('Enter ' + emphasis('here: '))

            if choice == '1' or choice == '2' or choice == '3' or \
                    choice == '4' or choice == '5' or choice == '6' or choice == '7':
                break
            else:
                print(error('\nInvalid data. Try again!'))
                e = input('Do you want exit? (1) ')
                if e == '1':
                    break
                print('')

        if choice == '1':
            os.system('clear')
            print(emphasis('View all clients...\n'))

            clients = Database.get_clients_with_banned()
            headers = ['Id', 'Login', 'Name']

            print(tabulate(clients, headers=list(map(emphasis, headers))))
            input('\n')
            break

        elif choice == '2':
            os.system('clear')
            print(emphasis('Ban/unban some client...\n'))

            while True:
                username = input('Enter ' + emphasis('login') + ': ')
                result = Database.ban_unban_client(username)
                print('')

                if result is None:
                    print(error('Invalid data. Try again!'))
                    e = input('Do you want exit? (1) ')
                    if e == '1':
                        break
                    print('')
                else:
                    break

            if result:
                print('This client was successfully ' + emphasis('banned') + '!')
            else:
                print('This client was successfully ' + emphasis('unbanned') + '!')
            input('\n')



        elif choice == '3':
            os.system('clear')
            print(emphasis('View all actions...\n'))

            actions = Database.get_actions()
            headers = ['Name', 'DateTime', 'Login']

            print(tabulate(actions, headers=list(map(emphasis, headers))))
            input('\n')

        elif choice == '4':
            os.system('clear')
            print(emphasis('View some client\'s actions...\n'))

            while True:
                username = input('Enter ' + emphasis('login') + ': ')
                actions = Database.get_client_actions(username)
                print('')

                if actions is None:
                    print(error('Invalid data. Try again!'))
                    e = input('Do you want exit? (1) ')
                    if e == '1':
                        break
                    print('')
                else:
                    headers = ['Name', 'DateTime']
                    print(tabulate(actions, headers=list(map(emphasis, headers))))
                    input('\n')
                    break

        elif choice == '5':
            os.system('clear')
            print(emphasis('Create good...\n'))

            new_title = input('Enter ' + emphasis('title') + ': ')
            firm = input('Enter ' + emphasis('firm') + ': ')
            category = input('Enter ' + emphasis('category') + ': ')
            animal = input('Enter ' + emphasis('animal') + ': ')

            goods = Database.add_good(new_title, firm, category, animal)
            print(goods)
            headers = ['Id', 'Title', 'Firm', 'Category', 'Animal']
            print(tabulate(list(goods), headers=list(map(emphasis, headers))))
            input('\n')
            break

        elif choice == '7':
            break

        elif choice == '6':
            os.system('clear')
            while True:
                good_name = input('Enter ' + emphasis('good\'s title') + ': ')
                good = Database.get_good_specific_name(good_name)

                if good is None:
                    print(error('\nInvalid data. Try again!'))
                    e = input('Do you want exit? (1) ')
                    if e == '1':
                        break
                    print('')
                else:
                    while True:
                        print(emphasis('Edit good\n'))

                        while True:
                            print('What you don\'t want to change, just ' + emphasis('skip!\n'))

                            new_title = input('Enter ' + emphasis('new title') + ': ')
                            firm = input('Enter ' + emphasis('firm') + ': ')
                            category = input('Enter ' + emphasis('category') + ': ')
                            animal = input('Enter ' + emphasis('animal') + ': ')

                            result = Database.edit_good(good[0][1], new_title, firm, category, animal)

                            if not result:
                                print(error('\nInvalid data. Try again!'))
                                e = input('Do you want exit? (1) ')
                                if e == '1':
                                    break
                                print('')
                            else:
                                print('\nYou were successfully ' + emphasis('edited good') + '!')
                                input('\n')
                                break
                        e1 = input('Return to menu? (9) ')
                        if e1 == '9':
                            break
                    break





def admin(user: User):
    while True:
        os.system('clear')
        print('Hello, ' + emphasis('admin') + '!\n')

        print('What do you want?\n' +
              emphasis('1') + ' Edit people\n' +
              emphasis('2') + ' Edit some client\'s role to moderator\n' +
              emphasis('3') + ' Exit\n')

        while True:
            choice = input('Enter ' + emphasis('here: '))

            if choice == '1' or choice == '2' or choice == '3' or choice == '4':
                break
            else:
                print(error('\nInvalid data. Try again!'))
                e = input('Do you want exit? (1) ')
                if e == '1':
                    break
                print('')

        # os.system('clear')
        # print(emphasis('Edit your profile...\n'))
        #
        # while True:
        #     print('What you don\'t want to change, just ' + emphasis('skip!\n'))
        #
        #     username = input('Enter ' + emphasis('login') + ': ')
        #     name = input('Enter ' + emphasis('name') + ': ')
        #     password = getpass('Enter ' + emphasis('password') + ': ')
        #
        #     result = Database.edit_client(user, username, password, name)
        #
        #     if result is None:
        #         print(error('\nInvalid data. Try again!'))
        #         e = input('Do you want exit? (1) ')
        #         if e == '1':
        #             break
        #         print('')
        #     else:
        #         print('\nYou were successfully ' + emphasis('edited profile') + '!')
        #         input('\n')
        #         break




        if choice == '1':
            os.system('clear')
            print(emphasis('Edit profile...\n'))

            while True:
                username = input('Enter ' + emphasis('login') + ': ')
                print('')
                user = Database.get_user_by_login(username)
                while True:
                    print('What you don\'t want to change, just ' + emphasis('skip!\n'))

                    username = input('Enter ' + emphasis('login') + ': ')
                    name = input('Enter ' + emphasis('name') + ': ')
                    password = getpass('Enter ' + emphasis('password') + ': ')

                    result = Database.edit_client(user, username, password, name)

                    if result is None:
                        print(error('\nInvalid data. Try again!'))
                        e = input('Do you want exit? (1) ')
                        if e == '1':
                            break
                        print('')
                    else:
                        print('\nYou were successfully ' + emphasis('edited profile') + '!')
                        input('\n')
                        break
                e1 = input('Return to menu? (9) ')
                if e1 == '9':
                    break

        elif choice == '2':
            os.system('clear')
            print(emphasis('Edit some client\'s role to moderator\n'))

            while True:
                username = input('Enter ' + emphasis('login') + ': ')
                print('')

                result = Database.edit_client_role(username)

                if not result:
                    print(error('Invalid data. Try again!'))
                    e = input('Do you want exit? (1) ')
                    if e == '1':
                        break
                    print('')
                else:
                    print('This client was successfully turned into ' + emphasis('moderator') + '!')
                    input('\n')
                    break

        elif choice == '3':
            break
