//문자열 길이가 4||6 &&숫자로만 구성
class Solution {
    public boolean solution(String s) {
        boolean answer = false;
        if((s.length()==4 || s.length()==6)&&s.matches("[0-9]+")){        
            answer=true;
        }
        return answer;
    }
}