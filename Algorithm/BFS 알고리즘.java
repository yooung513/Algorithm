/*
  BFS 알고리즘 (Breadth-First Search, 너비 우선 탐색 알고리즘)
  > 최단 경로 탐색, 임의의 경로 존재 탐색

  - 방문 노드 체크
  - Queue 사용
*/

public class Main {
	private static int[][] node;
	private static boolean[] visited;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		
		node = new int[n + 1][n + 1];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			node[s][e] = 1;
			node[e][s] = 1;
		}
		
		visited = new boolean[n + 1];
		bfs(v);
	}
	
	public static void bfs(int v) {
		Deque<Integer> dq = new ArrayDeque<>();
		dq.addLast(v);
		visited[v] = true;
		
		while(!dq.isEmpty()) {
			int x = dq.pollFirst();
			System.out.print(x + " ");
			
			for (int i = 0; i < node.length; i++) {
				if (!visited[i] && node[x][i] == 1) {
					visited[i] = true;
					dq.addLast(i);
				}
			}
		}
	}
}
