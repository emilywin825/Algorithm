//완주하지 못한 1명을 출력, 동명이인이 있을 수 있음
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> runners = new HashMap<>();
        String answer = "";
        for(int i=0;i<participant.length;i++){
            runners.put(participant[i], runners.getOrDefault(participant[i],0)+1);
        }
        
        for(int j=0;j<completion.length;j++){
            runners.put(completion[j], runners.get(completion[j])-1);
        }
        
        for(Map.Entry<String, Integer> runner: runners.entrySet()){
            if(runner.getValue()>0) {
                answer=runner.getKey();
                break;
            }
        }
        return answer;
    }
}