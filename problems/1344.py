class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30 * hour + minutes / 2
        minutes_angle = minutes * 6
        angle = abs(hour_angle - minutes_angle) % 360
        return min(angle, 360 - angle)
