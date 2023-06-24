import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.ListIterator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] string = br.readLine().toCharArray();
        int N = Integer.parseInt(br.readLine());
        LinkedList<Character> ll = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : string) {
            ll.add(c);
        }
        ListIterator<Character> iter = ll.listIterator();

        while(iter.hasNext()) {
            iter.next();
        }

        for (int i = 0; i < N; i++) {
            String command = br.readLine();
            if (command.charAt(0) == 'P'){
                iter.add(command.charAt(2));
            } else if (command.charAt(0) == 'L') {
                if (iter.hasPrevious()) {
                    iter.previous();
                }
            } else if (command.charAt(0) == 'D') {
                if (iter.hasNext()) {
                    iter.next();
                }
            } else if (command.charAt(0) == 'B') {
                if (iter.hasPrevious()) {
                    iter.previous();
                    iter.remove();
                }
            }
        }
        for (char c : ll) {
            sb.append(c);
        }
        System.out.println(sb);
    }
}
