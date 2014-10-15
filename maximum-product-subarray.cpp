#include <iostream>

using namespace std;

class Solution {
private:
    int min(int a, int b) {
        return a > b? b : a;
    }
    int max(int a, int b) {
        return a > b? a : b;
    }
public:
    int maxProduct(int A[], int n) {
        int max_prod = 1, min_prod = 1, r = A[0];
        for (int i = 0; i < n; i++) {
            if (A[i] > 0) {
                max_prod *= A[i];
                min_prod = min(min_prod * A[i], 1);
                if (r < max_prod)
                    r = max_prod;
            }
            else if (A[i] == 0) {
                max_prod = min_prod = 1;
                if (r < 0)
                    r = 0;
            }
            else {
                if (r < min_prod * A[i])
                    r = min_prod * A[i];
                int temp = max_prod;
                max_prod = max(min_prod * A[i], 1);
                min_prod = temp * A[i];
            }
        }
        return r;
    }
};

int main() {
    Solution s;
    int A[] = {1, 2, -3, 4, 5, -6, 7, 8, 9, 10};
    cout << s.maxProduct(A, 10) << endl;
    return 0;
}