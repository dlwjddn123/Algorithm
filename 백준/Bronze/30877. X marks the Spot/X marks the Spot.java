import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            sb.append(findCharAtX(input[0], input[1]));
        }
        System.out.println(sb.toString().toUpperCase());
    }

    public static char findCharAtX(String S, String T) {
        char result = ' ';
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == 'X' || S.charAt(i) == 'x') {
                result =  T.charAt(i);
                break;
            }
        }
        return result;
    }
}