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

int solve() {
    return 0;
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
