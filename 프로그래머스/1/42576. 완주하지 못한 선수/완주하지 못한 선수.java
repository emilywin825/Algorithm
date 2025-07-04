import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        
        Map<String,Integer> map = new HashMap<>();
        for(String s : participant){
            int num=map.getOrDefault(s,0);
            map.put(s,num+1);
        }
        
        
        for(String s : completion){
            int num=map.get(s);
            map.put(s,num-1);
        }
        
        String answer="";
        for(String key : map.keySet()){
            if(map.get(key)!=0){
                answer=key;
                break;
            }
        }
        return answer;
    }
}