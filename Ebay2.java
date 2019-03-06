import java.util.ArrayList;
import java.util.List;

class Ebay2 {
    public long[] solution(long n) {
        long[] answer = {};
        List primes = getPrimes(n);

        while(true){
            int i = 0;
            long a = (long)primes.get(i);

            for (Object x: primes) {
                if ((long)x == a) continue;
                if (n == (long)x * a){
                    answer[0] = a;
                    answer[1] = (long)x;
                    break;
                }
            }
            if(answer.length > 0) break;
            i++;
        }

        return answer;
    }
    public List getPrimes(long n){
        List ret = new ArrayList();
        List<Boolean> a = new ArrayList<>();
        for(int i = 2; i< n; i++){
            a.add(true);
        }

        int to = (int)Math.sqrt(n);
        for(int i =2;i<to;i++){
            if(a.get(i) == true){
                for(int j = i;j*i<n;j++)
                    a.set(i*j, false);
            }
        }

        for(int i =2;i<n;i++){
            if(a.get(i))
                ret.add(i);
        }
        return ret;
    }


    public static void main(String[] args) {
        Ebay2 e = new Ebay2();
        System.out.println(e.solution(6));
    }
}
