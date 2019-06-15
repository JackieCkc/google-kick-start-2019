#include <iostream>
#include <map>
#include <vector>
#include <tuple>
#include <array>
#include <stack>
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

void print(vector<int> &arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

struct Tables {
    vector<vector<int>> max_table;
    vector<vector<int>> min_table;
};

vector<int> compute_logs(int n) {
    vector<int> logs = {0, 0};
    for (int i = 2; i < n + 1; i++) {
        logs.push_back(logs[i / 2] + 1);
    }
    return logs;
}

Tables build(vector<int> &arr, int l) {
    vector<vector<int>> min_table(l, vector<int> (10, 0));
    vector<vector<int>> max_table(l, vector<int> (10, 0));

    for (int i = 0; i < l; i++) {
        max_table[i][0] = arr[i];
        min_table[i][0] = arr[i];
    }

    for (int j = 1; j < 11; j++) {
        for (int i = 0; i < l - (1 << j) + 1; i++) {
            max_table[i][j] = max(max_table[i][j - 1], max_table[i + (1 << (j - 1))][j - 1]);
            min_table[i][j] = min(min_table[i][j - 1], min_table[i + (1 << (j - 1))][j - 1]);
        }
    }

    return {max_table, min_table};
}

int get_min(int l, int r, vector<vector<int>> &table, vector<int> &logs) {
    int j = logs[r - l + 1];
    return min(table[l][j], table[r - (1 << j) + 1][j]);
}

int get_max(int l, int r, vector<vector<int>> &table, vector<int> &logs) {
    int j = logs[r - l + 1];
    return max(table[l][j], table[r - (1 << j) + 1][j]);
}

int max_rentagle(int hist[], int n)
{
    stack<int> s;

    int max_area = 0;
    int tp;
    int area_with_top;

    int i = 0;
    while (i < n)
    {
        if (s.empty() || hist[s.top()] <= hist[i])
            s.push(i++);
        else
        {
            tp = s.top();
            s.pop();

            area_with_top = hist[tp] * (s.empty() ? i :
                                        i - s.top() - 1);

            if (max_area < area_with_top)
                max_area = area_with_top;
        }
    }

    while (!s.empty())
    {
        tp = s.top();
        s.pop();
        area_with_top = hist[tp] * (s.empty() ? i :
                                    i - s.top() - 1);

        if (max_area < area_with_top)
            max_area = area_with_top;
    }

    return max_area;
}

int search(vector<vector<int>> &max_table, vector<vector<int>> &min_table, vector<int> &logs, int j, int k, int n, int c) {
    int s = j, e = n;
    while (s < e - 1) {
        int m = (s + e) / 2;
        int max_val = get_max(j, m, max_table, logs);
        int min_val = get_min(j, m, min_table, logs);

        if (max_val - min_val <= k) {
            s = m;
        } else {
            e = m;
        }
    }
    return s - j + 1;
}

int solve() {
    int R, C, K;
    cin >> R >> C >> K;

    vector<vector<int>> rows;
    for (int i = 0; i < R; i++) {
        vector<int> v;
        for (int j = 0; j < C; j++) {
            int n;
            cin >> n;
            v.push_back(n);
        }
        rows.push_back(v);
    }

    vector<vector<int>> mem(R, vector<int>(C, 0));
    vector<int> logs = compute_logs(C);
    for (int i = 0; i < R; i++) {
        Tables t = build(rows[i], C);
        vector<vector<int>> max_table = t.max_table, min_table = t.min_table;
        for (int j = 0; j < C; j++) {
            mem[i][j] = search(max_table, min_table, logs, j, K, C, rows[i][j]);
        }
    }

    int ans = 0;
    for (int i = 0; i < C; i++) {
        int bars[R];
        for(int j = 0; j < R; j++) {
            bars[j] = mem[j][i];
        }
        ans = max(ans, max_rentagle(bars, R));
    }
    return ans;
}

int main() {
    int tc;
    cin >> tc;
    for (int tt = 1; tt <= tc; tt++) {
        int ans = solve();
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
