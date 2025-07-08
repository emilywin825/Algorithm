import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int[][] dp = new int[triangle.length][];
        for(int i=0;i<triangle.length;i++){
            dp[i]=new int[triangle[i].length];
        }
        
        dp[0][0]=triangle[0][0];
        for(int i=1;i<triangle.length;i++){
            for(int j=0;j<triangle[i].length;j++){
                if(j==0){
                    dp[i][j]=dp[i-1][j]+triangle[i][j];
                }else if(j==triangle[i].length-1){
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j];
                }else{
                    dp[i][j]=Math.max(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j]);
                }
            }
        }
        
        int maxx=0;
        for(int i : dp[triangle.length-1]){
            maxx=Math.max(maxx,i);
        }
        
        return maxx;
    }
}