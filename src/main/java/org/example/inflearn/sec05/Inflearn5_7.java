package main.java.org.example.inflearn.sec05;

import java.io.*;
import java.util.*;

// 교육과정 설계
public class Inflearn5_7 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] order = br.readLine().split("");
        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            Deque<String> dq = new ArrayDeque<>(Arrays.asList(order));
            String[] data = br.readLine().split("");

            for (String str : data) {
                if (dq.isEmpty() ||
                    (dq.contains(str) && !dq.getFirst().equals(str))) break;

                if (dq.getFirst().equals(str)) {
                    dq.pollFirst();
                }
            }

            if (dq.isEmpty()) {
                System.out.printf("#%d YES\n", i);
            } else {
                System.out.printf("#%d NO\n", i);
            }
        }
    }
}
