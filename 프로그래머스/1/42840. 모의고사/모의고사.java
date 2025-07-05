import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        List<Integer> lis=new LinkedList<>();
        
        int[] one={1,2,3,4,5};
        int[] two={2, 1, 2, 3, 2, 4, 2, 5};
        int[] three={3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int oneRes=cntAnswer(answers,one);
        int twoRes=cntAnswer(answers,two);
        int threeRes=cntAnswer(answers,three);
        
        int maxx=Math.max(oneRes,Math.max(twoRes,threeRes));
        
        if(maxx==oneRes){lis.add(1);}
        if(maxx==twoRes){lis.add(2);}
        if(maxx==threeRes){lis.add(3);}
        int[] answer = new int[lis.size()];
        
        for(int i=0;i<lis.size();i++){
            answer[i]=lis.get(i);
        }
        return answer;
    }
    
    public int cntAnswer(int[] answers,int[] stu){
        int oneL = stu.length;
        int cnt=0;
        for(int i=0;i<answers.length;i++){
            if(answers[i]==stu[i%oneL]){
                cnt+=1;
            }
        }
        return cnt;
    }
}