//Y : 윷놀이-2, F : 같은 그림 찾기-3, O : 원카드-4
//N : 플레이 신청 횟수
//임스가 플레이할 게임의 종류
//임스와는 한번만 플레이할 수 있음
//return 최대 몇번 임스와 플레이할 수 있는지
import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input=br.readLine();
        String[] inputArr=input.split(" ");
        int n=Integer.parseInt(inputArr[0]);
        String gameType=inputArr[1];
        Set<String> playerList = new HashSet<>();
        
        for(int i=0;i<n;i++){
            String player = br.readLine();
            playerList.add(player);
        }
        
        if(gameType.equals("Y")){
            System.out.println(playerList.size());
        }else if(gameType.equals("F")){
            System.out.println(playerList.size()/2); 
        }else if(gameType.equals("O")){
            System.out.println(playerList.size()/3);
        }
        
        
    }
}