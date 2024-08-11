package main.java.org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 증가수열 만들기
public class Inflearn4_9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tmp = br.readLine().split(" ");

        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            dq.add(Integer.parseInt(tmp[i]));
        }

        StringBuilder sb = new StringBuilder();
        int lastVal = 0;
        while (!dq.isEmpty()) {
            int l = dq.pollFirst();
            int r = !dq.isEmpty() ? dq.pollLast() : 0;

            if(l > lastVal && r > lastVal) {
                if (l < r) {
                    lastVal = l;
                    sb.append("L");
                    dq.addLast(r);
                } else if (r < l){
                    lastVal = r;
                    sb.append("R");
                    dq.addFirst(l);
                }
            } else if (l > lastVal) {
                lastVal = l;
                sb.append("L");
                dq.addLast(r);
            } else if (r > lastVal) {
                lastVal = r;
                sb.append("R");
                dq.addFirst(l);
            } else {
                break;
            }

        }

        System.out.println(sb.length());
        System.out.println(sb);
    }
}
