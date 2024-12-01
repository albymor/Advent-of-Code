import re
from copy import copy
from tqdm import tqdm


with open('input.txt', 'r') as f:
    data = f.read()

test = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


class Node:
    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y):
        self.sensor_position = (sensor_x, sensor_y)
        self.beacon_position = (beacon_x, beacon_y)

        self.ll = set()

        self.manhattan_distance = abs(
            sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        self.occupancy_grid = []

    def get_occupancy_grid(self, y, max_):
        if abs(self.sensor_position[1] - y) <= self.manhattan_distance:
            aa = self.manhattan_distance - abs(self.sensor_position[1] - y)
            self.occupancy_grid.append(
                (self.sensor_position[0] - aa, self.sensor_position[0] + aa + 1))
        else:
            self.occupancy_grid.append((0, 0))

    def compute_occupancy_grid(self, max_):
        for y in range(0, max_+1):
            self.get_occupancy_grid(y, max_)


def get_part_one(data, y):
    lines = data.split('\n')

    nodes = []

    for line in lines:
        aa = re.findall(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)

        nodes.append(Node(*list(map(int, aa[0]))))

    for node in nodes:
        if node.sensor_position == (8, 7):
            cacca = 0
        if abs(node.sensor_position[1] - y) <= node.manhattan_distance:
            aa = node.manhattan_distance - abs(node.sensor_position[1] - y)
            for i in range(node.sensor_position[0] - aa, node.sensor_position[0] + aa + 1):
                if (i, y) != node.beacon_position:
                    node.ll.add((i, y))

    total = set()
    for node in nodes:
        total = total.union(node.ll)

    return len(total)


assert get_part_one(test, 10) == 26
print(f'Part 1: {get_part_one(data, 2000000)}')

# part 2


def merge_intervals(sorted_intervals):
    interval_index = 0
    # print(sorted_intervals)
    start = sorted_intervals[0][0]
    end = sorted_intervals[0][1]
    merge_intervals = []
    for i in sorted_intervals[1:]:
        if i[0] <= end:
            end = max(end, i[1])
        else:
            merge_intervals.append((start, end))
            start = i[0]
            end = i[1]

    merge_intervals.append((start, end))
    return merge_intervals


def get_part_two(data, max_):
    lines = data.split('\n')

    nodes = []

    for line in lines:
        aa = re.findall(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)

        nodes.append(Node(*list(map(int, aa[0]))))

    for node in tqdm(nodes):
        node.compute_occupancy_grid(max_)

    for i in tqdm(range(0, max_+1)):
        ranges = []
        for node in nodes:
            ranges.append(list(node.occupancy_grid[i]))
        ranges.sort()
        merged_ranges = merge_intervals(ranges)
        if len(merged_ranges) > 1:
            coord = (merged_ranges[0][1], i)
            break

    freq = (4000000*coord[0]) + coord[1]

    return freq


assert get_part_two(test, 20) == 56000011
print(f'Part 2: {get_part_two(data, 4000000)}')
