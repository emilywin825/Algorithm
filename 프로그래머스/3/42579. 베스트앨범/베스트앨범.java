import java.util.*; 

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        //수록 기준 : 많이 재생된 장르>많이 재생된 노래>고유 번호가 낮은 노래
        //장르 별로 가장 많이 재생된 노래를 두 개씩
// 1. genres, plays를 돌면서 Map으로 각 장르들의 총 재생 수를 계산한다 -> genresHapMap=[classic:1450], [pop:3100]
//동시에 노래의 재생횟수와 고유번호를 다른 map에 저장한다 -> playsOriginNum=[1:600], [4:2500], [0:500], [2:150], [3:800]
//동시에 같은 장르끼리 고유 번호를 저장한다. genresOriginNum=[clalssic:0,2,3], [pop:1,4]
// 2. map에서 entrySet()을 꺼내서 List로 받고, 내림차순 정렬(b-a)한다.  [pop:3100],[classic:1450]
// 3. List를 순서대로 돌면서 장르를 하나씩 꺼내고, genres를 돌며 일치하는 장르의 고유 번호를 찾는다. 
// 4. playsOriginNum 돌면서 재생횟수와 고유번호를 비교해 최종 저장될 2개의 노래를 결정한다 
//         int[] answer = {};
        List<Integer> answer = new ArrayList<>(); //answer : [4,1,3,0]
        Map<String, Integer> genresHapMap = new HashMap<>();
        Map<String, List<Integer>> genresOriginNum = new HashMap<>();

        for(int i=0;i<genres.length;i++){
            genresHapMap.put(genres[i],genresHapMap.getOrDefault(genres[i],0)+plays[i]);
            genresOriginNum.putIfAbsent(genres[i], new ArrayList<>());
            genresOriginNum.get(genres[i]).add(i);
        }

        List<Map.Entry<String, Integer>> sortGenres=new ArrayList<>(genresHapMap.entrySet());
        sortGenres.sort((a,b) -> b.getValue()-a.getValue());
        
        for(Map.Entry<String, Integer> targetGenre : sortGenres){
            List<Integer> list = genresOriginNum.get(targetGenre.getKey());
            Map<Integer, Integer> playsOriginNum = new HashMap<>();
            if(list.size()==1){
                answer.add(list.get(0));
            }else{
                for(Integer i : list){
                    playsOriginNum.put(i,plays[i]);
                }
                List<Map.Entry<Integer, Integer>> sortList = new ArrayList<>(playsOriginNum.entrySet());
                sortList.sort((a,b) -> b.getValue() - a.getValue());
                answer.add(sortList.get(0).getKey());
                answer.add(sortList.get(1).getKey());
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}