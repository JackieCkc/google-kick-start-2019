#include <iostream>
#include <map>
#include <vector>
#include <math.h>

using namespace std;

struct Node {
    int sum;
    int prefix;
};

void build_tree(Node nodes[], int arr[], int i, int l, int r) {
    if (l == r) {
        nodes[i].sum = arr[l];
        nodes[i].prefix = arr[l];
        return;
    }

    int m = (l + r) / 2;
    build_tree(nodes, arr, 2 * i + 1, l, m);
    build_tree(nodes, arr, 2 * i + 2, m + 1, r);
    nodes[i].sum = nodes[2 * i + 1].sum + nodes[2 * i + 2].sum;
    nodes[i].prefix = max(
            nodes[2 * i + 1].prefix,
            nodes[2 * i + 1].sum + nodes[2 * i + 2].prefix
    );
}

void update(Node nodes[], int arr[], int i, int l, int r, int i2, int d) {
    if (l == r) {
        nodes[i].sum = arr[l];
        nodes[i].prefix = arr[l];
        return;
    }
    int m = (l + r) / 2;
    if (i2 <= m) {
        update(nodes, arr, 2 * i + 1, l, m, i2, d);
    } else {
        update(nodes, arr, 2 * i + 2, m + 1, r, i2, d);
    }
    nodes[i].sum = nodes[2 * i + 1].sum + nodes[2 * i + 2].sum;
    nodes[i].prefix = max(
            nodes[2 * i + 1].prefix,
            nodes[2 * i + 1].sum + nodes[2 * i + 2].prefix
    );
}

Node max_prefix(Node nodes[], int i, int beg, int end, int l, int r) {
    Node node = {-1, -1};
    if (beg > r || end < l) {
        return node;
    }
    if (beg >= l && end <= r) {
        return nodes[i];
    }

    int m = (beg + end) / 2;
    if (l > m) {
        return max_prefix(nodes, 2 * i + 2, m + 1, end, l, r);
    }
    if (r <= m) {
        return max_prefix(nodes, 2 * i + 1, beg, m, l, r);
    }

    Node left_node = max_prefix(nodes, 2 * i + 1, beg, m, l, r);
    Node right_node = max_prefix(nodes, 2 * i + 2, m + 1, end, l, r);
    node.sum = left_node.sum + right_node.sum;
    node.prefix = max(left_node.prefix, left_node.sum + right_node.prefix);
    return node;
}

int main() {
    int n = int(2 * (pow(2, ceil(log(100000) / log(2)))) - 1);
    Node nodes[n];

    int tc;
    cin >> tc;
    for (int tt = 1; tt <= tc; tt++) {
        int N, S;
        cin >> N >> S;
        int types[N];
        for (int i = 0; i < N; i++) {
            cin >> types[i];
        }

        map<int, int> c;
        map<int, vector<int>> d;
        int arr[N];

        for (int i = 0; i < N; i++) {
            int t = types[i];
            c[t] += 1;

            if (c[t] <= S) {
                arr[i] = 1;
            } else if (c[t] == S + 1) {
                arr[i] = -S;
                d[t].push_back(i);
            } else {
                arr[i] = 0;
                d[t].push_back(i);
            }
        }

        int ans = 0;
        build_tree(nodes, arr, 0, 0, N - 1);
        for (int i = 0; i < N; i++) {
            int type = types[i];
            int curr = max_prefix(nodes, 0, 0, N - 1, i, N - 1).prefix;
            ans = max(ans, curr);
            arr[i] = 0;
            update(nodes, arr, 0, 0, N - 1, i, 0);
            if (!d[type].empty()) {
                int v = d[type][0];
                d[type].erase(d[type].begin());
                arr[v] = 1;
                update(nodes, arr, 0, 0, N - 1, v, 1);
            }
            if (!d[type].empty()) {
                int v = d[type][0];
                arr[v] = -S;
                update(nodes, arr, 0, 0, N - 1, v, -S);
            }
        }
        cout << "Case #" << tt << ": " << ans << endl;
    }
}
