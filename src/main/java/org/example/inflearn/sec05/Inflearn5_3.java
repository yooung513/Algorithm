package main.java.org.example.inflearn.sec05;

import java.io.*;
import java.util.*;

// 후위 표기식 만들기
// 참고
public class Inflearn5_3 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] data = br.readLine().split("");
        Deque<String> stack = new ArrayDeque<>();
        StringBuilder ans = new StringBuilder();
        for (String s : data) {
            if ("(".equals(s)) {
                stack.addLast(s);
            } else if ("*".equals(s) || "/".equals(s)) {
                while (!stack.isEmpty() &&
                        (stack.getLast().equals("*") ||
                        stack.getLast().equals("/")) ) {
                    ans.append(stack.pollLast());
                }
                stack.addLast(s);
            } else if ("+".equals(s) || "-".equals(s)) {
                while (!stack.isEmpty() && !stack.getLast().equals("(")) {
                    ans.append(stack.pollLast());
                }
                stack.addLast(s);
            } else if (")".equals(s)) {
                while (!stack.isEmpty() && !stack.getLast().equals("(")) {
                    ans.append(stack.pollLast());
                }
                stack.pollLast();
            } else {
                ans.append(s);
            }
        }

        while (!stack.isEmpty()) {
            ans.append(stack.pollLast());
        }

        System.out.println(ans);
    }
}
