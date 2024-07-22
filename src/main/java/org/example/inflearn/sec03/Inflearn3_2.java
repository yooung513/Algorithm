package main.java.org.example.inflearn.sec03;

import java.util.*;

// 숫자만 추출
public class Inflearn3_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] strArr = sc.next().toCharArray();

        StringBuilder sb = new StringBuilder();
        for (char c : strArr) {
            if (48 <= c && c <= 57) {
                sb.append(c);
            }
        }

        int n = Integer.parseInt(sb.toString());
        Set<Integer> div = new HashSet<>();
        for (int i = 1; i < Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                div.add(i);
                div.add(n/i);
            }
        }

        System.out.println(n);
        System.out.println(div.size());

    }
}
