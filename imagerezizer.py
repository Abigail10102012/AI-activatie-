import cv2

input_filename = 'input_image.jpg'
image = cv2.imread(input_filename)

if image is None:
    print(f"Error: Unable to load image '{input_filename}'.")
    exit()

sizes = {
    "small": (200, 200),
    "medium": (400, 400),
    "large": (600, 600)
}

for label, size in sizes.items():
    resized_image = cv2.resize(image, size)
    
    window_name = f"Image - {label.capitalize()}"
    cv2.imshow(window_name, resized_image)
    
    output_filename = f"input_image_{label}.jpg"
    cv2.imwrite(output_filename, resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()