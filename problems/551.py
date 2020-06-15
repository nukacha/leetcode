class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_flag = False
        late_count = 0
        for c in s:
            if c == 'L':
                if late_count == 2:
                    return False
                late_count += 1
            elif c == 'A':
                if absent_flag:
                    return False
                absent_flag = True
                late_count = 0
            else:
                late_count = 0
        return True
