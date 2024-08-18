package main.java.org.example.inflearn.sec05;

import java.util.*;
import java.io.*;

// 응급실
public class Inflearn5_6 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<int[]> patient = new ArrayDeque<>();

        String[] nm = br.readLine().split(" ");
        String[] data = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        for (int i = 0; i < n; i++) {
            patient.add(new int[]{Integer.parseInt(data[i]), i});
        }
        Arrays.sort(data, Comparator.reverseOrder());
        int idx = 0;
        int cnt = 0;
        while (!patient.isEmpty()) {
            int[] tmp = patient.pollFirst();
            if (Integer.parseInt(data[idx]) == tmp[0]) {
                cnt++;
                idx++;
                if (tmp[1] == m) {
                    System.out.println(cnt);
                    break;
                }
            } else {
                patient.addLast(tmp);
            }
        }

    }
}
