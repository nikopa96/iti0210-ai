class LavaMap:

    def __init__(self, lava_map_list):
        self.lava_map_list = lava_map_list

    def neighbors(self, cell):
        neighboring_cells = []
        lava_map_width = len(self.lava_map_list[cell[1]])
        lava_map_height = len(self.lava_map_list)

        x = cell[0]
        y = cell[1]

        if x + 1 < lava_map_width:
            if self.lava_map_list[y][x + 1] != '*':
                neighboring_cells.append((x + 1, y, self.lava_map_list[y][x + 1]))

        if x - 1 >= 0:
            if self.lava_map_list[y][x - 1] != '*':
                neighboring_cells.append((x - 1, y, self.lava_map_list[y][x - 1]))

        if y + 1 < lava_map_height:
            if self.lava_map_list[y + 1][x] != '*':
                neighboring_cells.append((x, y + 1, self.lava_map_list[y + 1][x]))

        if y - 1 >= 0:
            if self.lava_map_list[y - 1][x] != '*':
                neighboring_cells.append((x, y - 1, self.lava_map_list[y - 1][x]))

        return neighboring_cells
