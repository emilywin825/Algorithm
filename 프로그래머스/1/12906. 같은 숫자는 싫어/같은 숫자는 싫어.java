import java.util.*;
// O(n)
public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        int target=-1;
        
        for(int i=0;i<arr.length;i++){
            if(target!=arr[i]){
                target=arr[i];
                answer.add(target);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}