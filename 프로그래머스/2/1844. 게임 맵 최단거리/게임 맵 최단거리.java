import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int[][] visited= new int[maps.length][maps[0].length];
        return bfs(visited,maps);
    }
        
    public int bfs(int[][] visited,int[][] maps){
        Deque<int[]> q = new ArrayDeque<>();
        visited[0][0]=1;
        q.offer(new int[]{0,0});
        int answer=0;

        while(!q.isEmpty()){
            int[] now=q.poll();
            int x=now[0];
            int y=now[1];

            int[] dx={-1,0,1,0};
            int[] dy={0,1,0,-1};
            for(int i=0;i<4;i++){
                int xx=x+dx[i];
                int yy=y+dy[i];
                if(0<=xx&&xx<maps.length && 0<=yy && yy<maps[0].length && visited[xx][yy]==0 && maps[xx][yy]==1){
                    q.offer(new int[]{xx,yy});
                    visited[xx][yy]=visited[x][y]+1;
                }

            }
        }
        return visited[maps.length-1][maps[0].length-1]==0?-1:visited[maps.length-1][maps[0].length-1];
    }
        
}