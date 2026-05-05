import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        //Map으로 같은 종류의 개수를 count
        //headgear : 2 -> 3
        //eyewear : 1 -> 2
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        for(String[] cloth : clothes){
            String key = cloth[1];
            map.put(key,map.getOrDefault(key, 0)+1);
        }
        
        for(String s : map.keySet()){
            answer*=(map.get(s)+1);
        }
        return answer-1;
    }
}