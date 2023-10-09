# setando o caminho da pasta onde as imagens serão salvas:
CAMINHO = "/home/pi/Documents/ProjetoMoinho/img"

# importando bibliotecas:
import numpy as np
import cv2
import matplotlib.pyplot as plt

# carrega as imagens originais
imgOriginal01 = cv2.imread(CAMINHO + "/imagem01.jpg")
imgOriginal02 = cv2.imread(CAMINHO + "/imagem02.jpg")

# passa as imagens para tons de cinza
imgCinza01 = cv2.imread(CAMINHO + "/imagem01.jpg", cv2.IMREAD_GRAYSCALE)
imgCinza02 = cv2.imread(CAMINHO + "/imagem02.jpg", cv2.IMREAD_GRAYSCALE)

# cria uma figura com uma grade 2x2 de subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# exibe as imagens nos subplots
axs[0, 0].imshow(cv2.cvtColor(imgOriginal01, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title("Flor Original")

axs[0, 1].imshow(imgCinza01, cmap='gray')
axs[0, 1].set_title("Flor em Tons de Cinza")

axs[1, 0].imshow(cv2.cvtColor(imgOriginal02, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title("Pássaro Original")

axs[1, 1].imshow(imgCinza02, cmap='gray')
axs[1, 1].set_title("Pássaro em Tons de Cinza")

# Ajusta a disposição dos subplots para evitar sobreposições
plt.tight_layout()

# exibe a figura com os subplots
plt.show(block='false')

#calcula o histograma de cada imagem
hist1 = cv2.calcHist([imgOriginal01],[0],None,[256],[0,255])
hist2 = cv2.calcHist([imgOriginal02],[0],None,[256],[0,255])

fig = plt.figure(figsize =(10,10))

ax1 = fig.add_subplot(121)
plt.hist(imgCinza01.ravel(),256,[0,256])
plt.plot(hist1)
plt.title("Flor")

ax2 = fig.add_subplot(122)
plt.hist(imgCinza02.ravel(),256,[0,256])
plt.plot(hist2)
plt.title("Pássaro")

plt.show()