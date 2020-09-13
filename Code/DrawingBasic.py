import matplotlib.pyplot as plt
import random
from matplotlib.pylab import mpl
import matplotlib.ticker as ticker


mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置表格标题中文字体


class Drawing(object):
    """绘制图像类"""

    def draw_chart(self):
        """绘制折线图"""
        # 数据
        x = range(60)
        y = [random.uniform(26, 38) for i in x]
        # 创建画布
        # figsize=(20, 8)定义长宽比，dpi定义图片分辨率
        plt.figure(figsize=(20, 8), dpi=500)
        # 绘图
        plt.plot(x, y)

        # 构造x，y轴标签
        x_ticks_label = ["7:{}".format("%.2d" % (i)) for i in x]
        y_ticks = range(25, 40)
        plt.xticks(x[::5], x_ticks_label[::5])
        plt.yticks(y_ticks[::5])
        # 添加描述信息
        plt.xlabel("Time")
        plt.ylabel("Temporature")
        plt.title("7~8:00 am A&B Cities Temporature Chart")
        # 图像保存
        plt.savefig("./Picture1.png")

        # 显示
        plt.show()

    def draw_plot(self):
        """绘制散点图"""
        # 数据
        x = [random.uniform(50, 60) for i in range(60)]
        y = [random.uniform(50, 60) for i in range(60)]
        # 创建画布
        plt.figure(figsize=(20, 20), dpi=500)
        # 绘图
        plt.scatter(x, y)
        # 图像保存
        plt.savefig("./Picture2.png")
        # 显示
        plt.show()

    def draw_histogram(self):
        """柱状图"""
        # 数据
        names = ['信条', '哈利波特', '星际穿越', '寻梦环游记', '全球风暴',
                 '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
        y = [73853, 57767, 22354, 15969, 14839,
             8725, 8716, 8318, 7916, 6764, 52222]
        x = range(len(names))
        # 创建画布
        plt.figure(figsize=(20, 8), dpi=500)
        # 绘图
        plt.bar(x, y, width=0.5, color=['b', 'r', 'g', 'y', 'c', 'm'])

        # 添加刻度
        plt.xticks(x, names)
        # 添加网格
        # plt.grid(True, linestyle='-.')
        # 添加标题
        plt.title("电影票房对比", fontsize=20)

        # 图像保存
        plt.savefig("./Picture3.png")

        # 显示
        plt.show()
        
    def draw_hist(self):
        """直方图"""
        # 数据
        x = np.random.normal(1.75, 1, 100000000)

        # 创建画布
        plt.figure(figsize=(20, 8), dpi=500)
        # 绘制图像
        plt.hist(x, 1000)
        # 显示
        plt.show()
