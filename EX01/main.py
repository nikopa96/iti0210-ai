from EX01.bfs import BFS
from EX01.cell import Cell
from EX01.lava_map import LavaMap

if __name__ == '__main__':
    bfs = BFS()

    lava_map_list1 = [
        "      **               **      ",
        "     ***     D        ***      ",
        "     ***                       ",
        "                      *****    ",
        "           ****      ********  ",
        "           ***          *******",
        " **                      ******",
        "*****             ****     *** ",
        "*****              **          ",
        "***                            ",
        "              **         ******",
        "**            ***       *******",
        "***                      ***** ",
        "                               ",
        "                s              ",
    ]
    y1 = 14
    x1 = 16

    lava_map_1 = LavaMap(lava_map_list1)
    start_1 = Cell(x1, y1, lava_map_list1[y1][x1])
    print('\n' + '------------------   KAART 1   ------------------' + '\n')
    bfs.draw_path(bfs.get_path(start_1, lava_map_1), lava_map_1)

    lava_map_list2 = [
        "     **********************    ",
        "   *******   D    **********   ",
        "   *******                     ",
        " ****************    **********",
        "***********          ********  ",
        "            *******************",
        " ********    ******************",
        "********                   ****",
        "*****       ************       ",
        "***               *********    ",
        "*      ******      ************",
        "*****************       *******",
        "***      ****            ***** ",
        "                               ",
        "                s              ",
    ]
    y2 = 14
    x2 = 16

    lava_map_2 = LavaMap(lava_map_list2)
    start_2 = Cell(x2, y2, lava_map_list2[y2][x2])
    print('\n' + '------------------   KAART 2   ------------------' + '\n')
    bfs.draw_path(bfs.get_path(start_2, lava_map_2), lava_map_2)
