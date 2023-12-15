#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maximum_sub_array(vector<int> &nums)
    {
        int len = nums.size();
        int best = 0;
        int sum = 0;
        for (int i = 0; i < len; i++)
        {
            sum = max(nums[i], sum + nums[i]);
            best = max(best, sum);
        }

        return best;
    }
};

void printResult(vector<int> &nums)
{
    cout << "[";
    for (int s : nums)
    {
        cout << s << ",";
    }
    cout << "]\n";
}

int main()
{
    vector<int> nums{-1, 2, 4, -3, 5, 2, -5, 2};
    auto result = Solution().maximum_sub_array(nums);
    cout << "result" << result << endl;
}