package main.java.org.example.inflearn.sec05;

import java.io.*;
import java.util.*;

// Anagram
public class Inflearn5_9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str1 = br.readLine().split("");
        String[] str2 = br.readLine().split("");
        Map<String, Integer> dict = new HashMap<>();
        boolean flag = true;

        for (String s : str1) {
            if (dict.containsKey(s)) {
                dict.put(s, dict.get(s) + 1);
            } else {
                dict.put(s, 1);
            }
        }

        for (String s : str2) {
            if (dict.containsKey(s)) {
                dict.put(s, dict.get(s) - 1);
            } else {
                flag = false;
                break;
            }
        }

        for (int n : dict.values()) {
            if (n != 0) {
                flag = false;
                break;
            }
        }

        System.out.print(flag ? "YES" : "NO");
    }
}
