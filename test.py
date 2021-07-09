import shrtcode
import os
import sys

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def start():
    clear()
    test_input = input(
        'Choose thing to test:\n\n'
        '1 - Standart shorting\n'
        '2 - Get info about short link from code\n'
        '3 - Short with custom code\n'
        '4 - Short with emoji code\n'
        '5 - Short with password\n'
        '6 - Exit\n\n'
        '[1-6]\n\n>>> '
    )
    if test_input == "1":
        short()
    elif test_input == "2":
        info()
    elif test_input == "3":
        custom()
    elif test_input == "4":
        emoji()
    elif test_input == "5":
        password()
    elif test_input == "6":
        leave()

def short():
    clear()
    url = input(
        'Please, input URL.\n\n>>> '
    )
    print(
        'Alright! Please, wait some time!'
    )
    try:
        short = shrtcode.short(url)
        clear()
        input(
            'Here it:\n\n'
            f'First short link: {short["full_short_link"]}\n'
            f'Second short link: {short["full_short_link2"]}\n'
            f'Third short link: {short["full_short_link3"]}\n'
            f'Share short link: {short["full_share_link"]}\n\n'
            'Press ENTER to return to the Main Menu'
        )
        start()
    except:
        clear()
        input(
            'Whoops! Error!\n'
            f'{sys.exc_info()[0]}\n'
            'Press ENTER to return to the Main Menu'
        )
        start()

def info():
    clear()
    code = input(
        'Please, input code.\n\n>>> '
    )
    print(
        'Alright! Please, wait some time!'
    )
    try:
        info = shrtcode.info(code)
        clear()
        input(
            'Here it:\n\n'
            f'Full URL: {info["url"]}\n\n'
            'Press ENTER to return to the Main Menu'
        )
        start()
    except:
        clear()
        input(
            'Whoops! Error!\n'
            f'{sys.exc_info()[0]}\n'
            'Press ENTER to return to the Main Menu'
        )
        start()

def custom():
    clear()
    url = input(
        'Please, input URL.\n\n>>> '
    )
    clear()
    code = input(
        'Please, input code.\n\n>>> '
    )
    print(
        'Alright! Please, wait some time!'
    )
    try:
        custom = shrtcode.custom(url, code)
        clear()
        input(
            'Here it:\n\n'
            f'First short link: {custom["full_short_link"]}\n'
            f'Second short link: {custom["full_short_link2"]}\n'
            f'Third short link: {custom["full_short_link3"]}\n'
            f'Share short link: {custom["full_share_link"]}\n\n'
            'Press ENTER to return to the Main Menu'
        )
        start()
    except:
        clear()
        input(
            'Whoops! Error!\n'
            f'{sys.exc_info()[0]}\n'
            'Press ENTER to return to the Main Menu'
        )
        start()

def emoji():
    clear()
    url = input(
        'Please, input URL.\n\n>>> '
    )
    print(
        'Alright! Please, wait some time!'
    )
    try:
        short = shrtcode.emoji(url)
        clear()
        input(
            'Here it:\n\n'
            f'First short link: {short["full_short_link"]}\n'
            f'Second short link: {short["full_short_link2"]}\n'
            f'Third short link: {short["full_short_link3"]}\n'
            f'Share short link: {short["full_share_link"]}\n\n'
            'Press ENTER to return to the Main Menu'
        )
        start()
    except:
        clear()
        input(
            'Whoops! Error!\n'
            f'{sys.exc_info()[0]}\n'
            'Press ENTER to return to the Main Menu'
        )
        start()

def password():
    clear()
    url = input(
        'Please, input URL.\n\n>>> '
    )
    clear()
    password = input(
        'Please, input password.\n\n>>> '
    )
    print(
        'Alright! Please, wait some time!'
    )
    try:
        password = shrtcode.password(url, password)
        clear()
        input(
            'Here it:\n\n'
            f'First short link: {password["full_short_link"]}\n'
            f'Second short link: {password["full_short_link2"]}\n'
            f'Third short link: {password["full_short_link3"]}\n'
            f'Share short link: {password["full_share_link"]}\n\n'
            'Press ENTER to return to the Main Menu'
        )
        start()
    except:
        clear()
        input(
            'Whoops! Error!\n'
            f'{sys.exc_info()[0]}\n'
            'Press ENTER to return to the Main Menu'
        )
        start()

def leave():
    clear()
    toLeave = input(
        'Are you leaving already?\n'
        'If you don\'t want to go out, type "N"\n\n>>> '
        )
    if toLeave == "N":
        start()


start()
#print(shrtcode.password("https://example.com/", "kadilak"))