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
            System.exit(0);
        }

        st = new StringTokenizer(br.readLine());
        List<Integer> score = new ArrayList<>();
        while(st.hasMoreTokens()){
            score.add(Integer.parseInt(st.nextToken()));
        }
        score.add(tesuScore);
        score.add(2000000001);
        score.sort(Comparator.reverseOrder());
        
        int rank=0;
        int sameScore=0;

        for(int i=1;i<score.size();i++){
            int currentScore=score.get(i);
            if(currentScore<tesuScore) {
                break;
            }
            if(rank>=p) {
                rank=-1;
                break;
            }
            else if(currentScore==tesuScore){
                sameScore+=1;
            }
            else if(currentScore>tesuScore){
                rank+=1;
            }
        }

        if(rank+sameScore>p) {
            rank=-1;
        }else rank+=1;
        if(rank==0) rank=-1;

        System.out.println(rank);

    }
}