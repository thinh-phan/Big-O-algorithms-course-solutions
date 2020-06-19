#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string exp;

int get_integer(int it) {
    string temp = "";
    while (isdigit(exp[it]) || exp[it] == '-') {
        temp += exp[it];
        it++;
    }
    return stoi(temp);
}

int left_child(int it) {
    while (isdigit(exp[it]) || exp[it] == '-') {
        it++;
    }

    if (!(isdigit(exp[it + 1]) || exp[it + 1] == '-')) {
        return -1;
    }

    return it + 1;
}

int right_child(int it) {
    while (isdigit(exp[it]) || exp[it] == '-') {
        it++;
    }

    int brackets = 1;
    it++;
    while (brackets > 0) {
        if (exp[it] == '(') {
            brackets++;
        }
        else if (exp[it] == ')') {
            brackets--;
        }
        it++;
    }

    if (!(isdigit(exp[it + 1]) || exp[it + 1] == '-')) {
        return -1;
    }

    return it + 1;
}

bool check(int it, int target, int current) {
    if (isdigit(exp[it]) || exp[it] == '-') {
        current += get_integer(it);
    }
    else {
        return false;
    }

    int left = left_child(it);
    int right = right_child(it);

    if (left == -1 && right == -1) {
        return target == current;
    }

    bool left_path = false, right_path = false;

    if (left != -1) {
        left_path = check(left, target, current);
    }
    if (right != -1) {
        right_path = check(right, target, current);
    }

    return left_path || right_path;
}

int main() {
    int sum, next_sum;
    while (cin >> sum) {
        exp = "";
        string temp;
        int brackets = 0;
        while (cin >> temp) {
            for (int i = 0; i < temp.length(); i++) {
                if (temp[i] == '(') {
                    brackets++;
                }
                else if (temp[i] == ')') {
                    brackets--;
                }
            }

            exp += temp;
            if (brackets == 0) {
                break;
            }
        }

        cerr << sum << " " << exp << endl;

        if (check(1, sum, 0)) {
            cout << "yes\n";
        }
        else {
            cout << "no\n";
        }
        sum = next_sum;
    }
    return 0;
}