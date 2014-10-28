#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char> > &board) {
        iter(board, 0, 0);
    }
private:
    bool isValid(vector<vector<char> > &board, int i, int j) {
        for (int k = 0; k < 9; k++) {
            if (k != i && board[k][j] == board[i][j])
                return false;
            if (k != j && board[i][k] == board[i][j])
                return false;
        }
        for (int k = i / 3 * 3; k < i / 3 * 3 + 3; k++) {
            for (int h = j / 3 * 3; h < j / 3 * 3 + 3; h++) {
                if (k != i && j != h && board[k][h] == board[i][j])
                    return false;
            }
        }
        return true;
    }
    bool iter(vector<vector<char> > &board, int i, int j) {
        if (j >= 9)
            return iter(board, i + 1, 0);
        if (i == 9)
            return true;

        if (board[i][j] == '.') {
            for (int k = 1; k <= 9; k++) {
                board[i][j] = (char) k + '0';
                if (isValid(board, i, j))
                    if (iter(board, i, j + 1))
                        return true;
                board[i][j] = '.';
            }
        }
        else
            return iter(board, i, j + 1);
        return false;
    }
};

int main() {
    Solution s;
    s.solveSudoku()
}