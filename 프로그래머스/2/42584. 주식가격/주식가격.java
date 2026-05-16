import java.util.*;
//나보다 뒤에 있는 값들 중에 나보다 작은게 있는지
//나보다 뒤에 있는 값들의 개수 : prices.length-(i+1)
//O(n)
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                answer[i]++;

                if (prices[j] < prices[i]) {
                    break;
                }
            }
        }

        return answer;
    }
}