package main.java.org.example.inflearn;

import java.io.*;

public class Check {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] test_1 = br.readLine().split(" ");
        String[] test_2 = br.readLine().split(" ");

        for (int i = 0; i < test_1.length; i++) {
            if ( !test_1[i].equals(test_2[i]) ) {
                System.out.println(false);
                System.out.println(test_1[i]);
                System.out.println(test_2[i]);
                break;
            }
        }
        System.out.println(true);

    }
}
