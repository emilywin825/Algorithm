import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> runners = new HashMap<>();
        String answer = "";
        
        for(String p: participant){
            runners.put(p, runners.getOrDefault(p,0)+1);
        }
        
        for(String c: completion){
            runners.put(c, runners.getOrDefault(c,0)-1);
        }
        
        for(Map.Entry<String, Integer> runner: runners.entrySet()){
            if(runner.getValue()>0) {
                return runner.getKey();
            }
        }
        return "";
    }
}