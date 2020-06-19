#include <bits/stdc++.h>
#define eb emplace_back
using namespace std;
typedef vector<int> vi;
const double INF = 1e15;
const int inf = 1e9 + 1;
const double eps = 1e-5;

enum event_type {
    consumption, leak, gas, mechanic, goal
};
struct event {
    int d;
    event_type type;
    int n;
};

bool travelable(vector<event>& events, double tank) {
    double fuel = tank, consumption_rate = 0;
    int leaks = 0, last_pos = 0;
    for (auto& e : events) {
        fuel -= (e.d - last_pos) * (consumption_rate + leaks);
        if (fuel < 0) {
            return false;
        }
        if (e.type == consumption) {
            consumption_rate = e.n / 100.0;
        }
        else if (e.type == leak) {
            ++leaks;
        }
        else if (e.type == gas) {
            fuel = tank;
        }
        else if (e.type == mechanic) {
            leaks = 0;
        }
        last_pos = e.d;
    }
    return true;
}

void solve() {
    string s;
    vector<event> events;
    while (1) {
        int d, n = 0;
        event_type t;
        cin >> d >> s;
        if (s == "Fuel") {
            cin >> s >> n;
            if (d == 0 && n == 0) {
                exit(0);
            }
            t = consumption;
        }
        else if (s == "Gas") {
            cin >> s;
            t = gas;
        }
        else if (s == "Mechanic") {
            t = mechanic;
        }
        else if (s == "Leak") {
            t = leak;
        }
        else {
            t = goal;
        }
        events.push_back({d, t, n});
        if (t == goal) {
            break;
        }
    }

    double l = 0, r = INF;
    while (r - l > eps) {
        double mid = (l + r) / 2;
        if (travelable(events, mid)) {
            r = mid;
        }
        else {
            l = mid;
        }
    }
    
    printf("%.3lf\n", r);   
}

int main() {
    while (1) {
        solve();
    }
}