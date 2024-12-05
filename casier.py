# Hubungkan dengan file induk.py
from induk import Induk

# Buat class casier sebagai chiled dari class Induk
class Casier(Induk):
    def __init__(self):
        super().__init__()

        # List casier Acounts
        self.__casier_acounts = {
            "andris": "adm1",
            "akil": "adm2",
            "tomo": "adm3",
            "nevi": "adm4",
            "rozi": "adm5"
        }

        self.__casier_id = str
        self.__casier_name = str
        self.__new_password = str

    # Set casier Id
    def set_casier_id(self, casier_id):
        self.__casier_id = casier_id
    
    # Set casier Name
    def set_casier_name(self, casier_name):
        self.__casier_name = casier_name

    # Set New Password
    def set_new_password(self, new_password):
        self.__new_password = new_password
    


