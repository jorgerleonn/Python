import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '6.jpg'

image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold_value = 150

# el segundo valor corresponde al threshold del color negro
_, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

dark_pixels = np.sum(thresholded_image == 255)
total_pixels = thresholded_image.size
percentage_dark = (1 - (dark_pixels / total_pixels)) * 100

percentage_dark, thresholded_image.shape, total_pixels, dark_pixels

# mostramos la matriz binaria y más datos
grey_color = threshold_value / 255

plt.imshow(thresholded_image, cmap='gray')
plt.colorbar()
plt.title(loc='right',label='Imagen en escala de grises')
plt.text(0,0, f'{percentage_dark:.2f}% gris, gray_threshold = {threshold_value}', 
         color='black', 
         fontsize=12,
         bbox=dict(facecolor=str(grey_color)))
plt.show()