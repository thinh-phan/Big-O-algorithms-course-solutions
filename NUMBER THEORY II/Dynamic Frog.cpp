#include <bits/stdc++.h>

using namespace std;

const int MAXN = 105;

int nTest, n, D, x[MAXN];
bool isLarge[MAXN];

int getMinimaxLeap(int l, int r) {
    if (l+1 == r)
        return x[r] - x[l];

    int leap = 0;
    for(int i = l; i < r-1; ++i)
        leap = max(leap, x[i+2] - x[i]);
    return leap;
}

int main() {
    cin >> nTest;
    for(int iTest = 1; iTest <= nTest; ++iTest) {
        cin >> n >> D;
        for(int i = 1; i <= n; ++i) {
            string s;
            cin >> s;

            isLarge[i] = (s[0] == 'B');
            x[i] = stoi(s.substr(2));
        }

        isLarge[0] = true;
        x[0] = 0;

        isLarge[n+1] = true;
        x[n+1] = D;

        int ans = 0;
        int lastLarge = 0;
        for(int i = 1; i <= n+1; ++i) {
            if (isLarge[i]) {
                ans = max(ans, getMinimaxLeap(lastLarge, i));
                lastLarge = i;
            }
        }
        printf("Case %d: %d\n", iTest, ans);
    }
}