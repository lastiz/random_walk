from random import choice
import matplotlib.pyplot as plt


class RandomWalk(object):
    """Генерация случайных блужданий"""

    def __init__(self, num_points=5000):
        """инициализируем атрибуты блуждания"""
        # 5000 шагов
        self.num_points = num_points

        # точки координат, блуждание начинается с 0, 0
        self.x_values = [0]
        self.y_values = [0]

    def enter_walk(self):
        # добавляем точки пока список х точек меньше поинтов
        while len(self.x_values) < self.num_points:
            next_x, next_y = self.x_y_steps()
            if next_x == 0 and next_y == 0:  # продолжаем если обе коор. == 0
                continue
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def x_y_steps(self):
        """Определяет шаг и направление"""
        # выбор случайного направления и шагов
        directions = [1, -1]
        steps = [0, 1, 2, 3, 4]  # 0 для вертикального или горизонтального перемещения
        x_direction = choice(directions)
        y_direction = choice(directions)
        x_distance = choice(steps)
        y_distance = choice(steps)
        x_step = x_distance * x_direction
        y_step = y_distance * y_direction
        next_x = self.x_values[-1] + x_step
        next_y = self.y_values[-1] + y_step
        # следущие точки и добавляем их в списки
        return next_x, next_y


if __name__ == '__main__':
    rw = RandomWalk(50000)
    rw.enter_walk()
    plt.figure(dpi=128)
    plt.scatter(rw.x_values, rw.y_values, s=1, edgecolors='none', c=list(range(rw.num_points)), cmap=plt.cm.Blues)
    plt.scatter(0, 0, s=30, edgecolors='none', c='black')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)
    plt.title('Random Walk')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.savefig('random_walk.png')