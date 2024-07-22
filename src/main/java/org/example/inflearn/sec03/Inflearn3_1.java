package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 회문 문자열 검사
public class Inflearn3_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i = 1; i <= n; i++) {
            String result = "YES";
            String tmp = br.readLine().toUpperCase();
            int len = tmp.length();

            for (int j = 0; j < len / 2; j++) {
                char c1 = tmp.charAt(j);
                char c2 = tmp.charAt(len -1 - j);

                if (c1 != c2) {
                    result = "NO";
                }
            }

            System.out.println("#"+ i + " " + result);
        }
    }
}
