from EX01.cell import Cell


class LavaMap:

    def __init__(self, lava_map_list):
        self.lava_map_list = lava_map_list
        self.diamond = None

    def set_diamond(self, cell):
        self.diamond = cell

    def get_diamond(self):
        return self.diamond

    def get_lava_map_list(self):
        return self.lava_map_list

    def neighbors(self, cell):
        neighboring_cells = []
        lava_map_width = len(self.lava_map_list[cell.get_y()])
        lava_map_height = len(self.lava_map_list)

        if cell.get_x() + 1 < lava_map_width:
            new_cell = Cell(cell.get_x() + 1,
                            cell.get_y(),
                            self.lava_map_list[cell.get_y()][cell.get_x() + 1])
            neighboring_cells.append(new_cell)

        if cell.get_x() - 1 >= 0:
            new_cell = Cell(cell.get_x() - 1,
                            cell.get_y(),
                            self.lava_map_list[cell.get_y()][cell.get_x() - 1])
            neighboring_cells.append(new_cell)

        if cell.get_y() + 1 < lava_map_height:
            new_cell = Cell(cell.get_x(),
                            cell.get_y() + 1,
                            self.lava_map_list[cell.get_y() + 1][cell.get_x()])
            neighboring_cells.append(new_cell)

        if cell.get_y() - 1 >= 0:
            new_cell = Cell(cell.get_x(),
                            cell.get_y() - 1,
                            self.lava_map_list[cell.get_y() - 1][cell.get_x()])
            neighboring_cells.append(new_cell)

        return neighboring_cells
