import numpy as np
import imutils
import cv2 


def align_images(image, template, maxFeatures=500, keepPercent = 0.2, debug=False):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    orb = cv2.ORB_create(maxFeatures)
    (kpsA, descA) = orb.detectAndCompute(imageGray, None)
    (kpsB, descB) = orb.detectAndCompute(templateGray, None)
    
    method = cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
    matcher = cv2.DescriptorMatcher_create(method)
    matches = matcher.match(descA, descB)
    
    matches = sorted(matches , key=lambda x:x.distance)

    keep = int(len(matches)*keepPercent)
    matches = matches[:keep]
    
    ptsA = np.zeros((len(matches) , 2 ) , dtype="float")
    ptsB = np.zeros((len(matches) , 2 ) , dtype="float")
    
    
    if debug :
        matchedVis = cv2.drawMatches(image, kpsA, template, kpsB, matches, None)
        matchedVis = imutils.resize(matchedVis, width=1000)
        cv2.imshow("Matched Keypoints" , matchedVis)
        cv2.waitKey(0)
    
    for (i, m ) in enumerate(matches):
        ptsA[i] = kpsA[m.queryIdx].pt
        ptsB[i] = kpsB[m.trainIdx].pt
    
    (H, mask) = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC)
    
    (h,w) = template.shape[:2]

    aligned = cv2.warpPerspective(image, H, (w,h))
    return aligned
    
image = cv2.imread("image.jpg")
template = cv2.imread("main.png")

print("Aligning images")

aligned = align_images(image, template, debug=True)
    

    
aligned = imutils.resize(aligned, width=700)
template = imutils.resize(template, width=700)

stacked = np.hstack([aligned, template])

overlay = template.copy()
output = aligned.copy()
cv2.addWeighted(overlay, 0.5, output, 0.5 , 0 , output)
cv2.imshow("Aligned image stacked" , stacked)
cv2.imshow("Aligned image overlay" , output)
cv2.waitKey(0)

    