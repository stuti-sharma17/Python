import cv2
import os

# Define the source image path
src_path = r"D:\Python Development\Python\Image_Resizer\gogo-satoru.jpg"

# Read the image
src = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
if src is None:
    print("Error: Image not found or could not be read.")
    exit()

# Display the image
# cv2.imshow("title", src)

# Resize the image
scale_percent = 50  # percent of original size
nwidth = int(src.shape[1] * scale_percent / 100)
nheight = int(src.shape[0] * scale_percent / 100)
dsize = (nwidth, nheight)
output = cv2.resize(src, dsize)
cv2.imshow("title", output)
# Define the output image path in the same folder
output_path = os.path.join(os.path.dirname(src_path), "gogo-satoru_resized.jpg")

# Save the resized image
cv2.imwrite(output_path, output)
print(f"Resized image saved at: {output_path}")

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
