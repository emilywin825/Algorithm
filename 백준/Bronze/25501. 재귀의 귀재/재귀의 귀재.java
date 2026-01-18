//문자열이 팰린드롬인지 여부를 판단
//print - T : 1, F : 0 / recursion 함수의 호출 횟수
import java.io.*;

public class Main{
    static int iter;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            String s = br.readLine();
            iter=0;
            int res=recursion(s, 0, s.length()-1);
            System.out.println(res + " " + iter);
        }
    }
    
    public static int recursion(String s, int l, int r){
        iter+=1;
        if(l>=r) return 1;
        else if(s.charAt(l)!=s.charAt(r)) return 0;
        else return recursion(s, l+1, r-1);
    }
}