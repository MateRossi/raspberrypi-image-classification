# coding=utf-8

import variasFotos as f
import redeNeural as rn
import classificar as cl

CAMINHO_IMGS = "/home/pi/raspberrypi-image-classification/img/"
CAMINHO_NOVA_IMG = "/home/pi/raspberrypi-image-classification/img_testes/"

#TEMPO DE PREVIEW (PARA AJUSTAR O DE ACORDO COM A CaMERA)
#f.preview_camera(30)

#NUM DE FOTOS, PAUSA ENTRE FOTOS (SEGUNDOS), NOME BASE (NOME + 1, nOME +2, ETC). 
#f.obter_fotos(50, 2, "pecas_ruins")

#GERAR A MATRIZ DE UM GRUPO DE IMAGENS (O IDENTIFICADOR É O NOME DADO ÀS IMAGENS DO MESMO GRUPO (apenas o grupo desejado))
#df = f.montar_matriz("peca_boa")
#print(df)


#Gera o modelo treinado de inteligencia computacional para classificar as imagens.

#model = rn.treinar(df)

#Classifica uma imagem utilizando o modelo treinado acima.
#print(f.extrair_features("C:/Users/mateu/OneDrive/Documentos/ProjetoMoinho/img/peca_boa0.jpg"))

#print(cl.classificar(model, f.extrair_features("/home/pi/Documents/ProjetoMoinho/img_testes/teste1.jpg")))

df = None
model = None

# Solicita ao usuário a escolha de ação
while True:    
    print("Escolha uma opção:")
    print("1 - Preview da Câmera")
    print("2 - Obter Fotos de Treinamento")
    print("3 - Treinar o Modelo de Classificação")
    print("4 - Classificar uma foto")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    resultado_classificacao = "Não realizado."

    # Executa a ação correspondente
    if opcao == 0:
        break
    elif opcao == 1:
        segundos = int(input("Tempo da preview: "))
        f.preview_camera(segundos)
    elif opcao == 2:
        quantidade = int(input("Quantidade de fotos: "))
        pausa = float(input("Pausa entre fotos (segundos): "))
        nome = input("Nome do arquivo: ")
        f.obter_fotos(quantidade, pausa, nome)
        print("Quantidade de fotos: ", quantidade, ". Pausa entre fotos: ", pausa, ". Nome das imagens: ", nome)
    elif opcao == 3:
        identificador = input("Identificador do grupo desejado (nome base das fotos que se procura): ")
        dataframe = f.montar_matriz(identificador)
        df = dataframe
        print(df)
        modelo = rn.treinar(df)
        model = modelo
        print("Modelo de classificação: ", model)
    elif opcao == 4:
        caminho_img = "C:/Users/mateu/OneDrive/Documentos/raspberrypi-image-classification/img_testes/img_teste.jpg" 
        #caminho_img = f.obter_foto('img_teste')]
        #f.extrair_features(caminho_img)
        resultado_classificacao = cl.classificar(modelo, f.extrair_features(caminho_img))
        print("Imagem classificada como: ", resultado_classificacao)
    else:
        print("Escolha uma opção válida!")


    

