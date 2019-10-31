import java.util.*;
import java.io.*;

class Solution {

    public static void main(String args[]) {
        int n, first, min, worstDrop;
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        Integer[] values = new Integer[n];
        for (int i = 0; i < n; i++) {
            values[i] = in.nextInt();
        }

        List<Integer> falls = new LinkedList<>();
        int i = 0;
        while(i < n){
            first = values[i];
            min = -1;
            for(; i < n; i++){
                if(min < 0 || values[i] < min){
                    min = values[i];
                }
                if(values[i] > first){
                    break;
                }
            }
            if(min > -1){
                falls.add(first-min);
            }
        }
        Collections.sort(falls);
        worstDrop = (falls.size() > 0) ? falls.get(falls.size()-1) : 0;
        System.out.println((worstDrop > 0) ? "-" + worstDrop : worstDrop);
    }
}