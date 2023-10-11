#import variasFotos as f
import redeNeural as rn
import classificar as cl

#TEMPO DE PREVIEW (PARA AJUSTAR O DE ACORDO COM A CÂMERA)
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


def case_1(segundos):
    #f.preview_camera(segundos)
    print("case 1", segundos)

def case_2(quantidade, pausa, nome):
    #f.obter_fotos(quantidade, pausa, nome)
    print("case 2 ", nome)

#retorna a matriz
def case_3(identificador):
    #return f.montar_matriz(identificador)
    print("case 3")

#retorna o modelo
def case_4(dataFrame):
    return rn.treinar(dataFrame)

#retorna o resultado da classificação
def case_5(model, caminho_img):
    return cl.classificar(model, f.extrair_features(caminho_img))

def default():
    print("Escolha uma opção válida.")

switcher = {
    1: case_1,
    2: case_2,
    3: case_3,
    4: case_4,
    5: case_5,
    6: default
}

def switch(case):
    return switcher.get(case, default)()


dataFrame = 0
modelo = 0


# Solicita ao usuário a escolha de ação
while True:    
    print("Escolha uma opção:")
    print("1 - Preview da Câmera")
    print("2 - Obter Fotos de Treinamento")
    print("3 - Montar Matriz")
    print("4 - Treinar o Modelo de Classificação")
    print("5 - Classificar uma foto")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    resultado_classificação = "Não realizado."

    # Executa a ação correspondente
    if opcao == 0:
        break
    elif opcao == 1:
        segundos = int(input("Tempo da preview: "))
        switcher[1](segundos)
    elif opcao == 2:
        quantidade = int(input("Quantidade de fotos: "))
        pausa = float(input("Pausa entre fotos (segundos): "))
        nome = input("Nome do arquivo: ")
        switcher[2](quantidade, pausa, nome)
    elif opcao == 3:
        identificador = input("Identificador: ")
        dataframe = switcher[3](identificador)
    elif opcao == 4:
        modelo = switcher[4](dataFrame)
    elif opcao == 5:
        caminho_img = input("Caminho da imagem: ")
        resultado_classificação = switcher[5](modelo, caminho_img)
        print("Imagem classificada como: ", resultado_classificação)
    else:
        switcher[6]


    

