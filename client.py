import os
from art import *
import requests
import time
from colorama import Fore, Back, Style
from datetime import datetime

username = os.getlogin()
server = "http://localhost:1337/"

def send(username, message):
    data = {
        "username": username,
        "message": message
    }

    url = f"{server}api/send"
    r = requests.post(url, json=data)

def clearconsole():
    os.system("cls")

def defusername():
    clearconsole()
    print(f"Choose username : \n 1 - Use random username \n 2 - Use the actual user's username ({os.getlogin()}) \n 3 - Use custom username \n")
    choice = input("Enter your choice : ")
    print()

    global username

    #random username
    if choice == "1":
        clearconsole()
        print("Not now.")
        time.sleep(3)
        main()

    #actual user's username
    if choice == "2":
        clearconsole()
        print(f"Your username is now defined to {os.getlogin()}")
        username = os.getlogin()
        time.sleep(2)
    
    #custom username
    if choice == "3":
        clearconsole()
        print("Enter your username here :\n")
        username = input("")
        print("")
        print(f"Your username is now defined to {username}")
        time.sleep(2)

    #err
    else:
        clearconsole()
        print("Enter a valid choice.")
        time.sleep(2)
        main()

def defserver():
    clearconsole()
    print(f"Choose server : \n 1 - Use the talk.py base server \n 2 - Use custom server \n ")
    choice = input("Enter your choice : ")

    global server

    #base server
    if choice == "1":
        clearconsole()
        print(f"Server is now defined to the base server (http://localhost:1337/)")
        time.sleep(2)
        server = "http://localhost:1337/"
    #custom server
    if choice == "2":
        clearconsole()
        server = input("Enter the custom server URL : ")
        print(f"\nServer is now defined to {server}")
        time.sleep(2)
        main()

def chat():
    clearconsole()
    while True:
        clearconsole()
        messages = requests.get(server + "messages")
        print(messages.text)
        msg = input(f"\n{username} > ")
        if msg == "/reload":
            chat()
        send(username=username, message=msg)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if msg == "/exit":
            #mettez la ligne en dessous en commentaire et mettez le if en entier en dessous du if msg plus haut si vous voulez désactiver le message d'au revoir
            send(username=username, message=f"<System> : {current_time} : \n>The user {username} has left the chat\n")
            main()
            


def main():
    clearconsole()
    tprint("talk.py")
    print("")
    print(f"Your username is {username}\n")
    up = requests.get(server)
    global status
    if up == 200:
        status = "OFFLINE"
    else:
        status = "ONLINE"
    print(f"The actual server is {server} " + "[" + "\033[31m" + f"{status}" + "\033[39m" + "]\n" + str(up.status_code))

    
    print("")

    print("\n 1 - Define a new username \n 2 - Define a new server \n 3 - Enter chat \n 4 - Exit talk.py \n")
    
    choice = input("Enter your choice : ")

    if choice == "1":
        defusername()
    
    if choice == "2":
        defserver()
    
    if choice == "3":
        clearconsole()
        chat()
    
    if choice == "4":
        clearconsole()
        print("Exiting talk.py...")
        time.sleep(1)
        print("Goodbye.")
        os._exit(0)

    else:
        clearconsole()
        print("Enter a valid choice.")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()