#from picamera import PiCamera
from time import sleep
import os
import glob
import math
import cv2
import numpy as np
import pandas as pd
import re

#camera = PiCamera ()
#camera.framerate = 24

CAMINHO = "/home/pi/Documents/ProjetoMoinho/img/"
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
    vetor = []
    class_column = []
    for img in caminhos:
        
        #ler a imagem
        image = cv2.imread(img,  cv2.IMREAD_GRAYSCALE)

        #binarizar a imagem
        limiar, imglimiar = cv2.threshold(image, 50,255,cv2.THRESH_BINARY_INV)

        # extração de features: huMoments
        moments = cv2.moments(imglimiar)
        huMoments = cv2.HuMoments(moments)

        for i in range(7):
            huMoments[i] = -1*math.copysign(1.0, huMoments[i]) * math.log10(abs(huMoments[i]))
            data = huMoments
        vetor.append(data)
        if re.search(img_name, img):
            class_column.append(0)
        else:
            class_column.append(1)
    matriz=np.concatenate(vetor, axis=1)
    df = pd.DataFrame(matriz.T, columns=[f'Feature{i}' for i in range(1, 8)])
    df['Class'] = class_column
    return df

def extrair_features(img):
    vetor = []
    #ler a imagem
    image = cv2.imread(img,  cv2.IMREAD_GRAYSCALE)
    #binarizar a imagem
    limiar, imglimiar = cv2.threshold(image, 50,255,cv2.THRESH_BINARY_INV)

    # extração de features: huMoments
    moments = cv2.moments(imglimiar)
    huMoments = cv2.HuMoments(moments)

    for i in range(7):
        huMoments[i] = -1*math.copysign(1.0, huMoments[i]) * math.log10(abs(huMoments[i]))
        data = huMoments

    vetor.extend(data)  # Use extend to add individual elements to the list
    return np.array(vetor).ravel()