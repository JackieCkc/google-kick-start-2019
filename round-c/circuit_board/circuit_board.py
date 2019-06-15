from collections import Counter, defaultdict
from math import ceil
from bisect import bisect_left, bisect_right


class Solution():
    def max_rentagle(self, histogram):
        stack = list()

        max_area = 0

        index = 0
        while index < len(histogram):
            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            else:
                top_of_stack = stack.pop()

                area = (histogram[top_of_stack] *
                        ((index - stack[-1] - 1)
                         if stack else index))

                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()

            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            max_area = max(max_area, area)

        return max_area

    def solve(self):
        # R, C, K = [int(e) for e in input().split()]
        R, C, K = 300, 300, 0
        rows = []
        for _ in range(R):
            rows.append([0] * 300)

        mem = [[0] * C for _ in range(R)]
        for i, row in enumerate(rows):
            for j in range(C - 1, -1, -1):
                curr = row[j]
                val = 1
                if j + 1 < C and row[j + 1] == curr:
                    val = 1 + mem[i][j + 1]
                mem[i][j] = val

        ans = 0
        for i in range(C):
            bars = [mem[j][i] for j in range(R)]
            ans = max(ans, self.max_rentagle(bars))

        return ans


for t in range(50):
    ans = Solution().solve()
    print('Case #{}: {}'.format(t + 1, ans))
