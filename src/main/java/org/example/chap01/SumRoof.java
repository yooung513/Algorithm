package main.java.org.example.chap01;

import java.util.Scanner;

public class SumRoof {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("정수 n의 값 :"); int n = sc.nextInt();
        System.out.println("1부터 n까지의 합은 " + Solve(n) + "입니다.");
    }

    private static int Solve(int n) {
        int sum = 0;
        int i = 1;

        while (i <= n) {
            sum += i;
            i++;
        }

        return sum;
    }

    static int sumNum1(int n) {
        return n * (n+1) / 2;
    }

    static int sumNum2(int n) {
        int res = 0;

        for (int i = 1; i <= n; i++) {
            res += i;
        }

        return res;
    }

}
