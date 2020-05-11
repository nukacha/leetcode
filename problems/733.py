from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        org_color = image[sr][sc]
        if org_color == newColor:
            return image
        image[sr][sc] = newColor
        coords = [
            (sr - 1, sc),
            (sr, sc - 1),
            (sr + 1, sc),
            (sr, sc + 1)
        ]
        for coord in coords:
            x, y = coord
            if -1 < x < len(image) and -1 < y < len(image[0]):
                if image[x][y] == org_color:
                    self.floodFill(image, x, y, newColor)
        return image
