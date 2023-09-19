import java.util.*;

class Solution {
    public int[] solution(String my_string) {

        my_string = my_string.replaceAll("[a-z]","");
        
        String[] sol = my_string.split("");
        int[] answer = new int[sol.length];
        
        for(int i = 0; i<sol.length; i++){
            answer[i] = Integer.parseInt(sol[i]);
        }
        Arrays.sort(answer);
        return answer;
    }
}