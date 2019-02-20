from EX02.a_star import AStar
from EX02.heuristic_search import HeuristicSearch
from EX02.lava_map import LavaMap

if __name__ == '__main__':
    with open("caves/cave900x900") as f:
        map_data = [l.strip() for l in f.readlines() if len(l) > 1]

    lava_map = LavaMap(map_data)
    start = (2, 2, 's')
    goal = (895, 898, 'D')
    print(HeuristicSearch.explore_map(start, goal, lava_map))
    # print(AStar.explore_map(start, goal, lava_map))
