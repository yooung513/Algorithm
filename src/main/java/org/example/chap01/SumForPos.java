package main.java.org.example.chap01;

import java.util.Scanner;

public class SumForPos {
    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n;
//
//        do {
//            System.out.println("n의 값 :");
//            n = sc.nextInt();
//        } while (n <= 0);           // n이 음수일 때 반복 = 양수가 나올때까지 수를 정확하게 입력 받음
//
//        int sum = 0;
//        for (int i = 1; i <= n; i++) {
//            sum += i;
//        }
//
//        System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
        SolveQ10();
    }


    // Q10. b-a를 출력하는 프로그램
    static void SolveQ10() {
        Scanner sc = new Scanner(System.in);
        int a, b;

        do {
            System.out.println("a의 값 : ");
            a = sc.nextInt();

            System.out.println("b의 값 : ");
            b = sc.nextInt();
        } while (a > b);

        System.out.println("b - a의 값은 " + (b - a) + "입니다.");
    }


    // 드모르간 법칙
    // ex ) 2자리의 양수로 입력 값 제한
    static void Digits() {
        Scanner sc = new Scanner(System.in);
        int no;

        do {
            System.out.println("입력 :");
            no = sc.nextInt();
        } while(no < 10 || no > 99);

        do {
            System.out.println("입력 :");
            no = sc.nextInt();
        } while (!(10 <= no && no <= 99));
    }
}
