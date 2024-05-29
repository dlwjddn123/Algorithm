import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        Set<String> result = new HashSet<>();

        for (int i = 0; i < input.length(); i++) {
            StringBuffer sb = new StringBuffer();
            for (int j = i; j < input.length(); j++) {
                sb.append(input.charAt(j));
                result.add(sb.toString());
            }
        }

        System.out.println(result.size());
    }
}