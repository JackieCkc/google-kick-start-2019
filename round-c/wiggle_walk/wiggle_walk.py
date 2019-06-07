from collections import Counter, defaultdict
from math import ceil
from bisect import bisect_left, bisect_right


class Solution():
    def solve(self):
        N, R, C, r, c = [int(e) for e in input().split()]
        r -= 1
        c -= 1
        instructions = input()

        rows = [[] for _ in range(R)]
        cols = [[] for _ in range(C)]

        rows[r].append((c, c + 1))
        cols[c].append((r, r + 1))

        def update_interval(arr, v):
            if len(arr) == 0:
                arr.append((v, v + 1))
                return

            i = bisect_right(arr, (v, 0)) - 1
            a, b = arr[i]
            if b == v and i + 1 < len(arr) and arr[i + 1][0] == v + 1:
                _, e = arr.pop(i + 1)
                arr[i] = (a, e)
            elif b == v:
                arr[i] = (a, b + 1)
            elif i + 1 < len(arr) and arr[i + 1][0] == v + 1:
                _, e = arr[i + 1]
                arr[i + 1] = (v, e)
            else:
                arr.insert(i + 1, (v, v + 1))

        def find_next(arr, v, greater=True):
            i = bisect_right(arr, (v, 2 ** 32)) - 1
            a, b = arr[i]
            v = b if greater else a - 1
            update_interval(arr, v)
            return v

        for v in instructions:
            if v == 'E':
                c = find_next(rows[r], c)
                update_interval(cols[c], r)
            elif v == 'W':
                c = find_next(rows[r], c, False)
                update_interval(cols[c], r)
            elif v == 'S':
                r = find_next(cols[c], r)
                update_interval(rows[r], c)
            elif v == 'N':
                r = find_next(cols[c], r, False)
                update_interval(rows[r], c)

        return r, c


for t in range(int(input())):
    r, c = Solution().solve()
    print('Case #{}: {} {}'.format(t + 1, r + 1, c + 1))

