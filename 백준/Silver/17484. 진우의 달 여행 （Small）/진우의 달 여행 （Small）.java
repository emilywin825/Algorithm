//이동 가능 경로 : 왼,아래,오
//같은 방향으로 두번 연속 움직일 수 없음
//bfs - 너비 우선 탐색, 큐
import java.io.*;
import java.util.*;
import java.lang.*;

public class Main{
    static int m;
    static int n;
    static int[][] space;
    static int[] dx= {1,1,1};
    static int[] dy={-1,0,1};
    static int answer=Integer.MAX_VALUE;
    
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); //행
        m = Integer.parseInt(st.nextToken()); //열
        space = new int[n][m];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++){
                space[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        
        for(int k=0;k<m;k++){
            dfs(0, k, -1, space[0][k]);
        }
        System.out.println(answer);
    }
    
    public static void dfs(int x, int y, int prevDir, int fuel){
        if(x==n-1){
            answer=Math.min(answer,fuel);
            return;
        }
        
        for(int i=0; i<3; i++){
            if(prevDir==i) continue;
            
            int xx=x+dx[i];
            int yy=y+dy[i];
                
            if(xx>=0 && xx<n && yy>=0 && yy<m){
                dfs(xx,yy,i,fuel+space[xx][yy]);
            }
        }    
    }
}