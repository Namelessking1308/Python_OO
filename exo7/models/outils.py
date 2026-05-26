import time
import os 

class Outils:

    @staticmethod
    def clear_console():
        os.system("cls")
    
    @staticmethod
    def pauses(seconde):
        time.sleep(seconde)
