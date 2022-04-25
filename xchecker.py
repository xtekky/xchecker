#-------------------------------------------------------------------------------------------------
# Xchecker v2 by Tekky
# Copyright (c) 2022 Tekky. All rights reserved.
# I am not responsible for any damage caused by your use of this software.
#-------------------------------------------------------------------------------------------------

try:
    import os
    from threading import Thread, active_count
    import requests
    from pystyle import *
    from random import randint, choices
    import msvcrt
    import time
except ImportError as e:
    print(f"Error while importing [{e}]")

usernames = []
available = 0
unavailable = 0

class Main:
    def main(user, x):
        global available, unavailable, ls, usernames
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "content-type": "application/json"
        }
        r = requests.head(f"https://www.tiktok.com/@{user}", headers=headers)

        if r.status_code == 200:
            unavailable += 1
            print(Colorate.Diagonal(Colors.red_to_black, f'          [Unavailable]: [ {user} ] [id={randint(1000000000000000000, 9999999999999999999)}] [{x}]', 1))
            os.system(f"title Tekky @ 2022 ^| Banned: {available} ^| Unavailable: {unavailable} ^| Checked: {(available + unavailable)} ^| Remaining: {len(usernames) - (available + unavailable)}")

        elif r.status_code == 404:
            with open("banned.txt", "a") as d:
                d.write(user + "\n")
            available += 1
            print(Colorate.Diagonal(Colors.green_to_white, f'          [  Banned   ]: [ {user} ] [id={randint(1000000000000000000, 9999999999999999999)}] [{x}]', 1))
            os.system(f"title Tekky @ 2022 ^| Banned: {available} ^| Unavailable: {unavailable} ^| Checked: {(available + unavailable)} ^| Remaining: {len(usernames) - (available + unavailable)}")

    def start():
        global usernames
        x = 0

        while x < (len(usernames)):
            if active_count() < 5:
                user = usernames[x]
                Thread(target=Main.main, args=(user, x,)).start()
                x = x + 1
            else:
                pass
        
        Write.Print("          [?] Checked successfully \n", Colors.cyan_to_blue, interval=0.0001)
        input()


class Other:
    def logo():
        global file2, file3, ls
        
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
            
            x = 0

            # url input

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

            Write.Print("          [?] Amount ↓\n", Colors.cyan_to_blue, interval=0.000001)
            count = int(Write.Input("           >  ", Colors.cyan_to_blue, interval=0.0000000005, hide_cursor=True))
            
            
            if count > 5000000:
                count = 5000000

            while x < count:
                user = ''.join(choices(chrs, k=num))
                
                if not user[-1].isdigit():
                    if not user.isdecimal():
                            if not user[-1] == ".":
                                usernames.append(user)
                                x += 1
                
                
            print('\n\n')
            Write.Print("          [?] Generated successfully \n", Colors.cyan_to_blue, interval=0.0001)
            print('\n\n')
            time.sleep(0.3)
            Main.start()
            input()

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
        start_()


def start_():
    os.system('cls' if os.name == 'nt' else 'clear')
    Other.logo()


if __name__ == "__main__":
    os.system(f"title Tekky @ 2022 - Xchecker")
    start_()
