import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        Arrays.sort(array);
        int big = array[array.length - 1];
        
        int[] count = new int[big+1];
        
        for(int i = 0; i < array.length ; i++){
            count[array[i]]++;
        }
        int maxNum = count[0];
        for(int i = 1; i<count.length; i++ ){
            if(maxNum < count[i]){
                maxNum = count[i];
                answer = i;
            }else if(maxNum == count[i]){
                answer = -1;
            }
        }
        return answer;
    }
}