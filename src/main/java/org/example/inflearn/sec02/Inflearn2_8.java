package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

// 뒤집은 소수
public class Inflearn2_8 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] num = br.readLine().split(" ");

        List<Integer> findNum = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int rev = reverse(num[i]);

            if (isPrime(rev)) {
                findNum.add(rev);
            }
        }

        for(int x : findNum) {
            System.out.print(x + " ");
        }
    }

    public static int reverse(String x) {
        // stringBuilder 사용 -> 문자열 뒤집은 후 숫자로 변환
        StringBuilder sb = new StringBuilder(x);
        sb.reverse();

        return Integer.parseInt(sb.toString());
    }

    public static boolean isPrime(int x) {
        if (x < 2) return false;

        for (int i = 2; i < x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
}
