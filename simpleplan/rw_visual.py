import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个rw实例
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s=12)
# plt.show()

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_point))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds,
    #             edgecolors='none', s=1)
    plt.plot(rw.x_values, rw.y_values)
    # 突出起止点
    plt.scatter(0, 0, c='yellow', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make a anther walk? (y/n):\n")
    if keep_running == 'n':
        break
