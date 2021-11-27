from files.controller import controllerMonitor
from keyboard import is_pressed as pressed
from colorama import Fore, Style, init
import json, os, time


def banner():
    os.system("cls")
    print("\n")
    print("""
                                  /------------------------------------------------\\
                                  |                         __  .__  _____         |
                                  |    ____________   _____/  |_|__|/ ____\__.__.  |
                                  |   /  ___/\____ \ /  _ \   __\  \   __<   |  |  |
                                  |   \___ \ |  |_> >  <_> )  | |  ||  |  \___  |  |
                                  |  /____  >|   __/ \____/|__| |__||__|  / ____|  |
                                  |      \/ |__|                         \/        |
                                  |                   coded by e                   |
                                  \------------------------------------------------/""", Fore.RED, Style.RESET_ALL)
    print("\n")
    print("                                  --------------------controls---------------------")
    print("\n")
    print(f"                                                 activate key: {config['activateKey']}")
    print("                                                  active: ", (Fore.GREEN if spotifyController.active else Fore.RED) + str(spotifyController.active) + Style.RESET_ALL)
    print("\n")
    print("                                  -------------------------------------------------")

with open("config.json") as f:
    config = json.load(f)
    if config["firstTimeRun"]:
        os.system("title spotify setUp")
        print('setting up redirect ui, please rerun after logged in/accepted terms')
        spotifyController = controllerMonitor()
        with open("config.json", "r+") as file:
            config["firstTimeRun"] = False
            file.seek(0)
            json.dump(config, file, indent=4)
        os._exit(0)


os.system("title spotify - coded by e")
spotifyController = controllerMonitor()
spotifyController.activate()
banner()
while True:
    if pressed(config["activateKey"]):
        spotifyController.activate()
        banner()

    if spotifyController.active:
        spotifyController.monitor()
