from PIL import Image

caminhoImagem = 'AnaliseImagem/Imgs/Mario.jpg'

def getMatrizMae(caminhoImagem) :
    
        imagemRenderizada = Image.open(caminhoImagem).convert('RGB')

        width, height = imagemRenderizada.size

        imagemMatriz = [[0 for x in range(width)] for y in range(height)] 

        for x in range(0, width) :
                for y in range(0, height) : 
                        r, g, b = imagemRenderizada.getpixel((x, y))

                        # Calculo luminosidade
                        red = round(r * 0.3)
                        green = round(g * 0.59)
                        blue = round(b * 0.11)
                        
                        imagemMatriz[x][y] = red + green + blue
        
        print(imagemMatriz)
        
if __name__ == '__main__' :
    getMatrizMae(caminhoImagem)