#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll gcdll(ll a, ll b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) { a %= b; swap(a, b); }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll K;
    if (!(cin >> n >> K)) return 0;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<pair<ll,ll>> v; // {gcd, value}
    v.reserve(n);
    for (ll x : a) v.emplace_back(gcdll(x, K), x);

    stable_sort(v.begin(), v.end(), [](const pair<ll,ll>& p1, const pair<ll,ll>& p2) {
        if (p1.first != p2.first) return p1.first > p2.first; // larger gcd first
        return p1.second < p2.second; // then smaller value first
    });

    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << v[i].second;
    }
    cout << '\n';
    return 0;
}