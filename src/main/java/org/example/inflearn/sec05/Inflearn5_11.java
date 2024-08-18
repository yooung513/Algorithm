package main.java.org.example.inflearn.sec05;

import java.util.*;

// 최대 힙
public class Inflearn5_11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> heap = new PriorityQueue<>();
        while (true) {
            int n = sc.nextInt() * -1;
            if (n == 1) break;
            if (n == 0) {
                if (heap.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(heap.poll() * -1);
                }
            } else {
                heap.add(n);
            }
        }
    }
}
