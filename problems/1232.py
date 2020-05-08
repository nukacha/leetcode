from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        delta_x = abs(x0 - x1)
        delta_y = abs(y0 - y1)
        for coord in coordinates[2:]:
            x, y = coord
            if abs(x - x0) * delta_y != abs(y - y0) * delta_x:
                return False
        return True
