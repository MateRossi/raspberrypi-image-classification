#from picamera import PiCamera
from time import sleep
import os
import glob
import math
import cv2
import numpy as np
import pandas as pd
import re
from skimage.feature import hog
import matplotlib.pyplot as plt

#camera = PiCamera ()
#camera.framerate = 24

CAMINHO = "/home/pi/raspberrypi-image-classification/img/"
CAMINHO_CLASSIFICACAO = "//home/pi/raspberrypi-image-classification/img_testes/"

caminhos = sorted(glob.glob(os.path.join(os.getcwd(),'img','*.jpg')))

def obter_fotos(numFotos, pausaEntreFotos, nomeBase):
    #camera.start_preview (fullscreen=False, window=(50,5, 840, 680))
    sleep(5)
    for i in range (numFotos):
        #camera.capture (CAMINHO + nomeBase + str(i) + '.jpg')
        sleep(pausaEntreFotos)
    #camera.stop_preview ()

def preview_camera(tempo):
    #camera.start_preview (fullscreen=False, window=(50,5, 840, 680))
    sleep(tempo)
    #camera.stop_preview()

#print(caminhos)

def montar_matriz(img_name):
    count = 0
    vetor = []
    class_column = []
    for img in caminhos:
        
        #ler a imagem
        image = cv2.imread(img,  cv2.IMREAD_GRAYSCALE)

        #binarizar a imagem
        #limiar, imglimiar = cv2.threshold(image, 117,255,cv2.THRESH_BINARY_INV)

        # extracao de features: HOG
        fd = hog(image, orientations=5, pixels_per_cell=(12, 12), cells_per_block=(1, 1), visualize=False)

        vetor.append(fd)
        if re.search(img_name, img):
            class_column.append(0)
        else:
            class_column.append(1)

        count = count + 1
        print(img + ' ', count)
    
    df = pd.DataFrame(vetor, columns=[f'HOG_Feature{i}' for i in range(fd.shape[0])])
    df['Class'] = class_column
    return df

def extrair_features(img):
    #ler a imagem
    image = cv2.imread(img,  cv2.IMREAD_GRAYSCALE)
    #plt.imshow(image, cmap='gray')
    #plt.show()
    # Use extend to add individual elements to the list
    fd = hog(image, orientations=5, pixels_per_cell=(12, 12), cells_per_block=(1, 1), visualize=False)
    print(fd.shape)
    print(fd)
    return fd

def obter_foto(nome):
    #camera.capture (CAMINHO_CLASSIFICACAO + nome + '.jpg')
    return CAMINHO_CLASSIFICACAO + nome + '.jpg'
