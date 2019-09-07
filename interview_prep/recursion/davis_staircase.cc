#include <bits/stdc++.h>

using namespace std;

// Complete the stepPerms function below.
int stepPerms(int n) {
    if (n == 7) {
        return 44;
    }
    if (n == 5) {
        return 13;
    }
    if (n == 3) {
        return 4;
    }
    if (n == 2) {
        return 2;
    }
    if (n == 0 || n == 1) {
        return 1;
    }
    if (n < 0) {
        return 0;
    }
    return (stepPerms(n-3)+stepPerms(n-2)+stepPerms(n-1));

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int s;
    cin >> s;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int s_itr = 0; s_itr < s; s_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int res = stepPerms(n);

        fout << res << "\n";
    }

    fout.close();

    return 0;
}
