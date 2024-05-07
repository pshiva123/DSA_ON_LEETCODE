class Solution {
    public static int bs(int a[],int first,int last,int ele)
    {
        if(last > first)
        {
            return -1;
        }
        else
        {
            int mid=(first+last)/2;
            if(a[mid]==ele)
            {
               return mid;
            }
            else if(a[mid]<ele)
            {
                return bs(a,mid+1,last,ele);
            }
            else
            {
                return bs(a,first,mid-1,ele);
            }
        }
    }
    public int[] twoSum(int[] nums, int target) {
        int a[]=new int[2];
        int i,j;
        for(i=0;i<nums.length;i++)
        {
        for(j=i+1;j<nums.length;j++)
        {
            if(nums[i]+nums[j]==target)
            {
                a[0]=i;
                a[1]=j;
                break;
            }
        }
        }
        return a;
    }
}
