import java.io.*;
import java.lang.Math;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] temp = new int[n];
        for(int i=0;i<n;i++){
            temp[i]=Integer.parseInt(st.nextToken());
        }
        
        int answer=0;
        int summ=0;
        for(int i=0;i<k;i++) summ+=temp[i];
        answer=summ;
        
        for(int i=0;i<n-k;i++){
            summ-=temp[i];
            summ+=temp[i+k];
            
            answer=Math.max(answer, summ);
        }
        System.out.println(answer);
        
    }
}