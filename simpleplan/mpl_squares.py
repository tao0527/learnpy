import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
x_values = list(range(1, 1001))
# squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]
y_values = [x**2 for x in x_values]
# plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=16)
# plt.ylabel("Square of Value", fontsize=16)

# 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)

# 设置标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Number", fontsize=16)

# 设计刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=12)

plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
