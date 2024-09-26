import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public int[] solution(int[] answers) {
        int[][] pattern = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5,} 
        }; //패턴 정리
        
        int[] result = new int[3]; // 3명 동점일수 있으니까
        
        for(int i=0;i< answers.length;i++){
            for(int j=0;j<pattern.length ;j++){
                if(answers[i] == pattern[j][i%pattern[j].length]){
                    result[j]++;
                }
            }
        }
        
        int maxScore = Arrays.stream(result).max().getAsInt();
        
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<result.length;i++){
            if(result[i] == maxScore){
                answer.add(i+1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
        
    }
}