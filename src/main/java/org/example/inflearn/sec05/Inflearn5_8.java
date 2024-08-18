package main.java.org.example.inflearn.sec05;

import java.io.*;
import java.util.*;

// 단어 찾기
public class Inflearn5_8 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> dict = new HashMap<>();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            dict.put(str, 1);
        }

        for (int i = 1; i < n; i++) {
            String str = br.readLine();
            if (dict.containsKey(str)) {
                dict.put(str, 0);
            }
        }

        for (String key : dict.keySet()) {
            if (dict.get(key) == 1) {
                System.out.println(key);
                break;
            }
        }
    }
}
