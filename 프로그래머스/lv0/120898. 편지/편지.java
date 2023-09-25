class Solution {
    public int solution(String message) {
        int answer = 0;
        String[] array = message.split("");
        answer = array.length * 2;
        return answer;
    }
}