        // x*y==brown+yellow
        // 2x+2y==brown+4
        // brown=2x+2y-4
import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int x=0;
        int y=0;
        int xy=brown+yellow;
        for(int i=1;i<xy;i++){    
            if(xy%i!=0) continue;
            x=i;
            y=xy/i;
            if(2*x+2*y==brown+4){
                answer[0]=Math.max(x,y);
                answer[1]=Math.min(x,y);
                break;
            }
        }
        return answer;
    }
}