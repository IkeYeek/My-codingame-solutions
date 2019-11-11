import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        String lines[] = new String[N];
        if (in.hasNextLine()) {
            in.nextLine();
        }
        for (int i = 0; i < N; i++) {
            lines[i] = in.nextLine();
        }

        for(int i = 0; i < N; i++) {
            String line = lines[i];
            int opening_parenthesis = line.indexOf('(');
            int closing_parenthesis = line.indexOf(')');
            if(opening_parenthesis >= closing_parenthesis && closing_parenthesis >= 0) {
                String sub_string = line.subString(opening_parenthesis, closing_parenthesis);
                String [] available_options = sub_string.split('|');
                System.out.println(available_options[i % available_options.length]);
            }
        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        
        System.out.println("42");
    }
}