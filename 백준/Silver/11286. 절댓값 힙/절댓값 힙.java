//절대값이 가장 작은 값을 출력하고 제거
//절대값이 작은 값이 여러개라면 가장 작은 수를 출력하고 그 값을 제거
import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt((int[] a)->a[0])
                                                     .thenComparingInt((int[] a)->a[1]));
        for(int i=0;i<n;i++){
            int input = Integer.parseInt(br.readLine());
            if(input==0){
                if(pq.isEmpty()){
                    System.out.println(0);
                }else{
                    System.out.println(pq.poll()[1]);
                }
                continue;
            }
            pq.offer(new int[]{Math.abs(input),input});
        }
    }
}
