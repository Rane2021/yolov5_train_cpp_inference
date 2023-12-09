import os

image_path = "/home/rane/1T-SSD/01_Projects/04_huagong_proj/Dataset_fanyingshi/20231208_update/03_add_enpty_obj_imgs_yolo/images"
label_path = "/home/rane/1T-SSD/01_Projects/04_huagong_proj/Dataset_fanyingshi/20231208_update/03_add_enpty_obj_imgs_yolo/labels"

# 获取./images目录中所有.jpg文件的名称
image_files = [f[:-4] for f in os.listdir(image_path) if f.endswith('.jpg')]

# 获取./labels目录中所有.txt文件的名称
label_files = [f[:-4] for f in os.listdir(label_path) if f.endswith('.txt')]

# 找出存在.jpg但没有对应.txt的文件
missing_files = set(image_files) - set(label_files)

# 在./labels目录中为这些文件创建空的.txt文件
for file in missing_files:
    if file not in label_files:
        with open(os.path.join(label_path, f'{file}.txt'), 'w') as f:
            pass

print("finish")


