import time
import requests
import colorama
import pyfiglet
from colorama import Fore
print(Fore.MAGENTA+"")
Banner = pyfiglet.figlet_format("HUNTER", font="univers")
print("DISCORD:GOD OF CODING#7378")
print(Banner)
msg = input("Please Insert WebHook Spam Message: ")
webhook = input("Please Insert WebHook URL: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("404 not found》" + webhook)
            time.sleep(5)
            exit()
kingman_top = 1
while kingman_top == 1:
    spam(msg, webhook)