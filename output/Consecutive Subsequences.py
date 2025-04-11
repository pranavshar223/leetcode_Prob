
#include<vector>
#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;



struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
    public:
        ListNode* mergeKLists(vector<ListNode*>& lists) {
            // we can solve the problem in O(nklog(k))
            priority_queue< pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > heaps;
            for(int i = 0; i < lists.size() ; i++){
                if(lists[i]){
                    heaps.push(pair(lists[i]->val,i));
                }
            }
            ListNode* head = new ListNode(0);
            ListNode* curr = head;
            while(!heaps.empty()){
                pair<int,int> smallestElem = heaps.top();
                heaps.pop();
                curr->next = lists[smallestElem.second];
                curr = curr->next;
                lists[smallestElem.second] = lists[smallestElem.second]->next;
                if(lists[smallestElem.second]) heaps.push(pair(lists[smallestElem.second]->val,smallestElem.second));
            }
            ListNode * temp = head;
            head = head->next;
            temp->next = nullptr;
            delete temp;
            temp = nullptr;
            return head;
        }
    };



int main() {
    Solution solution;
    vector<ListNode*> lists; // Initialize your list of ListNode pointers here
    // Populate the lists with some test data
    ListNode* result = solution.mergeKLists(lists);
    // Print the merged list or perform further operations
    return 0;
}
// This code defines a class Solution with a method mergeKLists that merges k sorted linked lists into one sorted linked list. The main function demonstrates how to use the mergeKLists method.    