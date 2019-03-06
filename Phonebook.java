import java.util.HashMap;

class Phonebook {
    public boolean solution(String[] phone_book) {
        for (String v : phone_book) {
            for(String iv : phone_book){
                if(iv.equals(v))continue;
                if(v.startsWith(iv)){
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Phonebook p = new Phonebook();
        String[] n1 = {"119", "97674223", "1195524421"};
        System.out.println(p.solution(n1));
        String[] n2 = {"123", "456", "789"};
        System.out.println(p.solution(n2));
        String[] n3 = {"12", "123", "1235", "567", "88"};
        System.out.println(p.solution(n3));
    }
}