import java.lang.*;
import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int tesuScore=Integer.parseInt(st.nextToken());
        int p=Integer.parseInt(st.nextToken());
        if(n==0) {
            System.out.println("1");
            return;
        }

        st = new StringTokenizer(br.readLine());
        int[] score = new int[n];
        for(int i=0;i<n;i++){
            score[i]=Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(score);
        int rank=1;
        
        for(int i=n-1;i>=0;i--){
            if(score[i]>tesuScore) rank++;
            else break;
        }
        
        if(n==p && score[0]>=tesuScore){
            System.out.println(-1);
        }else{
            System.out.println(rank);
        }
    }
}