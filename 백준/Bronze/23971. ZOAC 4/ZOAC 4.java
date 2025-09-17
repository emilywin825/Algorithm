//h행 w열
//N행 M열을 띄우고 앉아야 함
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputt = br.readLine().split(" ");
        int h = Integer.parseInt(inputt[0]);
        int w = Integer.parseInt(inputt[1]);
        int n = Integer.parseInt(inputt[2]);
        int m = Integer.parseInt(inputt[3]);

        int x=(h-1)/(n+1)+1;
        int y=(w-1)/(m+1)+1;
        
        System.out.println(x*y);
    }
}