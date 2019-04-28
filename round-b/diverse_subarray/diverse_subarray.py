from collections import Counter, defaultdict, deque
from math import log, ceil


class Node:
    def __init__(self, sum, prefix):
        self.sum = sum
        self.prefix = prefix


def build_tree(arr, i, l, r):
    if l == r:
        nodes[i].sum = arr[l]
        nodes[i].prefix = arr[l]
        return

    m = (l + r) // 2
    build_tree(arr, 2 * i + 1, l, m)
    build_tree(arr, 2 * i + 2, m + 1, r)
    nodes[i].sum = nodes[2 * i + 1].sum + nodes[2 * i + 2].sum
    nodes[i].prefix = max(
        nodes[2 * i + 1].prefix,
        nodes[2 * i + 1].sum + nodes[2 * i + 2].prefix
    )


def update(i, l, r, i2, d):
    if l == r:
        nodes[i].sum = arr[l]
        nodes[i].prefix = arr[l]
        return

    m = (l + r) // 2
    if i2 <= m:
        update(2 * i + 1, l, m, i2, d)
    else:
        update(2 * i + 2, m + 1, r, i2, d)
    nodes[i].sum = nodes[2 * i + 1].sum + nodes[2 * i + 2].sum
    nodes[i].prefix = max(
        nodes[2 * i + 1].prefix,
        nodes[2 * i + 1].sum + nodes[2 * i + 2].prefix
    )


def max_prefix(i, beg, end, l, r):
    node = Node(-1, -1)
    if beg > r or end < l:
        return node
    if beg >= l and end <= r:
        return nodes[i]

    m = (beg + end) // 2

    if l > m:
        return max_prefix(2 * i + 2, m + 1, end, l, r)

    if r <= m:
        return max_prefix(2 * i + 1, beg, m, l, r)

    left_node = max_prefix(2 * i + 1, beg, m, l, r)
    right_node = max_prefix(2 * i + 2, m + 1, end, l, r)
    node.sum = left_node.sum + right_node.sum
    node.prefix = max(left_node.prefix, left_node.sum + right_node.prefix)
    return node


n1 = int(2 * (pow(2, ceil(log(100000) / log(2)))) - 1)
nodes = [Node(-1, -1) for _ in xrange(n1)]
for tt in xrange(int(raw_input())):
    N, S = map(int, raw_input().split())
    types = [int(e) for e in raw_input().split()]
    c = Counter()
    arr = []
    d = defaultdict(deque)
    for i, t in enumerate(types):
        c[t] += 1
        if c[t] <= S:
            arr.append(1)
        elif c[t] == S + 1:
            arr.append(-S)
            d[t].append(i)
        else:
            arr.append(0)
            d[t].append(i)

    l = len(arr)
    ans = 0
    build_tree(arr, 0, 0, l - 1)
    for i in xrange(N):
        n = types[i]
        curr = max_prefix(0, 0, l - 1, i, l - 1).prefix
        ans = max(ans, curr)
        update(0, 0, l - 1, i, 0)

        arr[i] = 0
        if len(d[n]) > 0:
            v = d[n].popleft()
            arr[v] = 1
            update(0, 0, l - 1, v, 1)
        if len(d[n]) > 0:
            v = d[n][0]
            arr[v] = -S
            update(0, 0, l - 1, v, -S)

    print('Case #{}: {}'.format(tt + 1, ans))