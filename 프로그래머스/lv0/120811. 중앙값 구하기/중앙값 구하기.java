import java.util.*;
class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int num = array.length /2;
        
        int answer = 0;
        answer = array[num];
        return answer;
    }
}