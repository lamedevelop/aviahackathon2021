from pathfinding.floors import matrixB
from pathfinding.core.grid import Grid
from pathfinding.finder.bi_a_star import BiAStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


TIME_LIMIT = 10


class Navigator:

    grid: Grid
    start: list
    end: list

    finder = BiAStarFinder

    def __init__(self):
        self.grid = Grid(matrix=matrixB, inverse=True)

    def get_point(self, point_id=0):
        return self.grid.node(
            self.grid.destination_points[point_id]['x'],
            self.grid.destination_points[point_id]['y']
        )

    def getPointByName(self, name: str):
        for point in self.grid.destination_points:
            if point['info'] == name \
                    or point['info'] == name.lower() \
                    or point['info'] == name.upper():
                return point

    def getPointIdByName(self, name: str):
        my_point = self.getPointByName(name)
        i = 0

        for point in self.grid.destination_points:
            if point['info'] == my_point['info']
                return i
            else:
                i += 1

        return -1

    def build_path(self, start_id=0, end_id=15):
        path_info = []
        total_time = 0

        start = self.get_point(start_id)
        end = self.get_point(end_id)

        for point in self.grid.destination_points:
            if start.x == point['x'] and start.y == point['y']:
                print('Start at: {}'.format(point['info']))
            if end.x == point['x'] and end.y == point['y']:
                print('End at: {}'.format(point['info']))

        self.grid.cleanup()
        route = self.finder(
            diagonal_movement=DiagonalMovement.always,
            time_limit=TIME_LIMIT
        )
        weighted = False

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
        total_time += len(path) * 5
        print('Общее время ~{} минут.'.format(total_time // 60))
        print(self.grid.grid_str(
            path=path,
            start=start,
            end=end,
            show_weight=weighted
        ))

        return path, path_info


if __name__ == '__main__':
    Navigator().build_path()
