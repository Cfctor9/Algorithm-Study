class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        int sol1 = box[0]/n;
        int sol2 = box[1]/n;
        int sol3 = box[2]/n;
        
        answer = sol1*sol2*sol3;
        
        return answer;
    }
}