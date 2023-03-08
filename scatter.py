import matplotlib.pyplot as plt

def plot_map(obstacles, points):
    # 创建一个50×50的网格图形，并设置坐标轴范围和刻度间距
    plt.figure(figsize=(5, 5))
    plt.xlim(0, 49)
    plt.ylim(0, 49)
    plt.xticks(range(0, 50))
    plt.yticks(range(0, 50))

    # 绘制网格线
    plt.grid(True)

    # 将障碍物的坐标分别存储在两个列表中
    x_coords = []
    y_coords = []

    for obstacle in obstacles:
        x_coords.append(obstacle[0])
        y_coords.append(obstacle[1])

    # 使用红色的圆点来表示障碍物
    plt.scatter(x_coords, y_coords, color='red', marker='o')

    # 将要绘制的点的坐标分别存储在两个列表中
    x_points = []
    y_points = []

    for point in points:
        x_points.append(point[0])
        y_points.append(point[1])

    # 使用蓝色的圆点来表示要绘制的点
    plt.scatter(x_points, y_points, color='blue', marker='o')

    # 显示图形
    plt.show()