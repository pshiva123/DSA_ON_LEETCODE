class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder a=new StringBuilder(strs[0]);
             StringBuilder b;
        for(int i=1;i<strs.length;i++)
        {
           b=new StringBuilder(strs[i]);
           for(int j=0;j<Integer.min(a.length(),b.length());j++)
           {
               if(a.charAt(j)!=b.charAt(j))
               {
                       a.delete(j,a.length()+1);
                       break;
               }

           }
        }
        int min_index=0;
        for(int i=1;i<strs.length;i++)
        {
            if(strs[i].length()<strs[min_index].length())
            {
                min_index=i;
            }
        }
        if(a.length()>strs[min_index].length())
        {
            a.delete(strs[min_index].length(),a.length()+1);
        }
        return a+"";


    }
}
