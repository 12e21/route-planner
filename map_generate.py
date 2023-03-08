import random
import matplotlib.pyplot as plt

def obstacle_generator(n):
    # n 是障碍物的数量，必须小于或等于 250
    # 返回一个列表，每个子列表有两个元素表示一个障碍物的坐标

    # 检查 n 是否有效
    if n < 0 or n > 600: #此处进行手动修改
        print("障碍物数量无效")
        return None

    # 创建一个空列表来存储障碍物
    obstacles = []

    # 创建一个集合来存储已占用的位置
    occupied = set()

    # 循环直到生成 n 个障碍物
    while len(obstacles) < n:

        # 在 [0,49] 的范围内生成一个随机位置 (x,y)
        x = random.randint(0, 49)
        y = random.randint(0, 49)

        # 检查位置是否已经被占用
        if (x, y) in occupied:
            continue  # 跳过这个位置，再试一次

        # 把位置加入到已占用的集合中
        occupied.add((x, y))

        # 添加一些随机性，避免分布过于密集或过于分散
        # 对于每个相邻的位置 (x+dx,y+dy)，其中 dx 和 dy 在 [-1,1] 中，
        # 抛一枚硬币并决定是否占用它或不占用它
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # 跳过原始位置
                    continue

                # 检查相邻位置是否有效且未被占用
                if 0 <= x + dx <= 49 and 0 <= y + dy <= 49 and (x + dx, y + dy) not in occupied:

                    # 抛一枚硬币，概率 p 是正面朝上
                    p = random.random()

                    # 如果正面朝上，占用相邻位置并把它加入到障碍物列表中
                    if p < 0.5:
                        occupied.add((x + dx, y + dy))
                        obstacles.append([x + dx, y + dy])

        # 把原始位置加入到障碍物列表中
        obstacles.append([x, y])

    return obstacles

'''
废弃代码
# 使用matplotlib将地图可视化

def plot_map(obstacles):
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

    # 显示图形
    plt.show()
'''


'''
# 使用一些例子测试函数

plot_map(obstacle_generator(10))
plot_map(obstacle_generator(250))
'''
