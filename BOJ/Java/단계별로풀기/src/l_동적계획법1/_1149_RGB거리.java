//baekjoon source = "https://www.acmicpc.net/problem/1149"
package l_동적계획법1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1149_RGB거리 {

	static int n;
	static int[][] arr;
	static int[][] visited;
	static int result;

	static int solution(int x, int sum) {
		int value = 0;
		System.out.println(x + " " + sum);
		
		for (int i = 0; i < 3; i++) {
			if (i == x) {
				continue;
			} else if (visited[x][i] != 0) {
				return visited[x][i];
			} else {
				if (x < n-1) {
					value = solution(x + 1, sum + arr[x+1][i]);
					visited[x][i] = value;
					System.out.println("vi"+visited[x][i]);
				}
				return sum;
			}
		}
		return sum;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(br.readLine());
		arr = new int[n][3];
		result = Integer.MAX_VALUE;
		visited = new int[n][3];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int[] i : arr) {
			bw.write(Arrays.toString(i) + "\n");
		}
		bw.newLine();
		for(int i =0; i<3; i++) {
			solution(0, arr[0][i]);
		}
		for (int[] i : visited) {
			bw.write(Arrays.toString(i) + "\n");
		}
		bw.flush();
	}
}
