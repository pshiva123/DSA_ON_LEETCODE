class Solution {
    public boolean isValid(String word) {
        word=word.toUpperCase();
        if(word.length()<3)
        {
            return false;
        }
        else
        {
            int vow=0;
            int cons=0;
            int digit=0;
            int spl=0;
            for(int i=0;i<word.length();i++)
            {
                int asc=(int)word.charAt(i);
                if(asc>=48 && asc<=57)
                {
                     digit++;
                }
                else if((asc>=0 && asc<65) ||(asc>90 && asc<97) || asc>122 )
                {
                    spl++;
                }
                 if(word.charAt(i)=='A' ||word.charAt(i)=='E' ||word.charAt(i)=='I' ||word.charAt(i)=='O' ||word.charAt(i)=='U')
                {
                     vow++;
                }
                else if(asc>65 && asc<=90)
                {
                     cons++;
                }
               
            }
            System.out.println(word);
            System.out.println(vow+" "+cons+" "+digit+" "+spl);
            //if(digit<1)
           // {
              //  return false;
           // }
             if(vow<1)
            {
                return false;
            }
             if(cons==0)
            {
                return false;
            }
             if(spl>0)
            {
                return false;
            }
        }
        return true;
    }
}
