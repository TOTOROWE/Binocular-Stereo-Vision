# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
#import camera_configs
#cv2.namedWindow("left")
#cv2.namedWindow("right")
#cv2.moveWindow("left", 0, 0)
#cv2.moveWindow("right", 600, 0)
#camera1 = cv2.VideoCapture(0)
#camera2 = cv2.VideoCapture(1)

def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:        
        print(disparity[y][x])

cv2.setMouseCallback("depth", callbackFunc, None)

while True:
    frame1 = cv2.imread('IMG_LEFT.png')
    frame2 = cv2.imread('IMG_RIGHT.png')
#    frame1 = cv2.imread('65L.jpg')
#    frame2 = cv2.imread('65R.jpg')
#    if not ret1 or not ret2:
#        break

#    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
#    img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

    imgL = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoBM_create(numDisparities=0, blockSize=11)
    disparity = stereo.compute(imgL, imgR)

#    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., camera_configs.Q)

#    cv2.imshow("left", imgL)
#    cv2.imshow("right", imgR)
    plt.imshow(disparity,'gray')
    plt.show()
    break

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
        # cv2.imwrite("./snapshot/BM_left.jpg", imgL)
        # cv2.imwrite("./snapshot/BM_right.jpg", imgR)
        # cv2.imwrite("./snapshot/BM_depth.jpg", disp)

#camera1.release()
#camera2.release()
cv2.destroyAllWindows()