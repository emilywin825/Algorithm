import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int[] dp = new int[n+1];
        int[] prev = new int[n+1];
        
        for(int i=2;i<n+1;i++){
            dp[i]=dp[i-1]+1;
            prev[i]=i-1;
            
            if(i%2==0 && dp[i/2]+1<dp[i]){
                dp[i]=dp[i/2]+1;
                prev[i]=i/2;
            }
            
            if(i%3==0 && dp[i/3]+1<dp[i]){
                dp[i]=dp[i/3]+1;
                prev[i]=i/3;
            }
        }
        
        System.out.println(dp[n]);
        
        StringBuilder sb = new StringBuilder();
        while(n>0){
            sb.append(n).append(" ");
            n=prev[n];
        }
        
        System.out.println(sb.toString().trim());
    }
}