from queue import PriorityQueue


class HeuristicSearch:

    @staticmethod
    def h(cell, goal):
        cell_x = cell[0]
        cell_y = cell[1]
        goal_x = goal[0]
        goal_y = goal[1]

        return abs(cell_x - goal_x) + abs(cell_y - goal_y)

    @staticmethod
    def explore_map(start, goal, lava_map):
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {start: None}

        while not frontier.empty():
            _, current = frontier.get()

            print(current)

            if current == goal:
                break

            for next in lava_map.neighbors(current):
                if next not in came_from:
                    priority = HeuristicSearch.h(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current
