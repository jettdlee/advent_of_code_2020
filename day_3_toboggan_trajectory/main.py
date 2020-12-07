from helpers.import_data import ImportData
import numpy as np
import pdb

TREE_MARKER = "#"
FREE_REAL_ESTATE = "."

class TobogganTrajectory:
    def __init__(self, dataset):
        self.dataset = dataset
        self.line_count = len(dataset)

    def calculateTrajectory(self, x_move, y_move):
        x_position = 0
        y_position = 0
        tree_hit_count = 0
        tree_miss_count = 0
        while y_position < self.line_count - 1:
            x_position += x_move
            y_position += y_move
            y_slope = self.dataset[y_position]
            space_value = self._getAborealSpace(y_slope, x_position)
            if self._spaceChecker(space_value):
                tree_hit_count += 1
            else: 
                tree_miss_count += 1

        return [tree_hit_count, tree_miss_count]

    def _spaceChecker(self, space_value):
        return space_value == TREE_MARKER

    def _getAborealSpace(self, slope, x_position):
        aboreal_x_position = x_position % len(slope)
        return slope[aboreal_x_position]


if __name__ == "__main__":

    data_file = ImportData('dataset/day_3.data')
    trajectory = TobogganTrajectory(data_file.dataset) 
    result = trajectory.calculateTrajectory(3, 1)
    print(f"Part one: Hit - {result[0]}, Miss - {result[1]}")

    routes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = { 'hit': [], 'miss': [] }
    for route in routes:
        route_result = trajectory.calculateTrajectory(route[0], route[1])
        result['hit'].append(route_result[0])
        result['miss'].append(route_result[1])
    
    prod_result = np.prod(result['hit'])
    print(f"Part Two:")
    print(f"Moves: {routes}")
    print(f"Results: {result}")
    print(f"Prod Result of Hits: {prod_result}")
