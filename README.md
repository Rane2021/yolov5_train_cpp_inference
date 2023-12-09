# requirements
目前使用 source activate pytorch1.8

#### update 20231206
```
# 修复由于版本更新出现的库不兼容问题
pip install -r requirement.txt
```


# 检查错误的图像：
使用：python 02_val.py
修改地方：
```apl
1、data/04_dumei_coco128_test.yaml  / 03_fanyingshi_coco128_test.yaml  / 05_chumuqi_coco128_test.yaml 中的 test 图像路径
这里还要注意下类别，有的修改过好多次

2、修改 02_val.py line 346: --data && --weights

3、python 02_val.py
```


# 更新训练集
1、通过验证整理有问题的图像，整理出来，通过 10_coco_label_tool 重新标注数据；
    辅助脚本：runs/vip_train_2023-3/01_get_tesed_data.py
2、将新数据并入最近的一版本模型训练数据集中；

# 重新训练模型

- train chumuqi:
```shell
python 01_train.py --data data/05_chumuqi_coco128.yaml --weights weights/yolov5s.pt  --batch-size 16  --epochs 200  --imgsz 640 
```


- train dumei:
```shell
python 01_train.py --data data/04_dumei_coco128.yaml --weights weights/yolov5s.pt  --batch-size 16  --epochs 200  --imgsz 640  --single-cls

```


- train fangyingshi:
```shell

```


# 导出模型
```shell
python 03_export.py --weights runs/vip_train_2023-3/exp_2023-3-24_dumei/weights/best.pt
```


