import java.util.*;

// 방문한 티켓을 boolean[] visited 배열로 체크하고, 
// 사용한 티켓은 true로 표시, 탐색 종료 후 다시 false로 돌려야 합니다.

class Solution {
    List<String> answer=null;
    
    public String[] solution(String[][] tickets) {   
        int[] visited = new int[tickets.length];
        List<String> answerList=new ArrayList<>();
        
        Arrays.sort(tickets,Comparator.comparing((String[] a)->a[0])
                   .thenComparing((String[] a)->a[1]));

        answerList.add("ICN");
        dfs(tickets,"ICN",visited,answerList);
        
        return answer.toArray(new String[0]);
    }
    
    public void dfs(String[][] tickets, String target, int[] visited, List<String> answerList){
        if(answerList.size()==tickets.length+1){
            if(answer==null){
                answer = new ArrayList<>(answerList);
            }
            return;
        }
        for(int i=0;i<tickets.length;i++){
            if(tickets[i][0].equals(target) && visited[i]==0){
                visited[i]=1;
                answerList.add(tickets[i][1]);
                dfs(tickets,tickets[i][1],visited,answerList);
                answerList.remove(answerList.size()-1);
                visited[i]=0;
            }
        }
    }
}