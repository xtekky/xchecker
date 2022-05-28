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

        _head_v1 = {
                'Host'          : 'api2.musical.ly'                                                      ,
                'Connection'    : 'close'                                                                ,
                'sdk-version'   : '1'                                                                    ,
                'User-Agent'    : 'TikTok 13.3.0 rv:133016 (iPhone; iOS 14.6; onlp@numbers=latn) Cronet' ,
                'x-tt-trace-id' : '00-f9a861fb243149ececad769a2f885ed7-f9a861fb243149ec-01'              ,
                'X-Khronos'     : '1651151348'                                                           ,
                'X-Gorgon'      : '830077702001086c95c07d5bae723fcdaa9ea05f9960faad72f8'
            }

        _api = f'https://api2.musical.ly/aweme/v1/search/sug/?aid=1233&version_code=13.3.0&pass-region=1&pass-route=1&language=en&app_name=musical_ly&vid={uuid.uuid4()}&app_version=13.3.0&carrier_region=TK&is_my_cn=0&channel=App%20Store&mcc_mnc=41601&device_id={uuid.uuid4()}&tz_offset=10800&account_region=&sys_region=TK&locale=en&residence=TK&screen_width=1125&uoo=1&openudid=7426eb7827be74f624392caad15e75cecb964e47&os_api=18&ac=WIFI&os_version=14.6&app_language=en&tz_name=Asia/Amman&current_region=ONLP&device_platform=iphone&build_number=133016&device_type=iPhone11,2&iid=7091638634483238662&idfa={uuid.uuid4()}&keyword={_username}&source=discover'

        response = requests.get(_api, _head_v1)

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
