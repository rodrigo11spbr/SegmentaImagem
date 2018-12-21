from processamento import Processamento

caminhoImagem = 'AnaliseImagem/Imgs/Mario.jpg'

def segmentarImagem(caminhoImagem) :

        largura, altura, imagem = Processamento.get_propriedade_imagem(caminhoImagem)
        matriz = Processamento.get_matriz_mae(largura, altura, imagem)
        
        MatrizSegmentada = [[0 for x in range(largura)] for y in range(altura)]

        for x in range(0, largura) :
                for y in range(0, altura) :
                        if matriz[x][y] <= 186 :
                                MatrizSegmentada[x][y] = matriz[x][y]
                        else :
                                MatrizSegmentada[x][y] = 123

        Processamento.montar_imagem_array(MatrizSegmentada)

if __name__ == '__main__' :
        segmentarImagem(caminhoImagem)