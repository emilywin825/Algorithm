import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        //스택 사용
        Deque<String> stack = new ArrayDeque<>();
        for(int i=0;i<s.length();i++){
            String now = s.substring(i,i+1);
            
            if(now.equals("(")||stack.size()==0){
                stack.push(now);
            } else{
                if(!stack.pop().equals("(")){
                    return false;
                }
            }
        }
        
        if(stack.size()>0){
            return false;
        }
        
        return answer;
    }
}