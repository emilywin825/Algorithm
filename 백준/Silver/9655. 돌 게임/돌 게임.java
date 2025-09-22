import java.io.*;

//돌을 1 or 3개 가져감 -> 마지막 돌을 가져가는 사람이 이김
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        if(n%2==0){
            System.out.println("CY");
        }else{
            System.out.println("SK");
        }
    }
}