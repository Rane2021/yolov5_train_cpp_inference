import os
import shutil


# 源目录和目标目录
src_dir = "/media/rane/RanePan/其它项目/2022-华峰化工/20231205-反应室更新/146"
dst_dir = "/home/rane/1T-SSD/01_Projects/04_huagong_proj/Dataset_fanyingshi/20231208_update/05_add_pred_error_images"

# 文件列表
file_list = [
    "20231114160321",
    "20231114132834",
    "20231114151956",
    "20231114204252",
    "20231108200737",
    "20231108190111",
    "20231108214933",
    "20231109045627",
    "20231108221820",
    "20231109234343"
]


# 确保目标目录存在
os.makedirs(dst_dir, exist_ok=True)

# 遍历文件列表
for file_name in file_list:
    # 源文件和目标文件的完整路径
    file_name = file_name+".jpg"
    src_file = os.path.join(src_dir, file_name[:8],file_name)
    dst_file = os.path.join(dst_dir, "128_" + file_name)

    # 复制文件
    shutil.copy(src_file, dst_file)
print("Done!")

