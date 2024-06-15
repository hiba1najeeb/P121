# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(1)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480
resized_image = cv2.resize(mountain, (640,480))



while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)


        # creating thresholds
        lower_bound = np.array([100, 100, 100])
        upper_bound = np.array([255, 255, 255])

    # Thresholding image
        mask = cv2.inRange(frame, lower_bound, upper_bound)

        # Inverting the mask
        inverted_mask = cv2.bitwise_not(mask)



        # Create the final image using np.where()
        final_image = np.where(frame== 0, frame, resized_image)

        # Show the final image
        cv2.imshow('Final Image', final_image)

  

        # show it
        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
