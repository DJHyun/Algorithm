//www.programmers.co.kr
package 프로그래머스;

import java.util.Deque;
import java.util.LinkedList;

public class 카카오프렌즈컬러링북 {

	static int[][] visited;
	static int[][] arr;
	int[] dx, dy;
	static int check_m, check_n;

	public static boolean check(int x, int y, int a, int b) {
		if (a < 0 || a > check_m - 1)
			return false;
		if (b < 0 || b > check_n - 1)
			return false;
		if (visited[a][b] == 1)
			return false;
		if (arr[x][y] != arr[a][b])
			return false;
		if (arr[a][b] == 0)return false;
		return true;
	}

	public int bfs(int a, int b) {
		Deque<Integer> que = new LinkedList<>();
		que.add(a * 1000 + b);
		visited[a][b] = 1;
		int count = 1;

		while (!que.isEmpty()) {
			int t = que.pollFirst();
			for (int i = 0; i < 4; ++i) {
				int x = t / 1000 + dx[i];
				int y = t % 1000 + dy[i];
				if (check(a, b, x, y)) {
					que.add(x * 1000 + y);
					count++;
					visited[x][y] = 1;
				}
			}
		}
		return count;
	}

	public int[] solution(int m, int n, int[][] picture) {
		int numberOfArea = 0;
		int maxSizeOfOneArea = 0;

		visited = new int[m][n];
		dx = new int[] { 0, 0, 1, -1 };
		dy = new int[] { 1, -1, 0, 0 };
		check_m = m;
		check_n = n;
		arr = picture;


		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				if (picture[i][j] != 0 && visited[i][j] != 1) {
					int check = bfs(i, j);
					numberOfArea++;
					if (check > maxSizeOfOneArea) {
						maxSizeOfOneArea = check;
					}
				}
			}
		}

		int[] answer = new int[2];
		answer[0] = numberOfArea;
		answer[1] = maxSizeOfOneArea;
		return answer;
	}

	public static void main(String[] args) {
		카카오프렌즈컬러링북 ch = new 카카오프렌즈컬러링북();
		ch.solution(6, 4, new int[][] { { 1, 1, 1, 0 }, { 1, 2, 2, 0 }, { 1, 0, 0, 1 }, { 0, 0, 0, 1 }, { 0, 0, 0, 3 },
				{ 0, 0, 0, 3 } });

	}
}
