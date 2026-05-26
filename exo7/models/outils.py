import time
import os 

class Outils:

    @staticmethod
    def clear_console(clear):
        clear = os.system("cls")
        return clear
    
    @staticmethod
    def pauses(seconde):
        seconde = time.sleep(3)
        return seconde
