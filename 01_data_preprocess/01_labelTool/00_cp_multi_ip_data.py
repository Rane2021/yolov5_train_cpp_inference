'''
Author: Rane wang_ran20121
Date: 2022-06-27 15:16:15
LastEditors: Rane wang_ran20121
LastEditTime: 2022-07-04 20:45:20
FilePath: /09_yolov5/00_cp_multi_ip_data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import shutil
import os


# TODO: 复制IP数据，并重命名，不然重复图像数据会很多
data_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/ip142_data/train_v4_change_type3/ip142_train_v2_yolo"
save_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/ip142_data/train_v4_change_type3/all_train"
save_prefix = "_ip142"

if not os.path.exists(save_path + "/images"):
    os.mkdir(save_path + "/images")
if not os.path.exists(save_path + "/labels"):
    os.mkdir(save_path + "/labels")

list_imgs = os.listdir(data_path + "/images")
# list_imgs = os.listdir(data_path + "/labels")

for fname in list_imgs:
    if 'label' not in fname:
        base_name = fname.split(".")[0]
        shutil.copy(os.path.join(data_path, "images", fname), os.path.join(save_path, "images", base_name+save_prefix+'.jpg'))
        shutil.copy(os.path.join(data_path, "labels", base_name+'.txt'), os.path.join(save_path, "labels", base_name+save_prefix+'.txt'))


print("finish!")






