import os
import shutil

data_path = "/media/rane/RanePan/其它项目/2022-华峰化工/20231205-反应室更新/01_挑选数据"
save_path = "/media/rane/RanePan/其它项目/2022-华峰化工/20231205-反应室更新/01_挑选数据_combine"


# 遍历所有子目录
for dir_name in os.listdir(data_path):
    dir_path = os.path.join(data_path, dir_name)
    # 确保是目录
    if os.path.isdir(dir_path):
        for file_name in os.listdir(dir_path):
            # 确保是jpg文件
            if file_name.endswith('.jpg'):
                # 构建新的文件名和路径
                new_file_name = dir_name + '_' + file_name
                new_file_path = os.path.join(save_path, new_file_name)
                # 复制并重命名文件
                shutil.copy(os.path.join(dir_path, file_name), new_file_path)

print("finish!")

