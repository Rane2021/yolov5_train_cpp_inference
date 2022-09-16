'''
Description: 复制标注软件标注的label.txt 和图像到同一个文件夹下(IP142 140, 需要根据IP重命名), 
Date: 2022-07-23 17:23:47
LastEditTime: 2022-09-13 15:36:26
FilePath: /09_yolov5/01_data_preprocess/01_labelTool/00_cp_change_name.py
'''
import numpy as np
import shutil
import os


# TODO: 复制IP数据，并重命名，不然重复图像数据会很多
data_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_test/0913_ip136_138_140_142_fanyongshi/172.16.236.142_0913_RaneDownload"
save_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_test/0913_ip136_138_140_142_fanyongshi/all_data"
save_prefix = "_ip142"

# TODO: 仅仅复制图像 + 重命名
list_imgs = os.listdir(data_path)
for fname in list_imgs:
    if 'label' not in fname:
        # base_name = fname.split(".")[0]
        sname = fname.replace(".jpg", save_prefix+'.jpg')
        # shutil.copy(os.path.join(data_path, fname), os.path.join(save_path, base_name+save_prefix+'.jpg'))
        shutil.copy(os.path.join(data_path, fname), os.path.join(save_path, sname))

print("finish!")






