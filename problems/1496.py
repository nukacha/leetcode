class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coord = (0, 0)
        coord_set = {coord}
        for d in path:
            x, y = coord
            if d == 'N':
                coord = x, y + 1
            elif d == 'S':
                coord = x, y - 1
            elif d == 'E':
                coord = x + 1, y
            else:
                coord = x - 1, y
            if coord in coord_set:
                return True
            else:
                coord_set.add(coord)
        return False
