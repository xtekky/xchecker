#-------------------------------------------------------------------------------------------------
# Xchecker v2 by Tekky
# Copyright (c) 2022 Tekky. All rights reserved.
# I am not responsible for any damage caused by your use of this software.
#-------------------------------------------------------------------------------------------------
try:
    import os, sys, requests, time, msvcrt
    from threading import Thread, active_count
    from pystyle import *
    from random import randint, choices
except ImportError as e:
    print(f"Error while importing [{e}]")

available = 0
unavailable = 0


def main(chrs, num):
    while True:
        user = ''.join(choices(chrs, k=num))

        if not user[-1].isdigit():
            if not user.isdecimal():
                if not user[-1] == ".":

                    global available, unavailable, ls
                    headers = {
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "content-type": "application/json"
                    }
                    r = requests.head(f"https://www.tiktok.com/@{user}", headers=headers)

                    if r.status_code == 200:
                        unavailable += 1
                        print(Colorate.Diagonal(Colors.red_to_black, f'          [Unavailable]: [ {user} ] [id={randint(1000000000000000000, 9999999999999999999)}]', 1))
                        os.system(f"title Tekky @ 2022 ^| Banned: {available} ^| Taken: {unavailable} ^| Checked: {(available + unavailable)}")

                    elif r.status_code == 404:
                        with open("banned.txt", "a") as d:
                            d.write(user + "\n")
                        available += 1
                        print(Colorate.Diagonal(Colors.green_to_white, f'          [  Banned   ]: [ {user} ] [id={randint(1000000000000000000, 9999999999999999999)}]', 1))
                        os.system(f"title Tekky @ 2022 ^| Banned: {available} ^| Taken: {unavailable} ^| Checked: {(available + unavailable)}")
        else:
            pass


def start():

    txt = """
        ╔═╗ ╗   ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
        ╔═╬═╝   │  ├─┤├┤ │  ├┴┐├┤ ├┬┘
        ╚ ╚═╝   └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─
            Made with <3 by Tekky       

       + - - - - -                              
           [1]  Start
           [2]  Documentation     
                           - - - - - +
    """
    print(Colorate.DiagonalBackwards(Colors.cyan_to_blue, Center.XCenter(txt), 1))
    print('\n')

    Write.Print("          [?] Choice \n", Colors.cyan_to_blue, interval=0.0001)
    print('\n')
    input_char = msvcrt.getch()

    if input_char == b'1':

        chrs = 'abcdefghijklmnopqrstuvwxyz'

        Write.Print("          [?] Length ↓\n", Colors.cyan_to_blue, interval=0.0001)
        num = int(Write.Input("           >  ", Colors.cyan_to_blue, interval=0.000000005, hide_cursor=True))

        Write.Print("          [?] Include numbers [y/n] ↓\n", Colors.cyan_to_blue, interval=0.0001)
        choice = Write.Input("           >  ", Colors.cyan_to_blue, interval=0.000000005, hide_cursor=True)
        if choice == "y":
            chrs = ''.join((chrs, '0123456789'))

        Write.Print("          [?] Include characters (._) [y/n] ↓\n", Colors.cyan_to_blue, interval=0.00000001)
        choice1 = Write.Input("           >  ", Colors.cyan_to_blue, interval=0.00000005, hide_cursor=True)
        if choice1 == "y":
            chrs = ''.join((chrs, '_.'))

        while True:
            if active_count() < 6:
                Thread(target=main, args=(chrs, num)).start()

            else:
                pass

    elif input_char == b'2':
        os.system('cls' if os.name == 'nt' else 'clear')
        txt = """
           Version: v2.0.1

         Author: Tekky#9999

Source: github.com/xtekky/xchecker    

       Server: discord.gg/onlp

    """
    print(Colorate.DiagonalBackwards(Colors.cyan_to_blue, Center.XCenter(txt), 1))
    print('\n')
    input()
    os.system(f"python {sys.argv[0]}")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title Tekky @ 2022 - Xchecker")
    start()
