// 전체 학생:n,도난학생:lost,체육복:reverse
// return 체육수업 들을 수 있는 학생 최대값
import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);   
        
        Set<Integer> lostSet = new HashSet<>();
        Set<Integer> reserveSet = new HashSet<>();
        
        for(int l : lost) lostSet.add(l);
        for(int r: reserve){
            if(lostSet.contains(r)){
                lostSet.remove(r);
            } else{
                reserveSet.add(r);
            }
        }
        
        for(int l : lost){
            if(lostSet.contains(l)){
                if(reserveSet.contains(l-1)){
                    reserveSet.remove(l-1);
                    lostSet.remove(l);
                }else if(reserveSet.contains(l+1)){
                    reserveSet.remove(l+1);
                    lostSet.remove(l);
                }
            }
        }
      
        
        return n-lostSet.size();
    }
}