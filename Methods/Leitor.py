from PIL import Image
import numpy as np

caminhoImagem = 'AnaliseImagem/Imgs/Mario.jpg'

def getMatrizLuminosidade(caminhoImagem) :
    
        imagemRenderizada = Image.open(caminhoImagem).convert('RGB')

        width, height = imagemRenderizada.size

        for x in range(width) :
                for y in range(height) :        
                        r, g, b = imagemRenderizada.getpixel((x, y))

                        # Calculo luminosidade
                        red = round(r * 0.3)
                        green = round(g * 0.59)
                        blue = round(b * 0.11)
                        
                        imagemMatriz = np.matrix('{} {} {}'.format(red, green, blue))

                        # imagemMatriz = [[red, green, blue]]

        print(imagemMatriz)
        
if __name__ == '__main__' :
    getMatrizLuminosidade(caminhoImagem)