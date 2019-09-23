
//baekjoon source = "https://www.acmicpc.net/problem/16234"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 인구이동_16234 {
	static int[][] arr;
	static int n, L, R;
	static int[][] visited;
	static int[] dx = new int[] { 0, 0, 1, -1 };
	static int[] dy = new int[] { 1, -1, 0, 0 };
	static boolean flag = true;

	public static boolean check(int c) {
		int x = c / 100;
		int y = c % 100;
		if (x < 0 || x > n - 1)
			return false;
		if (y < 0 || y > n - 1)
			return false;
		if (visited[x][y] == 1)
			return false;
		return true;
	}

	public static void solution(int x) {
		Queue<Integer> q = new LinkedList<>();
		Queue<Integer> newq = new LinkedList<Integer>();
		q.add(x);
		newq.add(x);
		visited[x / 100][x % 100] = 1;
		int cnt = 1, sum = arr[x / 100][x % 100];
		while (!q.isEmpty()) {
			int t = q.poll();
			for (int i = 0; i < 4; i++) {
				int tx = t / 100 + dx[i];
				int ty = t % 100 + dy[i];
				if (check(tx * 100 + ty)) {
					if (L <= Math.abs(arr[t / 100][t % 100] - arr[tx][ty])
							&& R >= Math.abs(arr[t / 100][t % 100] - arr[tx][ty])) {
						q.add(tx * 100 + ty);
						newq.add(tx * 100 + ty);
						flag = false;
						visited[tx][ty] = 1;
						cnt++;
						sum += arr[tx][ty];
					}
				}
			}
		}
		if (cnt != 1) {
//			System.out.println(sum + " " + cnt);
			int result = sum / cnt;
			while (!newq.isEmpty()) {
				int newx = newq.poll();
				arr[newx / 100][newx % 100] = result;
			}
		} else {
			return;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		arr = new int[n][n];
		
//		System.out.println(n + " " + L + " " + R);
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int index = 0;
		while (true) {
			visited = new int[n][n];
//			for (int[] i : arr) {
//				System.out.println(Arrays.toString(i));
//			}
//			System.out.println();
			flag = true;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (visited[i][j] == 0) {
						solution(i * 100 + j);
					}
				}
			}
			if (flag) {
				break;
			} else {
				index++;
			}
		}

		bw.write(index + "");
		bw.flush();

	}// end of main
}
