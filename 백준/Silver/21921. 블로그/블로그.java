//슬라이딩 윈도우
import java.io.*;
import java.util.*;
class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n=Integer.parseInt(st.nextToken());
        int x=Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] visitor = new int[n];
        for(int i=0;i<n;i++){
            visitor[i]=Integer.parseInt(st.nextToken());
        }

            long summ=0;
            for(int i=0;i<x;i++) summ+=visitor[i];
            long max=summ;
            int cnt=1;
        
            for(int i=0;i<n-x;i++){                
                summ-=visitor[i];
                summ+=visitor[i+x];
                
                if(max<summ) {
                    cnt=1;
                    max = summ;
                }
                else if(max==summ) cnt+=1;
            }
            
            if(max==0){
                System.out.println("SAD");
            }else{
                System.out.println(max);
                System.out.println(cnt);
            }
            
            br.close();
    }
}