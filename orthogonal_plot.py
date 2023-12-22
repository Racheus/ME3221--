import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname="C:\Windows\Fonts\STZHONGS.ttf", size=12)  # 替换为你的中文字体文件路径

# 自定义坐标轴刻度
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y_values = [10.310, 21.453, 30.571, 30.720, 17.766, 13.838, 10.120, 19.919, 32.286]
# y_values = [7.434, 13.370, 14.824, 14.382, 11.988, 9.257, 7.267, 11.534, 16.827]
y_values = [4.728, 7.679, 11.649, 13.452, 6.056, 4.549, 2.455, 7.033, 14.569]

# 绘制图表
plt.plot(x_values[:3], y_values[:3], marker='o', label='Segment 1')
plt.plot(x_values[3:6], y_values[3:6], marker='o', label='Segment 2')
plt.plot(x_values[6:], y_values[6:], marker='o', label='Segment 3')

# 自定义 X 轴刻度
plt.xticks(x_values, ['1', '2', '3', '1', '2', '3', '1', '2', '3'], fontproperties=font)

# 添加标题和标签
plt.title('Fz')
plt.xlabel('进给量                     主轴转速                   切深', fontproperties=font)
plt.ylabel('K值平均值(取绝对值)', fontproperties=font)

# 显示图表
plt.show()