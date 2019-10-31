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
        String expression = in.next();

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        List<Character> openers = new ArrayList<>(Arrays.asList('{', '[', '('));
        List<Character> closers = new ArrayList<>(Arrays.asList('}', ']', ')'));
        List<Character> operands = new ArrayList<>();
        boolean valid = true;
        for(char c : expression.toCharArray()) {
            if(valid) {
                if(openers.contains(c)) {
                    operands.add(c);
                } else if(closers.contains(c)) {
                     if(operands.size() > 0) {
                        switch(c) {
                            case '}':
                                if(operands.get(operands.size() - 1) != '{'){
                                 valid = false;   
                                } else {
                                    operands.remove(operands.size() - 1);   
                                }
                                break;
                            case ']':
                                if(operands.get(operands.size() - 1) != '['){
                                 valid = false;   
                                } else {
                                    operands.remove(operands.size() - 1);   
                                }
                                break;
                            case ')':
                                if(operands.get(operands.size() - 1) != '('){
                                 valid = false;   
                                } else {
                                    operands.remove(operands.size() - 1);   
                                }
                                break;
                        }
                     } else {
                        valid = false;   
                     }
                }
            }
        }
        System.err.println("valid ? " + valid);
        System.out.println((valid && operands.size() == 0) ? "true" : "false");
    }
}