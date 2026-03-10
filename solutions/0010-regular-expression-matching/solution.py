class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i, j,dp):
            if j == len(p):
                return i == len(s)
            if (i,j) in dp:
                return dp[(i,j)]
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                dp[(i,j)]= f(i, j+2,dp) or (first_match and f(i+1, j,dp))
            else:
                dp[(i,j)]= first_match and f(i+1, j+1,dp)
            return dp[(i,j)]
        dp={}
        return f(0, 0,dp)


    
   
  

    
        
    


        
