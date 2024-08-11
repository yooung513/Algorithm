package main.java.org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 마구간 정하기
public class Inflearn4_4 {
    static int[] stable;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nc = br.readLine().split(" ");
        int n = Integer.parseInt(nc[0]);
        int c = Integer.parseInt(nc[1]);

        stable = new int[n];
        for (int i = 0; i < n; i++) {
            stable[i] = Integer.parseInt(br.readLine());
        }
    }
}
