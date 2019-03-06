public class Main {

    public static void main(String[] args) {
        Entry entry = new Entry();
        entry.enter("AB54321");
        entry.enter("UK32032");
        System.out.println(entry.leave());
        System.out.println(entry.leave());
    }
}
