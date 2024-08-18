package main.java.org.example.inflearn.sec05;

import java.util.*;

// 최소 힙
public class Inflearn5_10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> heap = new PriorityQueue<>();
        while(true) {
            int n = sc.nextInt();
            if (n == 0) {
                if(heap.isEmpty()) {
                    System.out.println(-1);
                    break;
                } else {
                    System.out.println(heap.poll());
                }

            } else if (n == -1) {
                break;
            } else {
                heap.add(n);
            }
        }
    }
}
