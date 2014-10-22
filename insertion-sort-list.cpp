#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode *insertionSortList(ListNode *head) {
        if (!head) {
            return NULL;
        }
        ListNode *temp1, *temp2;
        ListNode *start = new ListNode(0);
        start -> next = head;
        ListNode *cur_node = head;
        while (cur_node -> next) {
            ListNode *pre_node = start;
            while (pre_node != cur_node) {
                if (pre_node -> next -> val > cur_node -> next -> val) {
                    temp1 = pre_node -> next;
                    temp2 = cur_node -> next -> next;
                    pre_node -> next = cur_node -> next;
                    cur_node -> next -> next = temp1;
                    cur_node -> next = temp2;
                    break;
                }
                else
                    pre_node = pre_node -> next;
            }
            if (pre_node == cur_node)
                cur_node = cur_node -> next;
        }
        return start -> next;
    }
};

int main() {
    ListNode *n1 = new ListNode(4);
    ListNode *n2 = new ListNode(1);
    ListNode *n3 = new ListNode(3);
    ListNode *n4 = new ListNode(2);
    n1 -> next = n2;
    n2 -> next = n3;
    n3 -> next = n4;
    Solution s;
    cout << s.insertionSortList(n1) -> next -> val << endl;
}