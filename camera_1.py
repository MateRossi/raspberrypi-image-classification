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

input("Para iniciar a câmera, pressione ENTER.")
camera.start_preview (fullscreen=False, window=(50,5, 840, 680))
input("Pressione qualquer enter para tirar a foto.")
camera.capture (CAMINHO + name + '.jpg')
camera.stop_preview ()

# carrega a imagem original.
imgOriginal = cv2.imread(CAMINHO + name + ".jpg")

# carrega a imagem em tons de cinza.
imgCinza = cv2.imread(CAMINHO + name + ".jpg", cv2.IMREAD_GRAYSCALE)

# cria uma figura com uma grade 2x2 de subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# exibe as imagens nos subplots
axs[0].imshow(cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2RGB))
axs[0].set_title("Imagem Original")

axs[1].imshow(imgCinza, cmap='gray')
axs[1].set_title("Imagem Em Tons de Cinza")

# Ajusta a disposição dos subplots para evitar sobreposições
plt.tight_layout()

# exibe a figura com os subplots
plt.show(block='false')

# início do cálculo do histograma na imagem em tons de cinza
hist = cv2.calcHist([imgCinza],[0],None,[256],[0,255])

plt.hist(imgCinza.ravel(),256,[0,256])
plt.plot(hist)
plt.title("Histograma da foto em tons de cinza.")

plt.show()




