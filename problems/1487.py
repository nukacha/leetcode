import re
from collections import defaultdict
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        pat = re.compile(r'^(.*)\((\d+)\)?$')
        name_n = defaultdict(lambda: [0, set()])
        result = []
        folder_set = set()
        for name in names:
            rname = str()
            if name in folder_set:
                if name in name_n:
                    while name_n[name][0] in name_n[name][1]:
                        name_n[name][0] += 1
                    rname = f'{name}({name_n[name][0]})'
                    name_n[name][0] += 1
                    name_n[rname][0] += 1
                elif (name := re.sub(pat, r'\1', name)) in name_n:
                    while name_n[name][0] in name_n[name][1]:
                        name_n[name][0] += 1
                    rname = f'{name}({name_n[name][0]})'
                    name_n[name][0] += 1
                    name_n[rname][0] += 1
            else:
                name_n[name][0] += 1
                rname = name
                if match := re.fullmatch(pat, name):
                    name_n[match.group(1)][1].add(int(match.group(2)))
            folder_set.add(rname)
            result.append(rname)
        return result
