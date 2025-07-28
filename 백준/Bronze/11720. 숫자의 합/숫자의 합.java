import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        String num = br.readLine();
        int answer = 0;
        for(int i=0;i<n;i++){
            answer+=num.charAt(i)-'0';
        }
        
        System.out.println(answer);
    }
}