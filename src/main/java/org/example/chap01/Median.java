package main.java.org.example.chap01;

import java.util.Arrays;
import java.util.Scanner;

public class Median {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("a의 값 : "); int a = sc.nextInt();
        System.out.println("b의 값 : "); int b = sc.nextInt();
        System.out.println("c의 값 : "); int c = sc.nextInt();

        System.out.println("세 정수의 중앙 값은 " + med(a, b, c) + "입니다.");
    }

    static int med(int a, int b, int c) {
        // 나의 풀이
        int[] med = new int[3];
        med[0] = a;
        med[1] = b;
        med[2] = c;

        Arrays.sort(med);

        return med[1];
    }

    static int solve(int a, int b, int c) {
        if (a >= b)
            if (b >= c)
                return b;
            else if (a <= c)
                return a;
            else
                return c;
        else if (a > c)
            return a;
        else if (b > c)
            return c;
        else
            return b;
    }
}
