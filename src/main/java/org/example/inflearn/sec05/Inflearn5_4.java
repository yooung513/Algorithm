package main.java.org.example.inflearn.sec05;

import java.io.*;
import java.util.*;

// 후위식 연산
// 참고
public class Inflearn5_4 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] data = br.readLine().split("");
        Deque<Integer> stack = new ArrayDeque<>();
        for (String s : data) {
            if ("+".equals(s) || "-".equals(s) ||
                "*".equals(s) || "/".equals(s)) {
                int n1 = stack.pollLast();
                int n2 = stack.pollLast();

                int x = 0;
                switch (s) {
                    case "+" : x = n2 + n1; break;
                    case "-" : x = n2 - n1; break;
                    case "*" : x = n2 * n1; break;
                    case "/" : x = n2 / n1; break;
                }
                stack.addLast(x);

            } else {
                stack.addLast(Integer.parseInt(s));
            }
        }

        System.out.println(stack.getFirst());
    }
}
