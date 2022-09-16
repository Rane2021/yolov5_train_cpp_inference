'''
Author: Rane wang_ran20121
Date: 2022-06-27 15:16:15
LastEditors: Rane wang_ran20121
LastEditTime: 2022-07-06 15:41:48
FilePath: /09_yolov5/00_cp_multi_ip_data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from cv2 import line
import numpy as np
import shutil
import os


# TODO: 复制IP数据，并重命名，不然重复图像数据会很多
val_error_imgs = "val_error_imgs.txt"
data_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Dumei/172.16.236.123_0705_RaneDownLoad"
save_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Dumei/ip121_2_3/ip12123_0706_yolo_v2"
save_prefix = "ip123_"


with open(val_error_imgs, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        img_path = os.path.join(data_path, line)
        if os.path.exists(img_path):
            save_name = save_prefix + line
            shutil.copy(img_path, os.path.join(save_path, save_name))
        else:
            print("******************************not exit image name: ", line)

print("finish!")








