package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

// 소수 (에라토스테네스 체)
public class Inflearn2_7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] prime = new int[n + 1];
        prime[0] = 1;
        prime[1] = 1;
        for (int i = 2; i < n + 1; i++) {
            for (int j = i * 2; j < n + 1; j += i) {
                prime[j] = 1;
            }
        }

        int cnt = 0;
        for (int x : prime) {
            if (x == 0) {
                cnt++;
            }
        }

        System.out.print(cnt);
    }
}
