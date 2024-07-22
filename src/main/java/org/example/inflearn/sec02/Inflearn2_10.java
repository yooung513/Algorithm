package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

// 점수 계산
public class Inflearn2_10 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] result = br.readLine().split(" ");

        int total = 0;
        int tmp = 1;
        for (int i = 0; i < n; i++) {
            if (Integer.parseInt(result[i]) == 1) {
                total += tmp;
                tmp++;
            } else {
                tmp = 1;
            }
        }

        System.out.println(total);
    }
}
