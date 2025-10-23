//심장이 위치한 행의 번호 x, 열의 번호 y
//왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이
//위에서부터 훑으면서 * 하나짜리 찾기
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());

        boolean head=false;
        int startx=0;
        int starty=0;
        char[][] mapp = new char[n][n];

        for(int i=0;i<n;i++) {
            String input = br.readLine();
            for (int a = 0; a < input.length(); a++) {
                mapp[i][a] = input.charAt(a);
                if (head == false && mapp[i][a] == '*') {
                    startx = i;
                    starty = a;
                    head = true;
                    break;
                }
            }
        }

        startx+=1;
        System.out.println((startx+1)+" "+(starty+1));

        int leftHand=0; int rightHand=0; int waist=0; int leftLeg=0; int rightLeg=0;
        //왼팔
        for(int i=starty-1;i>=0;i--){
            if(mapp[startx][i]=='*') leftHand+=1;
            else break;
        }

        //오른팔
        for(int i=starty+1;i<n;i++){
            if(mapp[startx][i]=='*') rightHand+=1;
            else break;
        }

        //허리
        int plus=0;
        for(int i=startx+1;i<n;i++){
            if(mapp[i][starty]=='*') {
                waist+=1;
                plus+=1;
            } else break;
        }
        startx+=plus;

        //왼다
        startx+=1;
        //(6,5)
        for(int i=startx;i<n;i++){
            if(mapp[i][starty-1]=='*') leftLeg+=1;
            else break;
        }

        //오다
        for(int i=startx;i<n;i++){
            if(mapp[i][starty+1]=='*') rightLeg+=1;
            else break;
        }

        System.out.println(leftHand+" "+rightHand+" "+waist+" "+leftLeg+" "+rightLeg);
    }
}
