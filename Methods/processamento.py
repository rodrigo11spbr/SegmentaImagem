from PIL import Image
import numpy as np

class Processamento:

    constante_pixel = 0
    media_constante = 20

    def get_propriedade_imagem(caminho_imagem) :
        imagem = Image.open(caminho_imagem).convert('RGB')

        width, height = imagem.size

        return width, height, imagem
    
    def get_matriz_mae(largura, altura, imagem) :
        matriz = [[0 for x in range(altura)] for y in range(largura)]
        for x in range(0, altura) :
                for y in range(0, largura) : 
                        r, g, b = imagem.getpixel((y, x))

                        lRed = round(r * 0.3)
                        lGreen = round(g * 0.59)
                        lBlue = round(b * 0.11)
                        
                        matriz[y][x] = lRed + lGreen + lBlue
        
        return matriz
    
    def verifica_pixel(pixel, constante_pixel, media) :
        
        return constante_pixel - media <= pixel and constante_pixel + media >= pixel

    def montar_imagem_array(matriz) :
        return Image.fromarray(np.asarray(matriz)).show()
