import matplotlib.pyplot as plt
import random
from matplotlib.pylab import mpl
import matplotlib.ticker as ticker


mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置表格标题中文字体


class Drawing(object):
    """绘制图像类"""

    def draw_mulinchart(self):
        """同一坐标系绘制多个图"""
        # 数据
        x = range(60)
        y1 = [random.uniform(26, 38) for i in x]
        y2 = [random.uniform(10, 20) for i in x]
        # 创建画布
        # figsize=(20, 8)定义长宽比，dpi定义图片分辨率
        plt.figure(figsize=(20, 8), dpi=500)
        # 绘图b
        plt.plot(x, y1, color="r", linestyle="--", label="A")  # "-": 实线  "--": 虚线
        plt.plot(x, y2, color="b", linestyle="--", label="B")

        # 构造x，y轴标签
        x_ticks_label = ["7:{}".format("%.2d" % (i)) for i in x]
        y_ticks = range(40)
        plt.xticks(x[::5], x_ticks_label[::5])
        plt.yticks(y_ticks[::5])
        # 添加描述信息
        plt.xlabel("Time")
        plt.ylabel("Temporature")
        plt.title("7~8:00 am A&B Cities Temporature Chart")
        # 绘制图例
        plt.legend(loc=4)  # loc = "best", 0 , 1, 2, 3, 4, ...
        # 图像保存
        plt.savefig("./Picture4.png")

        # 显示
        plt.show()

    def draw_multichart(self):
        """绘制多个图"""
        # 数据
        x = range(60)
        y1 = [random.uniform(26, 38) for i in x]
        y2 = [random.uniform(10, 20) for i in x]
        # 创建画布
        # nrows, ncols定义图按怎样的行列排列，figsize=(20, 8)定义长宽比，dpi定义图片分辨率
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=500)
        # 绘图b
        axes[0].plot(x, y1, color="r", linestyle="--",
                     label="A")  # "-": 实线  "--": 虚线
        axes[1].plot(x, y2, color="b", linestyle="--", label="B")

        # 构造x，y轴标签
        x_ticks_label = ["7:{}".format("%.2d" % (i)) for i in x]
        y_ticks = range(40)
        # # 第一幅图
        axes[0].set_xticks(x[::5])
        axes[0].set_yticks(y_ticks[::5])
        axes[0].set_xticklabels(x_ticks_label[::5])
        # # 第二幅图
        axes[1].set_xticks(x[::5])
        axes[1].set_yticks(y_ticks[::5])
        axes[1].set_xticklabels(x_ticks_label[::5])
        # 添加网格
        # axes[0].grid(True, linestyle='--')
        # axes[1].grid(True, linestyle='--')
        # 添加描述信息
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Temporature")
        axes[0].set_title("7~8:00 am A City Temporature Chart")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Temporature")
        axes[1].set_title("7~8:00 am B City Temporature Chart")
        # 绘制图例
        axes[0].legend(loc=4)  # loc = "best", 0 , 1, 2, 3, 4, ...
        axes[1].legend(loc=4)
        # 标记左图位置
        ax_top = axes[0].twiny()  # 建立顶部坐标轴的对象
        axes[0].axvline(30, linestyle='--', color='c')  # 青色虚线
        # # 设置顶部坐标轴
        xticks = axes[0].get_xticks()
        xlim = axes[0].get_xlim()
        ax_top.set_xlim(xlim)
        # # 设置标记信息
        mark_tick = [30]
        mark_label = ["key"]  # 这两行分别是要显示坐标的位置以及置换的标签
        ax_top.set_xticks(mark_tick)
        ax_top.set_xticklabels(mark_label)
        #     # 标记右图位置
        #     ax_top = axes[1].twiny()  # 建立顶部坐标轴的对象
        #     xticks = axes[1].get_xticks()
        #     xlim = axes[1].get_xlim()
        #     ax_top.set_xlim(xlim)
        #     # # 设置标记信息
        #     mark_tick = [0]
        #     mark_label = [" "]  # 这两行分别是要显示坐标的位置以及置换的标签
        #     ax_top.set_xticks(mark_tick)
        #     ax_top.set_xticklabels(mark_label)
        # 图像保存
        plt.savefig("./Picture5.png")

        # 显示
        plt.show()

    def draw_sharex(self):
        """同一坐标系共用x轴绘图"""
        # 数据
        x = range(60)
        y1 = [random.uniform(26, 38) for i in x]
        y2 = [random.uniform(10, 20) for i in x]
        # 创建画布
        fig, axes = plt.subplots(figsize=(20, 8), dpi=500)
        # 绘图b
        axes.plot(x, y1, color="r", linestyle="--", label="A")  # "-": 实线  "--": 虚线
        plt.legend(loc=2)
        axes2 = axes.twinx()  # 创建第二个Y轴
        axes2.plot(x, y2, color="b", linestyle="--", label="B")
        plt.legend(loc=0)
        # 构造x，y轴标签
        x_ticks_label = ["7:{}".format("%.2d" % (i)) for i in x]
        y_ticks = range(40)
        plt.xticks(x[::5], x_ticks_label[::5])
        plt.yticks(y_ticks[::5])
        # 添加描述信息
        plt.xlabel("Time")
        plt.title("7~8:00 am A&B Cities Temporature Chart")
        axes.set_ylabel("Temporature")
        axes2.set_ylabel("Temporature")
        # 绘制图例
        #     plt.legend(loc=4)  # loc = "best", 0 , 1, 2, 3, 4, ...
        # 图像保存
        plt.savefig("./Picture6.png")

        # 显示
        plt.show()

    def draw_mul_sharex(self):
        """绘制多个图"""
        # 数据
        x = range(60)
        y1 = [random.uniform(26, 38) for i in x]
        y2 = [random.uniform(10, 20) for i in x]
        # 创建画布
        # nrows, ncols定义图按怎样的行列排列，figsize=(20, 8)定义长宽比，dpi定义图片分辨率
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 8), dpi=500, sharex=True)
        # 绘图b
        axes[0].plot(x, y1, color="r", linestyle="--",
                     label="A")  # "-": 实线  "--": 虚线
        axes[1].plot(x, y2, color="b", linestyle="--", label="B")
        fig.suptitle("7~8:00 am A&B City Temporature Chart")

        # 构造x，y轴标签
        x_ticks_label = ["7:{}".format("%.2d" % (i)) for i in x]
        y_ticks = range(40)
        # # 第一幅图
        axes[0].set_yticks(y_ticks[::5])
        # # 第二幅图
        axes[1].set_xticks(x[::5])
        axes[1].set_yticks(y_ticks[::5])
        axes[1].set_xticklabels(x_ticks_label[::5])
        # 添加网格
        # axes[0].grid(True, linestyle='--')
        # axes[1].grid(True, linestyle='--')
        # 添加描述信息
        #     axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Temporature")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Temporature")
        #     axes[1].set_title("7~8:00 am B City Temporature Chart")
        # 绘制图例
        axes[0].legend(loc=4)  # loc = "best", 0 , 1, 2, 3, 4, ...
        axes[1].legend(loc=4)

        # 标记左图位置
        ax_top = axes[0].twiny()  # 建立顶部坐标轴的对象
        axes[0].axvline(30, linestyle='--', color='c')  # 青色虚线
        # # 设置顶部坐标轴
        xticks = axes[0].get_xticks()
        xlim = axes[0].get_xlim()
        ax_top.set_xlim(xlim)
        # # 设置标记信息
        mark_tick = [30]
        mark_label = ["key"]  # 这两行分别是要显示坐标的位置以及置换的标签
        ax_top.set_xticks(mark_tick)
        ax_top.set_xticklabels(mark_label)
        #     # 标记右图位置
        #     ax_top = axes[1].twiny()  # 建立顶部坐标轴的对象
        #     xticks = axes[1].get_xticks()
        #     xlim = axes[1].get_xlim()
        #     ax_top.set_xlim(xlim)
        #     # # 设置标记信息
        #     mark_tick = [0]
        #     mark_label = [" "]  # 这两行分别是要显示坐标的位置以及置换的标签
        #     ax_top.set_xticks(mark_tick)
        #     ax_top.set_xticklabels(mark_label)

        # 图像保存
        plt.savefig("./Picture7.png")

        # 显示
        plt.show()