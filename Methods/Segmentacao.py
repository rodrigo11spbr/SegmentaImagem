from PIL import Image
import math
import numpy as np

caminhoImagem = 'AnaliseImagem/Imgs/Mario.jpg'

def __getImagemDetalhe__(caminhoImagem) :
        imagem = Image.open(caminhoImagem).convert('RGB')

        width, height = imagem.size

        return width, height, imagem

def getMatrizMae(caminhoImagem) :

        width, height, imagem = __getImagemDetalhe__(caminhoImagem)

        imagemMatriz = [[0 for x in range(width)] for y in range(height)] 

        for x in range(0, width) :
                for y in range(0, height) : 
                        r, g, b = imagem.getpixel((x, y))

                        lRed = round(r * 0.3)
                        lGreen = round(g * 0.59)
                        lBlue = round(b * 0.11)
                        
                        imagemMatriz[x][y] = lRed + lGreen + lBlue
        
        return width, height, imagemMatriz

def segmentarImagem(matrizMae) :
        width, height, matriz = matrizMae
        MatrizSegmentadaFundo = [[0 for x in range(width)] for y in range(height)] 

        for x in range(0, width) :
                for y in range(0, height) :
                        if matriz[x][y] >= 160 and matriz[x][y] <= 195:
                                MatrizSegmentadaFundo[x][y] = matriz[x][y]
                        else:
                                MatrizSegmentadaFundo[x][y] = 0

        #Monta a imagem e apresenta
        imagemArray = np.asarray(MatrizSegmentadaFundo)
        imagemMontar = Image.fromarray(imagemArray)
        imagemMontar.show()

if __name__ == '__main__' :

        matrizMae = getMatrizMae(caminhoImagem) # Retorna a imagem em uma matriz realizando calculo de luminosidade
        segmentarImagem(matrizMae)