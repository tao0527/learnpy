from random import choice


class RandomWalk:
    """一个生产随机漫步的类"""

    def __init__(self, num_point=5000):
        """初始化随机漫步的属性"""
        self.num_point = num_point

        """所有随机漫步都始于(0,0)"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算包含随机的所有点"""
        while len(self.x_values) < self.num_point:

            # 决定前进方向及距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #不可原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
