import java.awt.*;
import java.util.*;
import java.io.*;
import java.util.List;

/**
 * Don't let the machines win. You are humanity's last hope...
 **/
class Player {

    public static void main(String args[]) throws IOException {
        Scanner in = new Scanner(System.in);
       // Scanner in = new Scanner(new FileReader("content.txt"));
        int width = in.nextInt(); // the number of cells on the X axis
        int height = in.nextInt(); // the number of cells on the Y axis
        if (in.hasNextLine()) {
            in.nextLine();
        }
        Map<Point, Character> cases = new HashMap<>();
        for (int i = 0; i < height; i++) {
            String line = in.nextLine(); // width characters, each either 0 or .
            System.err.println(line);
            for(int j = 0; j < width; j++){
                cases.put(new Point(j, i), line.charAt(j));
            }
        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");

        List<Point> cells = getCells(cases);
        Map<Point, Point[]> neighboorHood = new HashMap<>();
        cells.forEach(e -> {
            Point[] neightbors = {new Point(-1, -1), new Point(-1, -1)};
            boolean ended = false;
            for(int i = e.x+1; i < width && !ended; i++){
                if(cells.contains(new Point(i, e.y))){
                    neightbors[0] = new Point(i, e.y);
                    ended = true;
                }
            }
            ended = false;
            for(int j = e.y+1; j < height && !ended; j++){
                if(cells.contains(new Point(e.x, j))){
                    neightbors[1] = new Point(e.x, j);
                    ended = true;
                }
            }
            neighboorHood.put(e, neightbors);
        });

        // Three coordinates: a node, its right neighbor, its bottom neighbor
        StringBuilder answer = new StringBuilder();
        neighboorHood.forEach((e, v) -> {
            answer.append(e.x).append(" ").append(e.y).append(" ").append(v[0].x).append(" ").append(v[0].y).append(" ").append(v[1].x).append(" ").append(v[1].y).append("\n");
        });
        System.out.println(answer.toString());
    }

    private static List<Point> getCells(Map<Point, Character> cases){
        List<Point> cells = new ArrayList<>();

        cases.forEach((e, v) -> {
            if(v == '0') {
                cells.add(e);
            }
        });

        return cells;
    }
}