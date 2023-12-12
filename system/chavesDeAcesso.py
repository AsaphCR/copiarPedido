class Chaves:
    def __init__(self, app_key, app_secret) -> None:
        self.__app_key = app_key
        self.__app_secret = app_secret
    
    def get_key(self):
        return self.__app_key

    def get_secret(self):
        return self.__app_secret


FTG = Chaves("3385006281657", "25aebfbbcb19a37945598729ef4df420")
CR = Chaves("3385021614975", "8dd06fc70bb7987916c69071e775c315")
ECOM = Chaves("3743000923662", "f7d80cb2b9f0de077e30a81da7ecd342")
LBN = Chaves("3385013948316", "e280cda1d19ec6177ce0e69578227c17")
RDB = Chaves("3385044614952", "ce713169230a632e6309b417f00e4697")
IPA = Chaves("3385036948293", "a2c4e7a217a48018e221eb3fca8ab770")
ATAC = Chaves("3385029281634", "f300388f9300adfb90ad24b7dc37a455")
