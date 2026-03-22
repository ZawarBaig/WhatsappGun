#!/usr/bin/env python3
import time
import webbrowser
import pyautogui

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

mr_baig_lines = [
    r"  __  __             ____        _       ",
    r" |  \/  |           |  _ \      (_)      ",
    r" | \  / |_ __       | |_) | __ _ _  __ _ ",
    r" | |\/| | '__|      |  _ < / _` | |/ _` |",
    r" | |  | | |         | |_) | (_| | | (_| |",
    r" |_|  |_|_|         |____/ \__,_|_|\__, |",
    r"                                    __/ |",
    r"                                   |___/ "
]

skull_lines = [
    r"         _.--''''''''--._         ",
    r"       .'                '.       ",
    r"      /                    \      ",
    r"     |                      |     ",
    r"     |   ___          ___   |     ",
    r"     |  /   \        /   \  |     ",
    f"     | |  {GREEN}O{RED}  |      |  {GREEN}O{RED}  | |     ", 
    r"      \ \___/        \___/ /      ",
    r"       \                  /       ",
    r"        \      .---.     /        ",
    r"         \     \___/    /         ",
    r"          \            /          ",
    r"           |==========|           ",
    r"           | || || || |           ",
    r"            `--------`            "
]


print(f"\n{GREEN}", end="")
for line in mr_baig_lines:
    print(line)


print(f"\n{RED}", end="")
for i, line in enumerate(skull_lines):
    if i == 1:
        print(f"{line}   {RESET}WhatsApp Bomber By Zawar Baig.{RED}")
    else:
        print(line)

print(f"\n{GREEN}--- WhatsApp Bombing Tool ---{RESET}")

phone_number = input(f"{GREEN}Enter target phone number (+9200)>> {RESET}")
message = input(f"{GREEN}Enter the message text>>{RESET}")

while True:
    try:
        count = int(input(f"{GREEN}How many times do you want to send this message?>> {RESET}"))
        if count > 0:
            break
        else:
            print(f"{RED}Please enter a number greater than 0.{RESET}")
    except ValueError:
        print(f"{RED}Invalid input. Please enter a whole number.{RESET}")

while True:
    try:
        delay = float(input(f"{GREEN}Enter time delay between messages >> {RESET}"))
        if delay >= 0:
            break
        else:
            print(f"{RED}Please enter a positive number or 0.{RESET}")
    except ValueError:
        print(f"{RED}Invalid input. Please enter a number.{RESET}")

print(f"\n{YELLOW}[*] Opening WhatsApp Web in your default browser...{RESET}")
print(f"{YELLOW}[*] PLEASE DO NOT TOUCH YOUR MOUSE OR KEYBOARD FOR THE NEXT 15 SECONDS!{RESET}")

url = f"https://web.whatsapp.com/send?phone={phone_number}"
webbrowser.open(url)

time.sleep(15) 

print(f"{GREEN}[*] Starting message delivery...{RESET}")

try:
    for i in range(count):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        print(f"{GREEN}[{i + 1}/{count}] Your Message sent!{RESET}")
        time.sleep(delay)

    print(f"\n{GREEN}[+] Task Complete! All messages delivered.{RESET}")

except KeyboardInterrupt:
    print(f"\n{RED}[!] Script stopped by user.{RESET}")
except Exception as e:
    print(f"\n{RED}[!] An error occurred: {e}{RESET}")