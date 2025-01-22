import java.util.*;
import java.io.*;

public class Programmers {
	public static int[] solution(int[] array, int[][] commands) {
		int[] res = new int[commands.length];
		
		for (int x = 0; x < commands.length; x++) {
			int i = commands[x][0];
			int j = commands[x][1];
			int k = commands[x][2];
			
			int[] copyArr = Arrays.copyOfRange(array, i-1, j);
			Arrays.sort(copyArr);
			res[x] = copyArr[k-1];
		}
		
		return res;
	}
}

/* Arrays.copyOfRange(array, startIdx, endIdx)
 * array : 복사할 원본 배열
 * startIdx : 복사 시작할 인덱스
 * endIdx : 복사를 끝낼 인덱스
 * 
 * 해당 문제에서는 ~번 째이므로 인덱스 값과 차이가 나니 주의해야 함
 * ex) 2번째 = 1번 인덱스
 */
