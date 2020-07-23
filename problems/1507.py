MONTH_LIST = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_DICT = {k: i for i, k in enumerate(MONTH_LIST, 1)}


class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        return f'{year}-{MONTH_DICT[month]:02}-{int(day[:-2]):02}'
