from random import randint

n = int(input())
bad_version = randint(1, n)
num_called = 0

def isBadVersion(version):
    global num_called
    num_called += 1
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        vmax = n
        vmin = 1
        while True:
            vmid = (vmax - vmin) // 2 + vmin
            if isBadVersion(vmid):
                vmax = vmid
            else:
                vmin = vmid + 1
            if vmax == vmin:
                return vmax


if __name__ == "__main__":
    solution = Solution()
    r = solution.firstBadVersion(n)
    print(r, num_called)
