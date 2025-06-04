import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


input_path = '../original_images/sample_image.png'  
image = cv2.imread(input_path)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()


cropped_image = gray_image[100:300, 200:400]


(h, w) = cropped_image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(cropped_image, rotation_matrix, (w, h))


brightness_matrix = np.ones(rotated_image.shape, dtype="uint8") * 50
bright_image = cv2.add(rotated_image, brightness_matrix)


os.makedirs('../output_images', exist_ok=True)
output_path = '../output_images/processed_image.png'
cv2.imwrite(output_path, bright_image)
