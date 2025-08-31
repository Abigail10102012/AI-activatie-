import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


os.makedirs("output_images", exist_ok=True)


image = cv2.imread("original_images/sample.jpg")  


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()


cropped_image = image[100:300, 200:400]


(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))


brightened_image = cv2.convertScaleAbs(image, alpha=1, beta=50)


cv2.imwrite("output_images/grayscale.jpg", gray_image)
cv2.imwrite("output_images/cropped.jpg", cropped_image)
cv2.imwrite("output_images/rotated.jpg", rotated_image)
cv2.imwrite("output_images/brightened.jpg", brightened_image)

print("All transformed images saved in output_images folder.")
