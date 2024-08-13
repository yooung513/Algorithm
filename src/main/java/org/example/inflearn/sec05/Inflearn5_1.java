package main.java.org.example.inflearn.sec05;

import java.util.*;
import java.io.*;

// 가장 큰 수
public class Inflearn5_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] data = br.readLine().split(" ");

        String[] nData = data[0].split("");
        int[] n = new int[nData.length];
        for (int i = 0; i < nData.length; i++) {
            n[i] = Integer.parseInt(nData[i]);
        }
        int m = Integer.parseInt(data[1]);

        Deque<Integer> dq = new ArrayDeque<>();
        dq.addLast(n[0]);
        for (int i = 1; i < n.length; i++) {
            if (m == 0) break;

            int tmp = n[i];
            if (dq.peekLast() != null && tmp > dq.peekLast()) {
                while ()
                dq.pollLast();
                dq.addLast(tmp);
                m--;
            } else {
                dq.addLast(tmp);
            }
        }
    }
}
