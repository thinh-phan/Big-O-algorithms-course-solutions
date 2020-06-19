#include <iostream>
#include <math.h>
using namespace std;
#define MAXM 40 + 10
#define MAXS 300 + 10
#define INF 1e9
int main() {
    int t, m, s;
    int conventional[MAXM], infoTechnological[MAXM];
    int dp[MAXS][MAXS];
    cin >> t;
    while (t--) {
        cin >> m >> s;
        for (int i = 0; i < m; i++) {
            cin >> conventional[i] >> infoTechnological[i];
        }
        dp[0][0] = 0;
        for (int i = 0; i <= s; i++) {
            for (int j = 0; j <= s; j++) {
                if (i == 0 && j == 0) continue;
                dp[i][j] = INF;
                for (int k = 0; k < m; k++) {
                    if (i >= conventional[k] && j >= infoTechnological[k]) {
                        dp[i][j] = min(dp[i][j], dp[i - conventional[k]][j - infoTechnological[k]] + 1);
                    }
                }
            }
        }
        int ans = INF;
        for (int i = 0; i <= s; i++) {
            int tmp = sqrt(s * s - i * i);
            if (tmp * tmp == s * s - i * i) {
                ans = min(ans, dp[i][tmp]);
            }
        }
        if (ans == INF) cout << "not possible";
        else cout << ans;
        cout << endl;
    }
}