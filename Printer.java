import java.util.*;
import java.util.stream.Collectors;

public class Printer {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int target = priorities[location];

        LinkedList l = new LinkedList();
        l.addAll(Arrays.stream(priorities).boxed().collect(Collectors.toList()));

        ArrayList<Integer> al = new ArrayList();
        al.addAll(l);
        Collections.sort(al);
        Collections.reverse(al);


        for (Integer p : al) {
            while(true){
                int t = (int)l.poll();
                if(t != p){
                    l.offer(t);
                } else {
                    if(target == t) return ++answer;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Printer p = new Printer();

        p.solution( new int[]{2, 1, 3, 2}, 2);
    }
}
