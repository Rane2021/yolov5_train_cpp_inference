'''
Description: 
将用coco格式的json转化成labeime标注格式的json

coco格式的json由 04_pred_traindata_to_coco.py 生成

Date: 2022-09-06 10:44:19
LastEditTime: 2022-09-13 11:43:04
FilePath: /09_yolov5/05_coco2labelme_json.py
'''
import os
import cv2
import json
import numpy as np
from tqdm import tqdm
from utils.labelme_json import labelme_json


if __name__ == '__main__':
    # set param
    json_path = 'runs/val/exp_231206_fanyingshi_screen_v1/best_predictions.json'
    img_type = ".jpg"


    with open(json_path, 'r') as load_f:
        load_dict = json.load(load_f)

    all_dict = {}
    for idx_box in tqdm(load_dict):
        if idx_box["score"] > 0.2:
            idx_box["image_id"] = str(idx_box["image_id"])
            shape_i = {}
            shape_i["group_id"] = None
            shape_i["shape_type"] = "rectangle"
            shape_i["flags"] = {}
            shape_i["label"] = "type" + str(idx_box["category_id"])
            shape_i["points"] = [[idx_box["bbox"][0], idx_box["bbox"][1]], 
                                 [idx_box["bbox"][0] + idx_box["bbox"][2], 
                                 idx_box["bbox"][1] + idx_box["bbox"][3]]]

            if idx_box["image_id"] in all_dict:
                all_dict[idx_box["image_id"]]["shapes"].append(shape_i)
            else:
                all_dict[idx_box["image_id"]] = {}
                all_dict[idx_box["image_id"]]["imagePath"] = idx_box["image_id"] + img_type
                
                all_dict[idx_box["image_id"]]["shapes"] = []
                all_dict[idx_box["image_id"]]["shapes"].append(shape_i)
                
                all_dict[idx_box["image_id"]]["imageHeight"] = 1080
                all_dict[idx_box["image_id"]]["imageWidth"] = 1080
                all_dict[idx_box["image_id"]]["imageData"] = None
                all_dict[idx_box["image_id"]]["version"] = "5.0.1"
                all_dict[idx_box["image_id"]]["flags"] = {}
                

    # save label json
    save_path = os.path.join(os.path.dirname(json_path), 'labelme_json')
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for key in all_dict:
        idx_json = all_dict[key]
        s_json = json.dumps(idx_json)
        with open(os.path.join(save_path, idx_json["imagePath"].replace(img_type, '.json')), 'w') as jf:
            jf.write(s_json)

print("finish!")

    
   
