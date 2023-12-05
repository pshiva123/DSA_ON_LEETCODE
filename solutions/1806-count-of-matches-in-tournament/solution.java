
class Solution {
    public int numberOfMatches(int n) {
     int no=0;
     while(n>1)
     {
        if(n%2!=0)
        {
            no++;
            n-=1;
        }
        else
        {
            n/=2;
            no+=n;
        }
     }
      return no;
      
    }
}
