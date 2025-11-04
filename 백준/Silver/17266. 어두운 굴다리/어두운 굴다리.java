//M개의 가로등, 가로등 위치 X
//가로등은 왼/오를 높이만큼 비출 수 있음. 모두 같은 높이
//최소한의 높이로 
import java.util.*;
import java.io.*;

public class Main{
    static int n;
    static int m;
    static int[] light;
    public static void main(String[] args)throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        light=Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        int lt=1;
        int rt=n;
        int answer=0;
        while(lt<=rt){
            int mid=(lt+rt)/2;
            if(possible(mid)){
                answer=mid;
                rt=mid-1;
            }else{
                lt=mid+1;
            }
        }
        System.out.println(answer);
    }
    
    public static boolean possible(int mid){
        int prev=0;
        for(int i=0;i<light.length;i++){
            if(light[i]-mid<=prev){
                prev=light[i]+mid;
            } else return false;
        }
        return prev>=n;
    }
}