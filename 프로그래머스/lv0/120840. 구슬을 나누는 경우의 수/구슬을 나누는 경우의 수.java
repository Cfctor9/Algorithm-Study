class Solution {
    public int combin(int n , int m) {
        if(m==0 || n == m){
            return 1;
        }else{
            return combin(n-1,m) + combin(n-1,m-1);
        }        
    }
    public int solution(int balls, int share) {
        int answer = 0;
        answer = combin(balls,share);
        return answer;
    }
}