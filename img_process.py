# -*-coding:utf-8-*-
import cv2
import os
import numpy as np

def img_process(img_path):
    j = 0
    for i in os.listdir(img_path):
        j += 1
        tmp_img = cv2.imread(os.path.join(img_path, i))
        tmp_img = cv2.resize(tmp_img, (256, 256))
        cv2.imwrite("%s/%d.jpg" % (img_path, j), tmp_img)
        print(i)


if __name__ == '__main__':
    img_process("data/hands/imgs")
