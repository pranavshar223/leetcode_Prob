#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

class Solution {
    public:
        int findKthLargest(vector<int>& nums, int k) {
            nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
            return nums[k - 1];
        }
    };


int main() {
    Solution solution;
    vector<int> nums = {3, 2, 1, 5, 6, 4};
    int k = 2;
    cout << solution.findKthLargest(nums, k) << endl; // Output: 5
    return 0;
}
// This code defines a class Solution with a method findKthLargest that finds the k-th largest element in an array.    