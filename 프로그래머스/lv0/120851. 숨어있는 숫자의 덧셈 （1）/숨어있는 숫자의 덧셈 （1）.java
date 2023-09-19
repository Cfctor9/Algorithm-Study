class Solution {
    public int solution(String my_string) {
        int answer = 0;
        my_string = my_string.replaceAll("[a-z,A-Z]","");
        String[] sol = my_string.split("");
        int[] num = new int[sol.length];
        
        for(int i = 0; i<sol.length;i++){
            num[i] = Integer.parseInt(sol[i]);
        }
        for(int i = 0; i<num.length;i++){
          answer += num[i];
        }
        return answer;
    }
}