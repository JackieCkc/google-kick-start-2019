from collections import Counter, defaultdict
from math import ceil
from bisect import bisect_left, bisect_right
from random import randint


class Solution():
    def compute_logs(self, n):
        logs = [0, 0]
        for i in range(2, n + 1):
            logs.append(logs[i // 2] + 1)
        return logs

    def build(self, arr, l):
        min_table = [[0] * 10 for _ in range(l)]
        max_table = [[0] * 10 for _ in range(l)]
        for i in range(l):
            max_table[i][0] = arr[i]
            min_table[i][0] = arr[i]

        for j in range(1, 11):
            for i in range(l - (1 << j) + 1):
                max_table[i][j] = max(max_table[i][j - 1], max_table[i + (1 << (j - 1))][j - 1])
                min_table[i][j] = min(min_table[i][j - 1], min_table[i + (1 << (j - 1))][j - 1])
        return max_table, min_table

    def get_min(self, l, r, table, logs):
        j = logs[r - l + 1]
        return min(table[l][j], table[r - 2 ** j + 1][j])

    def get_max(self, l, r, table, logs):
        j = logs[r - l + 1]
        return max(table[l][j], table[r - 2 ** j + 1][j])

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

    def search(self, max_table, min_table, logs, j, k, n, c):
        s, e = j, n
        # print('search', j)
        while s < e - 1:
            m = (s + e) // 2
            max_val = self.get_max(j, m, max_table, logs)
            min_val = self.get_min(j, m, min_table, logs)
            # print('max', j, m, max_val)
            # print('min', min_val)
            if abs(max_val - c) <= k and abs(min_val - c) <= k:
                s = m
            else:
                e = m - 1
        # print(s)
        # print('')
        return s - j + 1

    def solve(self):
        R, C, K = [int(e) for e in input().split()]
        rows = []
        for _ in range(R):
            rows.append([int(e) for e in input().split()])

        mem = [[0] * C for _ in range(R)]
        logs = self.compute_logs(C)
        for i, row in enumerate(rows):
            max_table, min_table = self.build(row, C)
            print(max_table);
            for j in range(C):
                mem[i][j] = self.search(max_table, min_table, logs, j, K, C, row[j])

        # print(mem)
        ans = 0
        for i in range(C):
            bars = [mem[j][i] for j in range(R)]
            ans = max(ans, self.max_rentagle(bars))

        return ans


for t in range(int(input())):
    ans = Solution().solve()
    print('Case #{}: {}'.format(t + 1, ans))
