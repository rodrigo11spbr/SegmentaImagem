from processamento import Processamento

caminhoImagem = 'AnaliseImagem/Imgs/Mario.jpg'
CONST_MEDIA = 100

def segmentar(caminhoImagem) :

        largura, altura, imagem = Processamento.get_propriedade_imagem(caminhoImagem)
        matriz_original = Processamento.get_matriz_mae(largura, altura, imagem)
        
        matriz_segmentada = [[0 for x in range(altura)] for y in range(largura)]

        for x in range(0, altura) :
                for y in range(0, largura) :

                        # FUNÇÃO DE MUNFORD–SHAH
                        constante_pixel = matriz_original[y][x]     
                        for a in range(0, altura) :
                                for l in range(0, largura) :
                                        pixel = matriz_original[l][a]
                                        if Processamento.verifica_pixel(pixel, constante_pixel, CONST_MEDIA) :
                                                matriz_segmentada[l][a] = pixel
                                        else :
                                                matriz_segmentada[l][a] = 0

        Processamento.montar_imagem_array(matriz_segmentada)

if __name__ == '__main__' :
        segmentar(caminhoImagem)