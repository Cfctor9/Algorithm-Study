class Solution {
    public int solution(int[] sides) {

        int max = -1;
        int maxNum = 0;
        int sol =0;
        for(int i = 0; i<3 ; i++){
            if(sides[i]>max) {
                max = sides[i];
                maxNum = i;
            }            
        }
        for(int i = 0; i<3 ; i++){
            if(i != maxNum) {
                sol += sides[i];
            }            
        }
        
        if(max<sol){
            return 1;
        }else{
            return 2;
        }
        

    }
}