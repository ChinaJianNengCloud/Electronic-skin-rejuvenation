# 项目介绍
该项目是电子皮肤项目，拥有一个模拟皮肤的装置，可以把一些具有特殊形状的物体与该装置进行接触，能得到压力值数据。
目前有的数据是压力数据转成的热力图以及对应的用照相机拍该物体，之后提取该物体的轮廓，用黑红两种颜色表示该物体，黑色表示背景，红色表示掩码数据。
该项目实现的是，将热力数据转成掩码数据。
在项目中，热力数据描述为画质不清晰数据掩码数据为画质清晰数据。

# 项目来源:
https://github.com/xinntao/Real-RSRGAN

环境安装
可以通过GitHub的项目进行环境的安装，环境的requirements.txt在project文件夹中

# 项目使用
## 1.准备元信息 txt
准备两个文件夹的数据(图片)，其中一个是画质较差的数据，另外一个是画质较好的数据，里面的数据要名字一一对应，数量也要对应
数据的路径在/data/relidata
我已经将数据分成了两部分，训练数据和测试数据。
可以使用脚本进行元信息txt的准备

其中，input后面先更高质量数据路径后是低质量数据路径，--root同理，指定数据的根目录，--meta_info 指定生成元数据的路径和名字

 python project/scripts/generate_meta_info.py --input data/relidata/train-data/hq, data/relidata/train-data/lq --root data/relidata/train-data, data/relidata/train-data --meta_info /data/meta/relidata.txt

## 2.修改配置文件

在/project/options/finetune_realesrgan_x4plus_pairdata.yml
修改datasets中的dataroot_gt和dataroot_lq和meta_info

gt为高质量的图片路径，lq为低质量的图片路径，meta_info为上面得到的txt的路径（这个路径需要跟txt里面的路径拼接，即dataroot的路径加上relidata.txt中的路径为图片的相对路径）

同理val也需要修改

同理model路径也要修改(因为这个项目属于对抗网络，因此存在两个模型参数，一个是生成器一个是判断器)
其中pretrain_network_g是生成器，pretrain_network_d是判断器
这两个原始参数文件我准备上传到网盘，我训练好的参数也放网盘，路径暂定。

## 3.训练
python /project/realesrgan/train.py -opt /project/options/finetune_realesrgan_x4plus_pairdata.yml --auto_resume
可以直接运行start.py

## 4.推理
使用inference.py
注:在项目根目录中的nni.json和nniconfig.yml是我使用nni进行最优调参的产物

# 项目结果

模型的参数以及最终结果展示都在S:\baidu\sjwlab\chenyinda\project\电子皮肤还原实验\result

bestprsn是在指标prsn最好的情况下生成器的模型参数，bestssim是ssim指标最好的情况下的生成器参数。

