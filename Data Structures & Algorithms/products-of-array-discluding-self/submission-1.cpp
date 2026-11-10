
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> sol(n, 1);

        int pro = 1;

        for(int i = 0; i < n; i++)
        {
            sol[i] = pro;
            pro = pro * nums[i];
        }

        pro = 1;

        for(int i = n - 1; i >= 0; i--)
        {
            sol[i] = sol[i] * pro;
            pro = pro * nums[i];
        }

        return sol;
    }
};
