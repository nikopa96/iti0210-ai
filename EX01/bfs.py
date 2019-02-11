from queue import Queue


class BFS:

    @staticmethod
    def explore_map(start, lava_map):
        frontier = Queue()
        frontier.put(start)
        came_from = [start]

        while not frontier.empty():
            current = frontier.get()
            for next in lava_map.neighbors(current):
                if next not in came_from and next.get_value() != '*':
                    next.set_came_from(current)
                    came_from.append(next)
                    frontier.put(next)

                    if next.get_value() == 'D':
                        lava_map.set_diamond(next)

    @staticmethod
    def get_path(start, lava_map):
        BFS.explore_map(start, lava_map)

        current = lava_map.get_diamond()
        path = []
        while current != start:
            path.append(current)
            current = current.get_came_from()
        path.append(start)
        path.reverse()

        return path

    @staticmethod
    def draw_path(path, lava_map):
        lava_map_list = lava_map.get_lava_map_list()

        lava_map_chars = []

        for row in lava_map_list:
            sub_list = list(row)
            lava_map_chars.append(sub_list)

        for cell in path:
            if lava_map_chars[cell.get_y()][cell.get_x()] != 'D' and lava_map_chars[cell.get_y()][cell.get_x()] != 's' \
                    and lava_map_chars[cell.get_y()][cell.get_x()] != '*':
                lava_map_chars[cell.get_y()][cell.get_x()] = '.'

        for row in lava_map_chars:
            new_row = "".join(row)
            print(new_row)
