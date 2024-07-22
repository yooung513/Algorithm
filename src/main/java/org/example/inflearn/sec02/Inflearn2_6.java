package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

// 자릿수의 합
public class Inflearn2_6 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] num = br.readLine().split(" ");

        int origin = 0;
        int total = 0;
        for (int i = 0; i < n; i++) {
            int tmpOrg = Integer.parseInt(num[i]);
            int tmpTot = digit_sum(tmpOrg);

            if (tmpTot > total) {
                origin = tmpOrg;
                total = tmpTot;
            }
        }

        System.out.print(origin);
    }

    public static int digit_sum(int x) {
        int val = 0;
        while (x > 0) {
            val += x % 10;
            x /= 10;
        }
        return val;
    }
}
