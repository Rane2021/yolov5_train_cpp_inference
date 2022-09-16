'''
Description: 
Date: 2022-08-25 14:43:50
LastEditTime: 2022-08-25 15:17:29
FilePath: /09_yolov5/00_del_other_type.py
'''
import os
from tkinter import Label

label_txt_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Dumei/0822-ip121_2_3+0/01_ori_data/ip121_2_3_all/label_ori_type123.txt"


save_txt_path = label_txt_path.replace('.txt', '_fix.txt')
with open(save_txt_path, "w") as fw:
    with open(label_txt_path, "r") as fr:
        lines = fr.readlines()
        w_line = ''
        for line in lines:
            boxes = line.strip().split(" ")
            w_line += boxes[0] + ' '
            for b in range(5, len(boxes), 5):
                if float(boxes[b]) == 1:
                    cls_str = '0.0000'
                    w_line += boxes[b-4]+" "+boxes[b-3]+" "+boxes[b-2]+" "+boxes[b-1]+" "+cls_str+" "
            w_line = w_line[:-1] + '\n'
        fw.write(w_line)

print("finish!")


