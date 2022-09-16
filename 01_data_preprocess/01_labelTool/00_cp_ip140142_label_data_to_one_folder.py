'''
Description: 复制标注软件标注的label.txt 和图像到同一个文件夹下(IP142 140, 需要根据IP重命名), 
Date: 2022-07-23 17:23:47
LastEditTime: 2022-07-23 19:46:51
FilePath: /09_yolov5/00_cp_ip140142_label_data_to_one_folder.py
'''
import numpy as np
import shutil
import os


# TODO: 复制IP数据，并重命名，不然重复图像数据会很多
data_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/ip142_data/train_v4_change_type3/ip142_train_v2_addtype3_4"
save_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/ip142_data/train_v5_addtype5/ip140_142_all_train_data_before_202207"
save_prefix = "_ip142"

# TODO: 仅仅复制图像 + 重命名
list_imgs = os.listdir(data_path)
for fname in list_imgs:
    if 'label' not in fname:
        base_name = fname.split(".")[0]
        shutil.copy(os.path.join(data_path, fname), os.path.join(save_path, base_name+save_prefix+'.jpg'))

# TODO: label.txt 中重命名图像名称
data_label_path = os.path.join(data_path , "label.txt")
label_save_path = os.path.join(save_path , "202207_type0-4_label.txt")
with open(label_save_path, "a") as sf:
    with open(data_label_path, "r") as of:
        all_read_line = of.readlines()
        for rline in all_read_line:
            rline = rline.split(" ", 1)
            sline = rline[0].replace('.jpg', save_prefix + ".jpg") + " " + rline[1]
            sf.write(sline)

print("finish!")






