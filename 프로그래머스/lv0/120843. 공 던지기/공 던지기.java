class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        int sol = 2*(k-1) % numbers.length; 
        answer = numbers[sol];
        return answer;
    }
}