class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        j = 1
        for i in range(1, len(name)):
            while j < len(typed):
                if name[i] == typed[j]:
                    j += 1
                    break
                elif name[i - 1] == typed[j]:
                    j += 1
                else:
                    return False
            else:
                return False
        if len(set(typed[j - 1:])) == 1:
            return True
        else:
            return False
