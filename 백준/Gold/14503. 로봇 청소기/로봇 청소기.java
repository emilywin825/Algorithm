//각 칸은 벽 또는 빈 칸
//0 : 빈칸, 1 : 벽
import java.util.*;
import java.io.*;
class Main{
    
    static int[][] mapp;
    static int[][] visited;
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        mapp = new int[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                mapp[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = bfs(r, c, d);
        System.out.println(answer);
    }

    public static int bfs(int r, int c, int d) {
        Deque<int[]> stack = new ArrayDeque<>();
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        stack.offer(new int[]{r, c, d});
        int clean = 0;

        while (!stack.isEmpty()) {
            int[] arr = stack.poll();
            int x = arr[0];
            int y = arr[1];
            int dir = arr[2];

            if (visited[x][y] == 0) {
                visited[x][y] = 1;
                clean++;
            }
            boolean isClean = false;

            for (int i = 0; i < 4; i++) {
                dir = (dir + 3) % 4;
                int xx = x + dx[dir];
                int yy = y + dy[dir];
                if (0 <= xx && xx < n && 0 <= yy && yy < m && visited[xx][yy] == 0 && mapp[xx][yy] == 0) {
                    stack.offer(new int[]{xx, yy, dir});
                    isClean = true;
                    break;
                }
            }

            if (!isClean) {
                //방향 유지 후 한칸 후진 후 1번 이동
                int xx = x + dx[(dir + 2) % 4];
                int yy = y + dy[(dir + 2) % 4];
                if (0 <= xx && xx < n && 0 <= yy && yy < m && mapp[xx][yy] == 0) {
                    stack.offer(new int[]{xx, yy, dir});
                } else {
                    break;
                }
            }
        }
        return clean;
    }
}
