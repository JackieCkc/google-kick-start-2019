from operator import itemgetter

for tt in range(int(input())):
    N = int(input())
    stones = []
    for _ in range(N):
        S, E, L = map(int, input().split())
        stones.append((S, E, L, S/L if L != 0 else 2**32))
    stones.sort(key=itemgetter(3))


    def dp(t, i):
        if i >= len(stones):
            return 0

        if (t, i) in mem:
            return mem[t, i]

        s, e, l, _ = stones[i]
        ans1 = dp(t + s, i + 1) + max(0, e - l * t)
        ans2 = dp(t, i + 1)
        mem[t, i] = max(ans1, ans2)
        return mem[t, i]

    mem = {}
    ans = dp(0, 0)
    print('Case #{}: {}'.format(tt + 1, ans))
