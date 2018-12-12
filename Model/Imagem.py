class Img:

    def __init__(self, pixel):
        self.__pixel = pixel

    def setPixel(self, pixel): 
        self.__pixel = pixel
    
    def getPixel(self):
        return self.__pixel