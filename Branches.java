import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public class Branches {
    public static int count(int[] tree) {
        // base, element has parents address, so remove duplicated value is branches(include root)
        Set s = Arrays.stream(tree).boxed().collect(Collectors.toSet());
        s.remove(-1); // remove root
        return s.size();
    }

    public static void main(String[] args) {
        System.out.println(Branches.count(new int[] { 1, 3, 1, -1, 3 }));
    }
}