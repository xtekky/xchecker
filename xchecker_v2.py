import random, threading, time, os, sys
try:
    import requests, uuid, colorama, cursor
except ImportError as e:
    input(f"Package {e} is not installed")
    sys.exit(f"Install {e}")

class Checker:
    def __init__(self):
        colorama.init(convert=True, autoreset=True)
        cursor.hide()

        self.mag      = colorama.Fore.MAGENTA
        self.grn      = colorama.Fore.GREEN
        self.white    = colorama.Fore.WHITE
        self.blue     = colorama.Fore.CYAN

        self.sample   = "abcdefghijklmnopqrstuvwxyz"
        self.num      = 4
        self.threads  = 10 # Quasi no ratelimit when under 10
        self.owner    = 'tekky'
        self.skid     = 'you'

        self.hits     = 0
        self.fails    = 0
        self.rates    = 0

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''{self.mag}
    ██╗  ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
    ╚██╗██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
     ╚███╔╝ ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
     ██╔██╗ ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██╔╝ ██╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{self.white}
    ONLP © 2022 ~ Tekky#9999\n''', '__________'*10, "\n\n")

        self.thread_starter()

    def title(self):
        while True:
            os.system(f'title ONLP X TikTok Checker ^| Hits ~ {self.hits} : Fails ~ {self.fails} : Rates ~ {self.rates} : Threads ~ {threading.active_count()}' if os.name == 'nt' else '')

    def check(self):

        _username = ''.join(random.choices(self.sample, k=self.num))

        response = requests.get(
            url = 'https://api2.musical.ly/aweme/v1/search/sug/',
            params = {
                'aid': 1233,
                'device_id': random.randint(1000000000000000000, 9999999999999999999),
                'keyword': _username,
                'source': 'discover'
            },
            headers= {
                'Host'          : 'api2.musical.ly',
                'Connection'    : 'close',
                'sdk-version'   : '1',
                'User-Agent'    : 'TikTok 13.3.0 rv:133016 (iPhone; iOS 14.6; onlp@numbers=latn) Cronet'
            }
        )

        if f'"content":"{_username}"' in response.text:
            self.fails += 1

        elif '"info":"{}"' in response.text:
            print(f'    [ {self.grn}$ {self.white}] Available/Banned {self.blue}{_username}{self.white} '); print(_username, file=open('available.txt','a'))
            self.hits += 1

        elif response.status_code == 403:
            #print(' [ x ] Ratelimited, waiting ! (20s)')
            self.fails += 1
            self.rates += 1
            time.sleep(20)

        else:
            self.fails += 1
    
    def check2(self):
        while True:
            _username_v1 = ''.join(random.choices(self.sample, k=self.num))

            headers = {
                        "user-agent"      : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36" ,
                        "accept-encoding" : "gzip, deflate, br"                                                                                                  ,
                        "accept-language" : "en-US"                                                                                                              ,
                        "content-type"    : "application/json"
                        }
            response_v2 = requests.head(f"https://www.tiktok.com/@{_username_v1}", headers=headers)

            if response_v2.status_code == 200:
                self.fails += 1

            elif response_v2.status_code == 404:
                print(f'    [ {self.grn}$ {self.white}] Available/Banned {self.blue}{_username_v1}{self.white} '); print(_username_v1, file=open('available.txt','a'))
                self.hits += 1

            elif response_v2.status_code == 403:
                #print(' [ x ] Ratelimited, waiting ! (20s)')
                self.fails += 1
                self.rates += 1
                time.sleep(20)

            else:
                self.fails += 1


    def thread_starter(self):
        threading.Thread(target=self.title).start()

        for _ in range(6):
            threading.Thread(target=self.check2).start()

        while True:
            if threading.active_count() < self.threads + 6:
                threading.Thread(target=self.check).start()

Checker()
