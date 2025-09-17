import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            String[] temp=br.readLine().split(" ");
            Integer[] inputt=new Integer[temp.length];
            for(int i=0;i<temp.length;i++){
                inputt[i]=Integer.parseInt(temp[i]);
            }
            Arrays.sort(inputt);
            
            int a = inputt[0];
            int b = inputt[1];
            int c = inputt[2];
            
            if(a==0 && b==0 && c==0) break;
            if(a+b<=c) {
                System.out.println("Invalid");
                continue;
            }
            if(a==b && a==c && b==c) {
                System.out.println("Equilateral");
                continue;
            }
            if(a==b || a==c || b==c) {
                System.out.println("Isosceles");
                continue;
            }
            System.out.println("Scalene");
            continue;
        }
    }
}