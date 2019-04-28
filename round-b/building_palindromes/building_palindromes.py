from collections import Counter


def can_form_palindrome(count):
    odd = 0
    for k in count.values():
        if k & 1:
            odd += 1
        if odd > 1:
            return False
    return True


for t in range(int(input())):
    N, Q = map(int, input().split())
    chars = input()

    counter = Counter()
    curr = []

    for c in chars:
        counter[c] += 1
        curr.append(counter.copy())

    ans = 0
    for i in range(Q):
        l, r = map(int, input().split())
        curr_count = curr[r - 1].copy()
        if l - 2 >= 0:
            curr_count -= curr[l - 2]
        if can_form_palindrome(curr_count):
            ans += 1
    print('Case #{}: {}'.format(t + 1, ans))
