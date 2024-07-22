package main.java.org.example.inflearn.sec02;

import java.util.*;

// 정다면체
public class Inflearn2_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        Map<Integer, Integer> dice = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int val = i + j;

                if (dice.containsKey(val)) {
                    dice.put(val, dice.get(val) + 1);
                } else {
                    dice.put(val, 1);
                }
            }
        }

        int findMax = 0;
        for (int x : dice.values()) {
            if (findMax < x) {
                findMax = x;
            }
        }

        for (int x : dice.keySet()) {
            if (dice.get(x) == findMax) {
                System.out.print(x + " ");
            }
        }
    }
}
