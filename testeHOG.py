import cv2
from skimage.feature import hog
import matplotlib.pyplot as plt
        
images_path = "C:/Users/PET/Documents/GitHub/raspberrypi-image-classification/img_testes/"

def mostrar_hog(img):

    #ler a imagem
    image = cv2.imread(images_path+img+'.jpg',  cv2.IMREAD_GRAYSCALE)

    #binarizar a imagem
    #limiar, imglimiar = cv2.threshold(image, 80,255,cv2.THRESH_BINARY_INV)

    # extracao de features: HOG
    fd, hog_image = hog(image, orientations=5, pixels_per_cell=(10, 10), cells_per_block=(1, 1), visualize=True)

    plt.imshow(hog_image, cmap='gray')
    plt.show()

    print(fd)