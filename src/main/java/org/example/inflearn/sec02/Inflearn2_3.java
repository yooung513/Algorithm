package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

public class Inflearn2_3 {

    // K번째 큰 수
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]);
        int k = Integer.parseInt(firstLine[1]);

        String[] secondLine = br.readLine().split(" ");
        int[] card = new int[n];
        for (int i = 0; i < n; i++) {
            card[i] = Integer.parseInt(secondLine[i]);
        }

        List<Integer> val = new ArrayList<>();
        for (int x = 0; x < n; x++) {
            for (int y = x+1; y < n; y++) {
                for (int z = y+1; z < n; z++) {
                    int total = card[x] + card[y] + card[z];
                    if (!val.contains(total)) {
                        val.add(total);
                    }
                }
            }
        }

        Collections.sort(val, Comparator.reverseOrder());
        System.out.print(val.get(k-1));

    }
}
