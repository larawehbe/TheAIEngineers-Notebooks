import cv2
import numpy as np
from skimage import filters
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from scipy import ndimage
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Helper function to display images
def show_images(images, titles):
    fig, axs = plt.subplots(1, len(images), figsize=(15, 5))
    for i, (img, title) in enumerate(zip(images, titles)):
        axs[i].imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        axs[i].set_title(title)
        axs[i].axis('off')
    plt.tight_layout()
    plt.show()

# 1. Basic Global Thresholding
def global_threshold(image, threshold=127):
    _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary

# 2. Otsu's Thresholding
def otsu_threshold(image):
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

# 3. Adaptive Thresholding
def adaptive_threshold(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 4. Watershed Segmentation
def watershed_segmentation(image):
    # Compute the distance transform
    distance = ndimage.distance_transform_edt(image)
    # Find local maxima
    local_max = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=image)
    # Create markers
    markers = ndimage.label(local_max)[0]
    # Apply watershed
    labels = watershed(-distance, markers, mask=image)
    return labels

# 5. K-means Segmentation
def kmeans_segmentation(image, k=3):
    # Reshape the image
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    # Define criteria and apply kmeans
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    # Convert back to 8 bit values
    centers = np.uint8(centers)
    # Flatten the labels array
    labels = labels.flatten()
    # Convert all pixels to the color of the centroids
    segmented_image = centers[labels.flatten()]
    # Reshape back to the original image dimension
    segmented_image = segmented_image.reshape(image.shape)
    return segmented_image

# 6. U-Net Segmentation (assuming you have a pre-trained model)
def unet_segmentation(image, model):
    # Preprocess the image
    img = cv2.resize(image, (256, 256))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    # Predict
    pred = model.predict(img)
    
    # Post-process the prediction
    pred = (pred > 0.5).astype(np.uint8)
    pred = np.squeeze(pred, axis=0)
    pred = cv2.resize(pred, (image.shape[1], image.shape[0]))
    
    return pred * 255

# Main execution
if __name__ == "__main__":
    # Load an image
    image = cv2.imread('path_to_your_image.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply different segmentation techniques
    global_thresh = global_threshold(gray)
    otsu_thresh = otsu_threshold(gray)
    adaptive_thresh = adaptive_threshold(gray)
    watershed_seg = watershed_segmentation(otsu_thresh)
    kmeans_seg = kmeans_segmentation(image)
    
    # Display results
    show_images([image, global_thresh, otsu_thresh, adaptive_thresh, watershed_seg, kmeans_seg],
                ['Original', 'Global Threshold', 'Otsu Threshold', 'Adaptive Threshold', 'Watershed', 'K-means'])
    
    # For U-Net (uncomment if you have a trained model)
    # model = load_model('path_to_your_unet_model.h5')
    # unet_seg = unet_segmentation(image, model)
    # show_images([image, unet_seg], ['Original', 'U-Net Segmentation'])

# Note: For the U-Net example, you'll need a pre-trained model. 
# Training a U-Net is beyond the scope of this example, but you can find pre-trained models online.