/*
  DFS (Depth-First Search) : 깊이 우선 탐색
  > 그래프 완전 탐색 시 사용
    = 경로의 존재 여부 판단
/*

// 예시 > https://www.acmicpc.net/problem/1260

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
		dfs(v);
	}
	
	public static void dfs(int v) {
		visited[v] = true;
		System.out.print(v + " ");
		
		for(int i = 0; i < node.length; i++) {
			if (!visited[i] && node[v][i] == 1) {
				dfs(i);
			}
		}
	}
}
