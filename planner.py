# 定义一个函数，用于求最短路径
def dijkstra(obstacles, start, end):
  # 定义一个字典，用于存储每个点到起点的距离
  distances = {}
  # 定义一个集合，用于存储已经访问过的点
  visited = set()
  # 定义一个字典，用于存储每个点的前驱点
  previous = {}
  # 定义一个常量，表示无穷大
  INF = float("inf")
  # 定义一个函数，用于判断一个点是否在地图范围内
  def in_map(x, y):
    return 0 <= x < 50 and 0 <= y < 50
  # 定义一个函数，用于判断一个点是否是障碍点
  def is_obstacle(x, y):
    return [x, y] in obstacles
  # 定义一个函数，用于获取一个点的邻居点
  def get_neighbors(x, y):
    # 定义一个列表，用于存储邻居点
    neighbors = []
    # 定义一个列表，用于存储四个方向的偏移量
    offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 遍历四个方向
    for dx, dy in offsets:
      # 计算邻居点的坐标
      nx = x + dx
      ny = y + dy
      # 如果邻居点在地图范围内，且不是障碍点，就加入邻居点列表
      if in_map(nx, ny) and not is_obstacle(nx, ny):
        neighbors.append([nx, ny])
    # 返回邻居点列表
    return neighbors
  # 初始化每个点到起点的距离为无穷大，除了起点自身为0
  for x in range(50):
    for y in range(50):
      distances[(x, y)] = INF
  distances[(start[0], start[1])] = 0
  # 定义一个变量，用于存储当前访问的点，初始为起点
  current = start
  # 定义一个循环，直到当前访问的点为终点或者没有可访问的点
  while current != end and current != None:
    # 将当前访问的点加入已访问集合
    visited.add((current[0], current[1]))
    # 获取当前访问的点的邻居点
    neighbors = get_neighbors(current[0], current[1])
    # 遍历邻居点
    for neighbor in neighbors:
      # 如果邻居点没有被访问过
      if (neighbor[0], neighbor[1]) not in visited:
        # 计算邻居点到起点的距离，为当前访问的点到起点的距离加1
        distance = distances[(current[0], current[1])] + 1
        # 如果邻居点到起点的距离小于之前的距离，就更新距离和前驱点
        if distance < distances[(neighbor[0], neighbor[1])]:
          distances[(neighbor[0], neighbor[1])] = distance
          previous[(neighbor[0], neighbor[1])] = current
    # 定义一个变量，用于存储下一个访问的点，初始为None
    next = None
    # 定义一个变量，用于存储下一个访问的点到起点的最小距离，初始为无穷大
    min_distance = INF
    # 遍历每个点
    for x in range(50):
      for y in range(50):
        # 如果该点没有被访问过，且到起点的距离小于最小距离，就更新下一个访问的点和最小距离
        if (x, y) not in visited and distances[(x, y)] < min_distance:
          next = [x, y]
          min_distance = distances[(x, y)]
    # 将下一个访问的点赋值给当前访问的点
    current = next
  # 定义一个列表，用于存储最短路径
  path = []
  # 如果当前访问的点为终点，说明有最短路径
  if current == end:
    # 从终点开始，沿着前驱点回溯，直到起点，将每个点加入路径列表
    while current != start:
      path.append(current)
      current = previous[(current[0], current[1])]
    # 将起点加入路径列表
    path.append(start)
    # 反转路径列表，使其从起点到终点
    path.reverse()
  # 如果当前访问的点为None，说明没有最短路径
  else:
    # 将路径列表赋值为None
    path = None
  # 返回路径列表
  return path


'''
这是我为你写的一个函数，用于求最短路径，使用狄克斯特拉算法，入口参数有3个，第一个参数是一个包含若干个长度为2的数组的二维数组，用于表示50乘50的地图上的障碍点，第二，三个参数分别是长度为2的数组，一个表示起点，一个表示终点。函数的返回值为一个包含最短路径的点的数组，没有最短路径就返回none。特别注意，以上函数假设运行在50乘50的地图上。
'''

if __name__ =='__main__':
  obstacles=[[4,1],[4,2],[4,3],[4,4],[4,5]]
  start=[5,3]
  end=[3,3]
  shortest_route=dijkstra(obstacles,start,end)
  print(shortest_route)