from PIL import Image
import numpy as np

class Processamento:

    def get_propriedade_imagem(caminho_imagem) :
        imagem = Image.open(caminho_imagem).convert('RGB')

        width, height = imagem.size

        return width, height, imagem
    
    def get_matriz_mae(largura, altura, imagem) :
        matriz = [[0 for x in range(largura)] for y in range(altura)] 
        for x in range(0, largura) :
                for y in range(0, altura) : 
                        r, g, b = imagem.getpixel((x, y))

                        lRed = round(r * 0.3)
                        lGreen = round(g * 0.59)
                        lBlue = round(b * 0.11)
                        
                        matriz[x][y] = lRed + lGreen + lBlue
        
        return matriz

    def montar_imagem_array(matriz) :
        return Image.fromarray(np.asarray(matriz)).show()
