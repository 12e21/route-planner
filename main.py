import map_generate
import planner
import scatter

start=[1,1]
end=[49,49]
obstacles=map_generate.obstacle_generator(600)
route=planner.dijkstra(obstacles,start,end)
scatter.plot_map(obstacles,route)