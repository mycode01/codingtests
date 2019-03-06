import java.util.*;
import java.text.SimpleDateFormat;

public class MovieNight {
    public static Boolean canViewAll(Collection<Movie> movies) {
        long ep = 0;
        for (Movie m: movies) {
            if(m.getStart().getTime() > m.getEnd().getTime())
                return false;
            if(m.getStart().getTime() <= ep)
                return false;
            ep = m.getEnd().getTime();
        }
        return true;
    }


    public static void main(String[] args) throws Exception {
        SimpleDateFormat sdf = new SimpleDateFormat("y-M-d H:m");

        ArrayList<Movie> movies = new ArrayList<Movie>();
        movies.add(new Movie(sdf.parse("2015-01-01 20:00"), sdf.parse("2015-01-01 21:30")));
        movies.add(new Movie(sdf.parse("2015-01-01 23:10"), sdf.parse("2015-01-01 23:30")));
        movies.add(new Movie(sdf.parse("2015-01-01 21:30"), sdf.parse("2015-01-01 23:00")));

        System.out.println(MovieNight.canViewAll(movies));
    }
}