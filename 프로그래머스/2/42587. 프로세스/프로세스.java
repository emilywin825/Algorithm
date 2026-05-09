//큐 : fifo
//run = que.pollFirst(); : 맨 앞에꺼 실행
//list를 돌면서 뒤에 값들이랑 쭉 비교
    //내가 제일 크고 && run[1]==location return answer;
    //나보다 큰 값이 있으면, que 맨 뒤로 다시 이동 && answer+=1;
import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        Deque<int[]> que = new LinkedList<>();
        int answer = 0;

        for(int i=0;i<priorities.length;i++){
            int[] arr = new int[2];
            arr[0]=priorities[i]; //값
            arr[1]=i;//인덱스
            que.addLast(arr);
        }

        while(que.size()>0){
            int[] run=que.pollFirst();
            boolean finish=true;
            for(int[] wait : que){
                if(run[0]<wait[0]){
                    que.offerLast(run);
                    finish=false;
                    break;
                }
            } 
            if(finish==true) {
                answer+=1;
                if(run[1]==location) return answer;
            }
        }
        return answer+=1;
    }
}