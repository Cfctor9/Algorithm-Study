class Solution {
    public String solution(int age) {
        
        StringBuilder answer = new StringBuilder();
        while(age>0){
            int i = age%10;
            char result = (char)(i + 'a');
            answer.insert(0,result);
            age /= 10;
        }
        return answer.toString();
    }
}