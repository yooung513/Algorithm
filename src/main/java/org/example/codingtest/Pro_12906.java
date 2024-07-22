package main.java.org.example.codingtest;

import java.util.*;

// 같은 숫자는 싫어
public class Pro_12906 {
    public static void main(String[] args) {
        int[] ans = Solution(new int[] {1,1,3,3,0,1,1});
        System.out.println(Arrays.toString(ans));
    }

    public static int[] Solution(int[] arr) {
        Stack<Integer> chk = new Stack<>();
        for (int a : arr) {
            if (chk.empty()) {
                chk.push(a);
            } else {
                if (chk.peek() != a) {
                    chk.push(a);
                }
            }
        }

        int[] answer = new int[chk.size()];
        for (int i = 0; i < chk.size(); i++) {
            answer[i] = chk.get(i);
        }

        return answer;
    }
}
