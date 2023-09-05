class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int solNum = numer1 * denom2 + numer2 * denom1;
        int solDe = denom2 * denom1;
        
        int max = 1;
        
        for(int i = 1; i<solNum+1 ; i++){
            if(solNum % i == 0 && solDe % i == 0){
                max = i;
            }
        }
        
        
        int[] answer = {solNum/max,solDe/max};
        return answer;
    }
}