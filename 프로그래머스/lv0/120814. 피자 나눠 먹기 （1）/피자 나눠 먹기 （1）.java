class Solution {
    public int solution(int n) {
        int num1 = n / 7;
        int num2 = n % 7;
        
        if(num2 > 0) {num1++;}

        return num1;
    }
}