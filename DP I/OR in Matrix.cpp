#include <iostream>
using namespace std;

const int N = 109;

int n, m, a[N][N] = {}, b[N][N] = {}, c[N][N] = {};

unsigned int rs_hash(int keys[]) {
    unsigned int a = 63689, b = 378551;
    unsigned int hash_value = 0;
    for (int i = 0; i < m; i++) {
        hash_value = hash_value * a + keys[i];
        a = a * b;
    }
    return hash_value & 0x7FFFFFFF;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> b[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            a[i][j] = 1;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (b[i][j] == 0) {
                for (int k = 0; k < n; k++) {
                    a[k][j] = 0;
                }
                for (int k = 0; k < m; k++) {
                    a[i][k] = 0;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < n; k++) {
                if (a[k][j] == 1) {
                    c[i][j] = 1;
                }
            }
            for (int k = 0; k < m; k++) {
                if (a[i][k] == 1) {
                    c[i][j] = 1;
                }
            }
        }
    }

    bool flag = true;
    for (int i = 0; i < n; i++) {
        if (rs_hash(b[i]) != rs_hash(c[i])) {
            flag = false;
            break;
        }
    }

    if (flag) {
        cout << "YES\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cout << a[i][j] << " ";
            }
            cout << "\n";
        }
    }
    else {
        cout << "NO\n";
    }
    return 0;
}