import java.util.*;
class Solution {
    int answer=0;
    List<Integer> list = new ArrayList<>();
    
    public int solution(int[] numbers, int target) {
        dfs(numbers,target,0);
        return answer;
    }
    
    public void dfs(int[] numbers,int target, int idx){
        if(list.size()==numbers.length){
            int summ=0;
            for(int i:list) summ+=i;
            if(summ==target) answer+=1;  
            return;
        }
        if(idx>numbers.length-1) return;
        
        list.add(numbers[idx]);
        dfs(numbers,target,idx+1);
        list.remove(list.size()-1);
        
        list.add(-numbers[idx]);
        dfs(numbers,target,idx+1);
        list.remove(list.size()-1);
    }
}