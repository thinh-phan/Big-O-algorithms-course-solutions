#include <bits/stdc++.h>
using namespace std;
const int MAX = 1005;

long long a[MAX];
long long f[MAX][MAX];

long long knapsack(int n, int w) {
    for (int i = 0; i <= n; i++) {
        f[i][0] = 0;
    }

    for (int i = 0; i <= w; i++) {
        f[0][i] = 0;
    }

    for (int i = a[0]; i <= w; i++) {
        f[1][i] = a[0];
    }
    
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= w; j++) {
            if (a[i - 1] > j) {
                f[i][j] = f[i - 1][j];
            }
            else {
                long long tmp1 = a[i - 1] + f[i - 2][j - a[i - 1]];
                long long tmp2 = f[i - 1][j];
                f[i][j] = max(tmp1, tmp2);
            }
        }
    }

    return f[n][w];
}

int main() {
    int tc, n, k;
    cin >> tc;

    for (int t = 1; t <= tc; t++) {
        cin >> n >> k;

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        cout << "Scenario #" << t << ": " << knapsack(n, k);
        if (t != tc) {
            cout << endl;
        }
    }

    return 0;
}