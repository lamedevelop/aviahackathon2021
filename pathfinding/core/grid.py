# -*- coding: utf-8 -*-
from .node import Node

try:
    import numpy as np

    USE_NUMPY = True
except ImportError:
    USE_NUMPY = False
from pathfinding.core.diagonal_movement import DiagonalMovement


def build_nodes(width, height, matrix=None, inverse=False):
    """
    create nodes according to grid size. If a matrix is given it
    will be used to determine what nodes are walkable.
    :rtype : list
    """
    nodes = []
    use_matrix = (isinstance(matrix, (tuple, list))) or \
                 (USE_NUMPY and isinstance(matrix, np.ndarray) and matrix.size > 0)

    for y in range(height):
        nodes.append([])
        for x in range(width):
            # 1, '1', True will be walkable
            # while others will be obstacles
            # if inverse is False, otherwise
            # it changes
            weight = int(matrix[y][x]) if use_matrix else 1
            walkable = weight <= 0 if inverse else weight >= 1

            nodes[y].append(Node(x=x, y=y, walkable=walkable, weight=weight))
    return nodes


class Grid(object):
    def __init__(self, width=0, height=0, matrix=None, inverse=False):
        """
        a grid represents the map (as 2d-list of nodes).
        """
        self.width = width
        self.height = height
        self.passable_left_right_border = False
        self.passable_up_down_border = False
        self.destination_points = [{'x': 8, 'y': 9, 'info': 'Паркинг',
                                    'text': '',
                                    'warning': ''},
                                   {'x': 3, 'y': 11, 'info': 'Терминал C',
                                    'text': '',
                                    'warning': ''},
                                   {'x': 11, 'y': 16, 'info': 'Аптека 36,6',
                                    'text': 'Акция! Кагоцел с 90% скидкой!',
                                    'warning': ''},
                                   {'x': 13, 'y': 9, 'info': 'Туалет',
                                    'text': '',
                                    'warning': ''},
                                   {'x': 9, 'y': 22, 'info': 'Стойки регистрации 301-316',
                                    'text': 'Стойки самостояткельной регистрации и сдачи багажа.'
                                            'Подготовьте заранее паспорт.',
                                    'warning': 'Возможно образование очереди. Ожидание до 5 минут'},
                                   {'x': 13, 'y': 22, 'info': 'Стойки регистрации 317-332',
                                    'text': 'Приготовьте заранее паспорт.',
                                    'warning': 'Возможно образование очереди. Ожидание до 5 минут'},
                                   {'x': 13, 'y': 22, 'info': 'Стойки регистрации 333-348',
                                    'text': 'Приготовьте заранее паспорт.',
                                    'warning': 'Возможно образование очереди. Ожидание до 5 минут'},
                                   {'x': 13, 'y': 22, 'info': 'Стойки регистрации 349-364',
                                    'text': 'Приготовьте заранее паспорт.',
                                    'warning': 'Возможно образование очереди. Ожидание до 5 минут'},
                                   {'x': 27, 'y': 14, 'info': 'Контроль',
                                    'text': 'Приготовьте посадочный талон для проверки',
                                    'warning': 'Возможно образование очереди. Ожидание до 2 минут'},
                                   {'x': 33, 'y': 11, 'info': 'Duty-Free',
                                    'text': 'В магазине "Ивановский трикотаж" сегодня проходит акция.'
                                            '5 пар трусов по цене 4!!!'},
                                   {'x': 43, 'y': 26, 'info': 'Выходы 101-104',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 49, 'y': 27, 'info': 'Выходы 105-106',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 44, 'y': 36, 'info': 'Выходы 107-108',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 39, 'y': 39, 'info': 'Выходы 109-110',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 44, 'y': 48, 'info': 'Выходы 111-112',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 39, 'y': 51, 'info': 'Выходы 113-114',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 44, 'y': 60, 'info': 'Выходы 115-116',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 45, 'y': 66, 'info': 'Выход 117',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 40, 'y': 69, 'info': 'Выход 118',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 38, 'y': 67, 'info': 'Выходы 119-120',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 38, 'y': 64, 'info': 'Выход 121',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'},
                                   {'x': 42, 'y': 62, 'info': 'Выходы 122-123',
                                    'text': '',
                                    'warning': 'Посадка уже началась!'}]
        self.checkpoints = [{'x': 9, 'y': 22, 'info': 'Стойки регистрации 301-316',
                             'text': 'Стойки самостояткельной регистрации и сдачи багажа. Подготовьте заранее паспорт.',
                             'warning': 'Возможно образование очереди. Ожидание до 5 минут',
                             'time': '300'},
                            {'x': 13, 'y': 22, 'info': 'Стойки регистрации 317-332',
                             'text': 'Приготовьте заранее паспорт.',
                             'warning': 'Возможно образование очереди. Ожидание до 5 минут',
                             'time': '300'},
                            {'x': 13, 'y': 22, 'info': 'Стойки регистрации 333-348',
                             'text': 'Приготовьте заранее паспорт.',
                             'warning': 'Возможно образование очереди. Ожидание до 5 минут',
                             'time': '300'},
                            {'x': 13, 'y': 22, 'info': 'Стойки регистрации 349-364',
                             'text': 'Приготовьте заранее паспорт.',
                             'warning': 'Возможно образование очереди. Ожидание до 5 минут',
                             'time': '300'},
                            {'x': 27, 'y': 14, 'info': 'Контроль',
                             'text': 'Приготовьте посадочный талон для проверки',
                             'warning': 'Возможно образование очереди. Ожидание до 2 минут',
                             'time': '120'},
                            {'x': 33, 'y': 11, 'info': 'Duty-Free',
                             'text': 'В магазине "Ивановский трикотаж" сегодня проходит акция. 5 пар трусов по цене '
                                     '4!!!',
                             'warning': '',
                             'time': '0'},
                            {'x': 41, 'y': 27, 'info': 'Выходы 101-106', 'text': 'Пройдите мимо выходов 101-106',
                             'warning': '',
                             'time': '0'},
                            {'x': 42, 'y': 38, 'info': 'Выходы 107-110', 'text': 'Пройдите мимо выходов 107-110',
                             'warning': '',
                             'time': '0'},
                            {'x': 42, 'y': 51, 'info': 'Выходы 111-114', 'text': 'Пройдите мимо выходов 111-114',
                             'warning': '',
                             'time': '0'},
                            {'x': 41, 'y': 27, 'info': 'Выходы 101-106', 'text': 'Пройдите мимо выходов 101-106',
                             'warning': '',
                             'time': '0'},
                            {'x': 39, 'y': 39, 'info': 'Выход', 'text': 'Пройдите мимо выходов 101-106',
                             'warning': '',
                             'time': '0'}]
        if isinstance(matrix, (tuple, list)) or (
                USE_NUMPY and isinstance(matrix, np.ndarray) and
                matrix.size > 0):
            self.height = len(matrix)
            self.width = self.width = len(matrix[0]) if self.height > 0 else 0
        if self.width > 0 and self.height > 0:
            self.nodes = build_nodes(self.width, self.height, matrix, inverse)
        else:
            self.nodes = [[]]

    def set_passable_left_right_border(self):
        self.passable_left_right_border = True

    def set_passable_up_down_border(self):
        self.passable_up_down_border = True

    def node(self, x, y):
        """
        get node at position
        :param x: x pos
        :param y: y pos
        :return:
        """
        return self.nodes[y][x]

    def inside(self, x, y):
        """
        check, if field position is inside map
        :param x: x pos
        :param y: y pos
        :return:
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def walkable(self, x, y):
        """
        check, if the tile is inside grid and if it is set as walkable
        """
        return self.inside(x, y) and self.nodes[y][x].walkable

    def neighbors(self, node, diagonal_movement=DiagonalMovement.never):
        """
        get all neighbors of one node
        :param node: node
        """
        x = node.x
        y = node.y
        neighbors = []
        s0 = d0 = s1 = d1 = s2 = d2 = s3 = d3 = False

        # ↑
        if y == 0 and self.passable_up_down_border:
            if self.walkable(x, self.height - 1):
                neighbors.append(self.nodes[self.height - 1][x])
                s0 = True
        else:
            if self.walkable(x, y - 1):
                neighbors.append(self.nodes[y - 1][x])
                s0 = True
        # →
        if x == self.width - 1 and self.passable_left_right_border:
            if self.walkable(0, y):
                neighbors.append(self.nodes[y][0])
                s1 = True
        else:
            if self.walkable(x + 1, y):
                neighbors.append(self.nodes[y][x + 1])
                s1 = True
        # ↓
        if y == self.height - 1 and self.passable_up_down_border:
            if self.walkable(x, 0):
                neighbors.append(self.nodes[0][x])
                s2 = True
        else:
            if self.walkable(x, y + 1):
                neighbors.append(self.nodes[y + 1][x])
                s2 = True
        # ←
        if x == 0 and self.passable_left_right_border:
            if self.walkable(self.width - 1, y):
                neighbors.append(self.nodes[y][self.width - 1])
                s3 = True
        else:
            if self.walkable(x - 1, y):
                neighbors.append(self.nodes[y][x - 1])
                s3 = True

        if diagonal_movement == DiagonalMovement.never:
            return neighbors

        if diagonal_movement == DiagonalMovement.only_when_no_obstacle:
            d0 = s3 and s0
            d1 = s0 and s1
            d2 = s1 and s2
            d3 = s2 and s3
        elif diagonal_movement == DiagonalMovement.if_at_most_one_obstacle:
            d0 = s3 or s0
            d1 = s0 or s1
            d2 = s1 or s2
            d3 = s2 or s3
        elif diagonal_movement == DiagonalMovement.always:
            d0 = d1 = d2 = d3 = True

        # ↖
        if d0 and self.walkable(x - 1, y - 1):
            neighbors.append(self.nodes[y - 1][x - 1])

        # ↗
        if d1 and self.walkable(x + 1, y - 1):
            neighbors.append(self.nodes[y - 1][x + 1])

        # ↘
        if d2 and self.walkable(x + 1, y + 1):
            neighbors.append(self.nodes[y + 1][x + 1])

        # ↙
        if d3 and self.walkable(x - 1, y + 1):
            neighbors.append(self.nodes[y + 1][x - 1])

        return neighbors

    def cleanup(self):
        for y_nodes in self.nodes:
            for node in y_nodes:
                node.cleanup()

    def grid_str(self, path=None, start=None, end=None,
                 border=True, start_chr='s', end_chr='e',
                 path_chr='x', empty_chr=' ', block_chr='#',
                 show_weight=False):
        """
        create a printable string from the grid using ASCII characters

        :param path: list of nodes that show the path
        :param start: start node
        :param end: end node
        :param border: create a border around the grid
        :param start_chr: character for the start (default "s")
        :param end_chr: character for the destination (default "e")
        :param path_chr: character to show the path (default "x")
        :param empty_chr: character for empty fields (default " ")
        :param block_chr: character for blocking elements (default "#")
        :param show_weight: instead of empty_chr show the cost of each empty
                            field (shows a + if the value of weight is > 10)
        :return:
        """
        data = ''
        if border:
            data = '+{}+'.format('-' * len(self.nodes[0]))
        for y in range(len(self.nodes)):
            line = ''
            for x in range(len(self.nodes[y])):
                node = self.nodes[y][x]
                if node == start:
                    line += start_chr
                elif node == end:
                    line += end_chr
                elif path and ((node.x, node.y) in path or node in path):
                    line += path_chr
                elif node.walkable:
                    # empty field
                    weight = str(node.weight) if node.weight < 10 else '+'
                    line += weight if show_weight else empty_chr
                else:
                    line += block_chr  # blocked field
            if border:
                line = '|' + line + '|'
            if data:
                data += '\n'
            data += line
        if border:
            data += '\n+{}+'.format('-' * len(self.nodes[0]))
        return data
