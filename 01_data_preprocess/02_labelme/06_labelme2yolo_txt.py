'''
Description: 

1、label json 标注文件转为 yolo txt 标注文件
2、文件名中添加IPxxx, 分别存入 images labels

Date: 2022-09-02 15:45:31
LastEditTime: 2022-09-13 14:37:48
FilePath: /09_yolov5/01_data_preprocess/02_labelme/06_labelme2yolo_txt.py
'''
from fileinput import close
import shutil
import json
import os


# Labelme坐标到YOLO V5坐标的转换
def convert(size, box):
    '''
    description: 
    event: 
    return: x_center/image_width y_center/image_height width/image_width height/image_height
    '''    
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def decode_json(json_floder_path, json_name, save_path, ip_prefix):
    txt_name = os.path.join(save_path, json_name[0:-5] + '_' + ip_prefix + '.txt')
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:
        if i['shape_type'] == 'rectangle':
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])
            
            label = i['label'][-1]  # 大于10类存在问题
            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write( label + " " + " ".join([str(a) for a in bbox]) + '\n')

    txt_file.close()
    

if __name__ == "__main__":
    ip_prefix = 'ip142'
    labelme_json_path = '/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/0913_oldAdd_IP136_138_140_142/IP136_138_140_142_data/IP142'
    # 图像和标注文件分别存入 save_path/images save_path/labels
    save_path = "/home/rane/2TDisk/01_Projects/04_huagong_proj/Dataset_Fanyingshi/0913_oldAdd_IP136_138_140_142/IP136_138_140_142_data/all_images_labels"
    
    
    
    save_images_path = os.path.join(save_path, 'images')
    save_labels_path = os.path.join(save_path, 'labels')
    if not os.path.exists(save_images_path):
        os.mkdir(save_images_path)
    if not os.path.exists(save_labels_path):
        os.mkdir(save_labels_path)
    
    json_names = os.listdir(labelme_json_path)
    for json_name in json_names:
        if '.json' in json_name:
            decode_json(labelme_json_path, json_name, save_labels_path, ip_prefix)
        if '.jpg' in json_name:
            shutil.copy(os.path.join(labelme_json_path, json_name), 
                        os.path.join(save_images_path, json_name.replace('.jpg', '_'+ip_prefix+'.jpg')))


    print("finsih!")


