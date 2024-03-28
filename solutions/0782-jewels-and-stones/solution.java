class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int c=0;
        for(int i=0;i<stones.length();i++)
        {
            String st=stones.charAt(i)+"";
            if(jewels.contains(st)) c++;

        }
        return c;
    }
}
