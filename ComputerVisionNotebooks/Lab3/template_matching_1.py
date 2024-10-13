import cv2
import numpy as np
import matplotlib.pyplot as plt

def template_matching(image_path, template_path):
    # Read the main image
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    # Read the template
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]
    
    # Perform template matching
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    
    # Specify a threshold
    threshold = 0.8
    
    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)
    
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    
    # Display the result
    plt.subplot(121), plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))
    plt.title('Detected Point'), plt.axis('off')
    plt.subplot(122), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.axis('off')
    plt.show()

# Usage
image_path = 'path/to/your/main_image.jpg'
template_path = 'path/to/your/template_image.jpg'
template_matching(image_path, template_path)
"""

Notes
ome notes and potential modifications:

The threshold value (0.8) can be adjusted based on your needs. A higher threshold will result in fewer but more accurate matches, while a lower threshold will find more potential matches but may include false positives.
This script uses the normalized correlation coefficient method for matching. OpenCV provides several other methods (like cv2.TM_SQDIFF, cv2.TM_CCORR, etc.) which you can experiment with.
For multiple matches, this script will draw rectangles for all matches above the threshold. If you only want the best match, you can use cv2.minMaxLoc() on the result instead of np.where().
This method works best when the template image is very similar to the portion of the main image you're trying to match (including size, rotation, etc.). For more complex scenarios, you might need to look into more advanced techniques like feature matching.
"""

### Best match example :
import cv2
import numpy as np
import matplotlib.pyplot as plt

def template_matching_best_match(image_path, template_path):
    # Read the main image
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    # Read the template
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]
    
    # Perform template matching
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    
    # Find the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Get the location of the best match
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    # Draw a rectangle around the best match
    cv2.rectangle(img_rgb, top_left, bottom_right, (0,255,0), 2)
    
    # Display the result
    plt.subplot(121), plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))
    plt.title('Best Match'), plt.axis('off')
    plt.subplot(122), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.axis('off')
    plt.suptitle(f'Best match score: {max_val:.2f}')
    plt.show()

# Usage
image_path = 'path/to/your/main_image.jpg'
template_path = 'path/to/your/template_image.jpg'
template_matching_best_match(image_path, template_path)
