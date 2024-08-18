package main.java.org.example.inflearn.sec05;

import java.util.*;
import java.io.*;

// 가장 큰 수
// 강의 참고
public class Inflearn5_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputData = br.readLine().split(" ");
        String[] data = inputData[0].split("");
        int n = Integer.parseInt(inputData[1]);

        Deque<Integer> stack = new ArrayDeque<>();
        for (String s : data) {
            int x = Integer.parseInt(s);

            while(!stack.isEmpty() && n > 0 && stack.getLast() < x) {
                stack.pollLast();
                n--;
            }
            stack.addLast(x);
        }

        if (n != 0) {
            for (int i = 0; i < n; i++) {
                stack.pollLast();
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int x : stack) {
            sb.append(x);
        }
        System.out.println(sb);
    }
}
