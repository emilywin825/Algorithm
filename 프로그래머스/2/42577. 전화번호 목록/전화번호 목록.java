//접두어인 경우 : false, 접두어가 아닌 경우 : true
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> map = new HashMap<>();
        for(String number : phone_book){
            map.put(number, 1);
        }
        
        for(String n : phone_book){
            for(int i=1; i<n.length();i++){
                if(map.containsKey(n.substring(0,i))) return false;
            }
        }
        return true;
    }
}