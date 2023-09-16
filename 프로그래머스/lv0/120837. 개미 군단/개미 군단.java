class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        int boss = hp / 5;
        int sol =  (hp % 5) / 3;
        int sur = (hp % 5) % 3;
        answer = boss + sol + sur;
        
        
        return answer;
    }
}