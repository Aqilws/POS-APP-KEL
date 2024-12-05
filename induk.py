from typing import Any

# Class induk / Parent
class Induk:
    def __init__(self):
        self.__aplication_name = "Aplikasi kasir"
        self.__screen_size = "1000x500"
    
    # Get Aplication name
    def get_aplication_name(self):
        return self.__aplication_name

    # Get screen size
    def get_screen_size(self):
        return self.__screen_size