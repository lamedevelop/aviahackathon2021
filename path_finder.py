# -*- coding: utf-8 -*-
import os
import json
import pytest
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.best_first import BestFirst
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.bi_a_star import BiAStarFinder
from pathfinding.finder.ida_star import IDAStarFinder
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.finder.finder import ExecutionRunsException
from pathfinding.finder.finder import ExecutionTimeException
from pathfinding.finder.msp import MinimumSpanningTree
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement


BASE_PATH = os.path.abspath(os.path.dirname(__file__))

scenarios = os.path.join(BASE_PATH, 'path_test_scenarios.json')
data = json.load(open(scenarios, 'r'))
finder = BiAStarFinder
TIME_LIMIT = 10

class Navigator:

    grid: Grid
    start: list
    end: list

    def grid_from_scenario(self, scenario):
        inverse = scenario['inverse'] if 'inverse' in scenario else True
        self.grid = Grid(matrix=scenario['matrix'], inverse=inverse)

    def get_point(self, point_id=0):
        return self.grid.node(
            self.grid.destination_points[point_id]['x'],
            self.grid.destination_points[point_id]['y']
        )

    def build_path(self):
        path_info = []
        total_time = 0
        # test diagonal movement
        for scenario in data:
            self.grid_from_scenario(scenario)
            start = self.get_point(0)
            end = self.get_point(15)

            for point in self.grid.destination_points:
                if start.x == point['x'] and start.y == point['y']:
                    print('Start at: {}'.format(point['info']))
                if end.x == point['x'] and end.y == point['y']:
                    print('End at: {}'.format(point['info']))

            self.grid.cleanup()
            route = finder(diagonal_movement=DiagonalMovement.always,
                          time_limit=TIME_LIMIT)
            weighted = False
            if 'weighted' in scenario:
                weighted = scenario['weighted']

            path, runs = route.find_path(start, end, self.grid)

            for coords in path:
                for checkpoint in self.grid.checkpoints:
                    if checkpoint['x'] == coords[0] and checkpoint['y'] == coords[1]:
                        path_info.append(checkpoint)

            for i in path_info:
                print(i['info'], i['text'])
                total_time += int(i['time'])
                print(i['warning'])
                print()
            total_time += len(path)*5
            print('Общее время ~{} минут.'.format(total_time//60))
            print(self.grid.grid_str(
                path=path,
                start=start,
                end=end,
                show_weight=weighted
            ))



if __name__ == '__main__':
    # test_path()
    test_path_diagonal()
