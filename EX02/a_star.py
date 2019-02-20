from queue import PriorityQueue


class AStar:

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
        cost_so_far = {start: 0}

        while not frontier.empty():
            _, current = frontier.get()

            print(current)

            if current == goal:
                break

            for next in lava_map.neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + AStar.h(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current
