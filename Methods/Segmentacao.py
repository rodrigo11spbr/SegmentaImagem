from processamento import Processamento

caminhoImagem = 'AnaliseImagem/Imgs/teste.jpg'
CONST_MEDIA = 20

def segmentar(caminhoImagem) :

        largura, altura, imagem = Processamento.get_propriedade_imagem(caminhoImagem)
        matriz = Processamento.get_matriz_mae(largura, altura, imagem)
        
        MatrizSegmentada = [[0 for x in range(altura)] for y in range(largura)]

        for x in range(0, altura) :
                for y in range(0, largura) :

                        # FUNÇÃO DE MUNFORD–SHAH A SER MELHORADA
                        constante_pixel = matriz[x][y]
                        for a in range(0, altura) :
                                for b in range(0, largura) :
                                        pixel = matriz[b][a]
                                        if Processamento.verifica_pixel(pixel, constante_pixel, CONST_MEDIA) :
                                                MatrizSegmentada[b][a] = pixel
                                        else :
                                                MatrizSegmentada[b][a] = 0

                        # if matriz[y][x] != 185 and matriz[y][x] != 186 :
                        #         MatrizSegmentada[y][x] = matriz[y][x]
                        # else :
                        #         MatrizSegmentada[y][x] = 0

        Processamento.montar_imagem_array(MatrizSegmentada)

if __name__ == '__main__' :
        segmentar(caminhoImagem)