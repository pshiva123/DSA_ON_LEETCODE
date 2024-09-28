class Solution {
public:
    long long maximumTotalSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        long long search=nums.back();
        long long ans=0;
        for(int i=nums.size()-1;i>=0;i--)
        {
            search=min(search,(long long)nums[i]);
            if (search<=0)
            {
              return -1;
            }
            ans+=search;
            search--;
        }
       return ans;
        
    }
};
