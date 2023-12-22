# ME3221--测试原理与技术大作业
## 滤波器实验代码
### by 董前程 庞博 吴欣怡 赵四维
### School of Mechanical Engineering , SJTU

在原始文件中，以"-origin.csv"结尾的为原始采集数据，以"-filtered-xxHz.csv"为经过Kilster仪器自带的滤波器滤波产生的原始数据，"xx"表示滤波器的截止频率。

比如，[7-filtered-60Hz](./7-filtered-60Hz) 代表第7组实验(实验参数可见报告),数据经过原始滤波，截止频率为 60Hz。

在单独力文件中，有 ![](https://latex.codecogs.com/svg.image?&space;27(3\times9)) 张图，分别为不同正交实验条件下3个方向力的数据。受力作图文件是整合结果。

在[DataProcessing.ipynb](./DataProcessing.ipynb)中是尝试了不同的滤波器的实验结果（巴特沃斯滤波、高斯滤波、小波变换）。

在[orthogonal_plot.py](./orthogonal_plot.py)中是对正交实验结果图的绘制。

---
指导老师：孙方宏
Thank you for your watching!

