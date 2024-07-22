package main.java.org.example.chap01;

import java.util.Scanner;

public class Max3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("세 정수의 최댓값을 구합니다.");
        System.out.println("a의 값 : "); int a = sc.nextInt();
        System.out.println("b의 값 : "); int b = sc.nextInt();
        System.out.println("c의 값 : "); int c = sc.nextInt();

        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;

        System.out.println("최댓값은 " + max + "입니다.");
    }


    // Q1. 네 값의 최댓값을 구하는 max4 메소드
    static int max4 (int a, int b, int c, int d) {
        int maxVal = Math.max(a, b);
            maxVal = Math.max(maxVal, c);
            maxVal = Math.max(maxVal, d);

        return maxVal;
    }
}
