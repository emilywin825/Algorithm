import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> que = new ArrayDeque<>();
        boolean answer = true;
        char[] arrayS = s.toCharArray();
        
        for(char c : arrayS){
            if(c=='('){
                que.push(c);
            } else{
                if(que.size()==0 || !(que.pop()=='('))
                    return false;
            }
        }
        if(que.size()==0)
            return answer;
        return false;
    }
}