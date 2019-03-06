import java.util.LinkedList;
import java.util.Queue;

public class Entry {
    private Queue<String> _q = new LinkedList<String>();

    public void enter(String passportNumber) {
        _q.add(passportNumber);
    }

    public String leave() {
        Object o = null;
        try { // null should be returned.
            o = _q.remove();
        } catch (java.util.NoSuchElementException e) {
            return null;
        }
        return o.toString();
    }

    public static void main(String[] args) {
        Entry entry = new Entry();
        entry.enter("AB54321");
        entry.enter("UK32032");
        System.out.println(entry.leave());
        System.out.println(entry.leave());
    }
}