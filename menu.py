import variasFotos as f
import redeNeural as rn
import classificar as cl

#TEMPO DE PREVIEW (PARA AJUSTAR O DE ACORDO COM A CÂMERA)
f.preview_camera(30)

#NUM DE FOTOS, PAUSA ENTRE FOTOS (SEGUNDOS), NOME BASE (NOME + 1, nOME +2, ETC). 
#f.obter_fotos(50, 2, "pecas_ruins")

#GERAR A MATRIZ DE UM GRUPO DE IMAGENS (O IDENTIFICADOR É O NOME DADO ÀS IMAGENS DO MESMO GRUPO (apenas o grupo desejado))
df = f.montar_matriz("peca_boa")
#print(df)

#Gera o modelo treinado de inteligencia computacional para classificar as imagens.
model = rn.treinar(df)

#Classifica uma imagem utilizando o modelo treinado acima.
#print(f.extrair_features("C:/Users/mateu/OneDrive/Documentos/ProjetoMoinho/img/peca_boa0.jpg"))
print(cl.classificar(model, f.extrair_features("/home/pi/Documents/ProjetoMoinho/img_testes/teste1.jpg")))
