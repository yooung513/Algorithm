package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

// 주사위 게임
public class Inflearn2_9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Integer[] price = new Integer[n];
        for (int i = 0; i < n; i++) {
            TreeMap<Integer, Integer> dice = new TreeMap<>();
            String[] strDice = br.readLine().split(" ");
            for (int j = 0; j < 3; j++) {
                int tmp = Integer.parseInt(strDice[j]);

                if (dice.containsKey(tmp)) {
                    dice.put(tmp, dice.get(tmp) + 1);
                } else {
                    dice.put(tmp, 1);
                }
            }

            if (dice.size() == 3) {
                price[i] = dice.lastKey() * 100;
            } else if (dice.size() == 2) {
                for (int x : dice.keySet()) {
                    if (dice.get(x) == 2) {
                        price[i] = 1000 + x * 100;
                        break;
                    }
                }
            } else {
                price[i] = 10000 + dice.lastKey() * 1000;
            }
        }

        Arrays.sort(price, Collections.reverseOrder());
        System.out.print(price[0]);
    }
}
