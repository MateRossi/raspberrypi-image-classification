from picamera import PiCamera
from time import sleep
import numpy as np
import cv2
import matplotlib.pyplot as plt

camera = PiCamera ()
camera.framerate = 24

# setando o caminho da pasta onde as imagens serão salvas:
CAMINHO = "/home/pi/Documents/ProjetoMoinho/img/"

name = "imagem"

#input("Para iniciar a câmera, pressione ENTER.")
camera.start_preview (fullscreen=False, window=(50,5, 840, 680))
input("Pressione qualquer enter para tirar a foto.")
camera.capture (CAMINHO + name + '.jpg')
camera.stop_preview ()

# carrega a imagem original.
imgOriginal = cv2.imread(CAMINHO + name + ".jpg")
imc = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2RGB)
#plt.imshow(imc)
#plt.show()

# carrega a imagem em tons de cinza.
imgCinza = cv2.imread(CAMINHO + name + ".jpg", cv2.IMREAD_GRAYSCALE)

# cria uma figura com uma grade 2x2 de subplots
#fig, axs = plt.subplots(1, 2, figsize=(10, 5))

#binarizar a imagem
limiar, imglimiar = cv2.threshold(imgCinza, 117,255,cv2.THRESH_BINARY_INV)
plt.imshow(imglimiar, cmap="gray")
plt.show()




