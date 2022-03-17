#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    string ufo, group;
    cin >> ufo >> group;

    int sum_ufo = (int) ufo[0] - 64;
    int sum_group = (int) group[0] - 64;
    
    for (int i = 1; i < 6; ++i)
        sum_ufo *= (int) ufo[i] - 64;
    for (int i = 1; i < 6; ++i)
        sum_group *= (int) group[i] - 64;
    
    if (sum_ufo % 47 == sum_group % 47) cout << "GO\n";
    else cout << "STAY\n";
}
