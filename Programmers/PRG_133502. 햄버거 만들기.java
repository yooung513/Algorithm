import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        
        List<Integer> list = new ArrayList<>();
        for (int in : ingredient) {
            list.add(in);                   // 1. 재료 입력
            
            while(list.size() >= 4) {       // 2. 재료가 4개 이상인 경우 확인
                int n = list.size();        // 3. 전체 재료의 크기
                
                if(!(list.get(n-1) == 1 &&
                     list.get(n-2) == 3 &&
                     list.get(n-3) == 2 &&
                     list.get(n-4) == 1
                )) break;                    // 4. 재료의 순서가 다르면 반복문 종료
            
                // 5. 재료의 순서가 일치해 햄버거 완성 = list에서 제거
                for(int i = 1; i <= 4; i++) {
                    list.remove(n-i);
                }
                answer++;
            }
            
        }
        
        return answer;
    }
}
