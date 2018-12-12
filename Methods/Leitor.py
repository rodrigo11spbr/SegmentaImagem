from PIL import Image

caminhoImagem = 'AnaliseImagem/Imgs/Mario.jpg'
def getMatriz(caminhoImagem):
    with Image.open(caminhoImagem) as i :
        pixels = i.getpixel((0, 0))
        dimensoes = width, height = i.size

        print('altura {}'.format(height))
        print('largura {}'.format(width))
        print('pixels {}'.format(pixels))
        

if __name__ == '__main__' :
    getMatriz(caminhoImagem)