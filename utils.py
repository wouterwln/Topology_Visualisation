import cv2
import os
import numpy as np

def rgb_to_height(image):
     encoding = np.array([1, pow(2, 8), pow(2, 16)])
     return np.dot(image, encoding)

def split(x):
    return int(x.partition(".")[0])

def read_data(dir):
    data = []
    for file in sorted(os.listdir(dir), key=split):
        raw_image_data = cv2.imread("{}/{}".format(dir, file))
        data.append(rgb_to_height(raw_image_data))
    data = np.array(data)
    return data