import cv2
from skimage.feature import hog
import matplotlib.pyplot as plt
        
img = 'C:/Users/mateu/OneDrive/Documentos/raspberrypi-image-classification/img_testes/img_teste.jpg'

#ler a imagem
image = cv2.imread(img,  cv2.IMREAD_GRAYSCALE)

#binarizar a imagem
limiar, imglimiar = cv2.threshold(image, 80,255,cv2.THRESH_BINARY_INV)

# extracao de features: HOG
fd, hog_image = hog(image, orientations=5, pixels_per_cell=(10, 10), cells_per_block=(1, 1), visualize=True)

plt.imshow(hog_image, cmap='gray')
plt.show()

print(fd)