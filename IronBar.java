import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class IronBar {
    public int solution(String arrangement) {
        int answer = 0;
        int level = 0;

        Stack<Character> s = new Stack<>();

        for (Character v : arrangement.toCharArray()) {
            if(s.empty()) { // start of bar
                s.push(v);
                continue;
            }
            if(')'== v && '(' == s.peek()){
                s.push(v);
                answer = answer + level; //snapshot
            } else if (')' == v){
                s.push(v);
                level--;
                answer++;
            } else if('(' == v){
                if(s.peek() == '(') {
                    level++;
                }
                s.push(v);
            }
        }


        return answer;
    }

    public static void main(String[] args){
        IronBar i = new IronBar();
        System.out.println(i.solution("()(((()())(())()))(())"));
    }
}
