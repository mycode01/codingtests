public class Pelin {

    public static void main(String[] args) {



        String inputString = "abcde";
        solution(inputString);
        System.out.println(solution(inputString));

    }

    private static int solution(String inputString) {
        int i, len = inputString.length();
        for(i=0;i<len;i++)
            if(isPalindrome(inputString.substring(i)))
                return i + len;
        return len << 1;
    }

    private static boolean isPalindrome(String str) {
        int i, len = str.length(), half = len >>> 1;
        for(i=0;i<=half;i++)
            if(str.charAt(i) != str.charAt(len-i-1))
                return false;
        return true;
    }
}
