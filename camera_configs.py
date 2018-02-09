#�������������������
#����һ������ʹ��
import cv2
import numpy as np

left_camera_matrix = np.array([[824.93564, 0., 251.64723],
                               [0., 825.93598, 286.58058],
                               [0., 0., 1.]])
left_distortion = np.array([[0.23233, -0.99375, 0.00160, 0.00145, 0.00000]])



right_camera_matrix = np.array([[853.66485, 0., 217.00856],
                                [0., 852.95574, 269.37140],
                                [0., 0., 1.]])
right_distortion = np.array([[0.30829, -1.61541, 0.01495, -0.00758, 0.00000]])

om = np.array([0.01911, 0.03125, -0.00960]) # ��ת��ϵ����
R = cv2.Rodrigues(om)[0]  # ʹ��Rodrigues�任��om�任ΪR
T = np.array([-70.59612, -2.60704, 18.87635]) # ƽ�ƹ�ϵ����

size = (640, 480) # ͼ��ߴ�

# �����������
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# �������map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)