import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant); Arrays.sort(completion);

        String answer = "";

        try{
            for (int i = 0 ; i< participant.length; i++){
                if (!participant[i].equals(completion[i])){
                    answer = participant[i];
                    break;
                }
            }
        } catch(Exception e)
        {
            answer = participant[participant.length - 1];
        }

        return answer;
    }
}

public class Completion{
    public static void main(String[] args){
        Solution s = new Solution();

        String[] p1 = {"leo", "kiki", "eden"};
        String[] c1 = {"kiki", "eden"};
        System.out.println(s.solution(p1,c1));
        String[] p2 = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] c2 = {"josipa", "filipa", "marina", "nikola"};
        System.out.println(s.solution(p2,c2));
        String[] p3 = {"mislav", "stanko", "mislav", "ana"};
        String[] c3 = {"stanko", "ana", "mislav"};
        System.out.println(s.solution(p3,c3));
    }
}