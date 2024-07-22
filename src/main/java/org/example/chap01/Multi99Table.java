package main.java.org.example.chap01;

public class Multi99Table {
    public static void main(String[] args) {
        System.out.println("----- 곱셈표 -----");

        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                System.out.println(i + "*" + j + "=" + (i * j));
            }
            System.out.println();
        }
    }
}
