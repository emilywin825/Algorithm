import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Deque<Integer> deque = new ArrayDeque<>();
        int target=-1;
        
        for(int i : arr){
            if(target!=i){
                deque.offerLast(i);
                target=i;
            }
        }
        
        int[] answer=new int[deque.size()];
        for(int i=0;i<answer.length;i++ ){
            answer[i]=deque.pollFirst();
        }
        
        return answer;
    }
}