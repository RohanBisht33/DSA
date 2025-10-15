#include <bits/stdc++.h>
using namespace std;

vector<int> unionSortedArrays(const vector<int>& a, const vector<int>& b) {
    int i = 0, j = 0;
    int n = (int)a.size(), m = (int)b.size();
    vector<int> res;
    while (i < n && j < m) {
        if (a[i] == b[j]) {
            if (res.empty() || res.back() != a[i]) res.push_back(a[i]);
            int v = a[i];
            while (i < n && a[i] == v) ++i;
            while (j < m && b[j] == v) ++j;
        } else if (a[i] < b[j]) {
            if (res.empty() || res.back() != a[i]) res.push_back(a[i]);
            int v = a[i];
            while (i < n && a[i] == v) ++i;
        } else {
            if (res.empty() || res.back() != b[j]) res.push_back(b[j]);
            int v = b[j];
            while (j < m && b[j] == v) ++j;
        }
    }
    while (i < n) {
        if (res.empty() || res.back() != a[i]) res.push_back(a[i]);
        int v = a[i];
        while (i < n && a[i] == v) ++i;
    }
    while (j < m) {
        if (res.empty() || res.back() != b[j]) res.push_back(b[j]);
        int v = b[j];
        while (j < m && b[j] == v) ++j;
    }
    return res;
}

int main() {
    vector<int> nums1 = {1, 2, 3, 4, 5};
    vector<int> nums2 = {1, 2, 7};

    vector<int> u = unionSortedArrays(nums1, nums2);

    cout << "[";
    for (size_t k = 0; k < u.size(); ++k) {
        cout << u[k];
        if (k + 1 < u.size()) cout << ", ";
    }
    cout << "]\n";
    return 0;
}