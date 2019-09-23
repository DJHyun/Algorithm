//baekjoon source = "https://www.acmicpc.net/problem/3085"
package 브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 사탕게임_3085 {

	static int n;
	static String[][] arr;
	static int result;
	static int[] garo;
	static int[] sero;

	static void gsolution(int x) {
		for (int i = 0; i < n - 1; i++) {
			if(arr[x][i].equals(arr[x][i+1])) continue;
			String tmp = arr[x][i];
			String tm = arr[x][i + 1];
			arr[x][i] = arr[x][i + 1];
			arr[x][i + 1] = tmp;
			
			int c = 1, re = 0, ct = 1, cre = 0;
			for (int j = 0; j < n; j++) {
				if(j == n-1) {
					re = Math.max(re, c);
					break;
				}
				if (arr[x][j].equals(arr[x][j + 1])) {
					c++;
				} else {
					re = Math.max(re, c);
					c = 1;
				}
			}
			result = Math.max(result, re);
			
			c = 1;
			re = 0;
			ct = 1;
			cre = 0;
			for (int j = 0; j < n; j++) {
				if(j == n-1) {
					re = Math.max(re, c);
					cre = Math.max(cre, ct);
					break;
				}
				if (arr[j][i].equals(arr[j + 1][i])) {
					c++;
				} else {
					re = Math.max(re, c);
					c = 1;
				}

				if (arr[j][i + 1].equals(arr[j + 1][i + 1])) {
					ct++;
				} else {
					cre = Math.max(cre, ct);
					ct = 1;
				}
			}
			re = Math.max(re, cre);
			result = Math.max(result, re);
			arr[x][i] = tmp;
			arr[x][i + 1] = tm;
		}
	}

	static void ssolution(int x) {
		for (int i = 0; i < n - 1; i++) {
			if(arr[i][x].equals(arr[i+1][x])) continue;
			String tmp = arr[i][x];
			String tm = arr[i + 1][x];
			arr[i][x] = arr[i+1][x];
			arr[i + 1][x] = tmp;

			int c = 1, re = 0, ct = 1, cre = 0;
			for (int j = 0; j < n; j++) {
				if(j == n-1) {
					re = Math.max(re, c);
					break;
				}
				if (arr[j][x].equals(arr[j+1][x])) {
					c++;
				} else {
					re = Math.max(re, c);
					c = 1;
				}
			}
			result = Math.max(result, re);

			c = 1;
			re = 0;
			ct = 1;
			cre = 0;
			for (int j = 0; j < n; j++) {
				if (j == n-1) {
					re = Math.max(re, c);
					cre = Math.max(cre, ct);
					break;
				}
				if (arr[i][j].equals(arr[i][j+1])) {
					c++;
				} else {
					re = Math.max(re, c);
					c = 1;
				}

				if (arr[i+1][j].equals(arr[i+1][j+1])) {
					ct++;
				} else {
					cre = Math.max(cre, ct);
					ct = 1;
				}
			}
			
			re = Math.max(re, cre);
			result = Math.max(result, re);
			arr[i][x] = tmp;
			arr[i+1][x] = tm;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(br.readLine());
		arr = new String[n][n];
		garo = new int[n];
		sero = new int[n];
		result = 0;

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String[] s = st.nextToken().split("");
			for (int j = 0; j < n; j++) {
				arr[i][j] = s[j];
			}
		}

		int cg = 0, cs = 0;
		for (int i = 0; i < n; i++) {
			int g = 1, s = 1;
			for (int j = 0; j < n; j++) {
				if (j == n - 1) {
					cg = Math.max(cg, g);
					cs = Math.max(cs, s);
					break;
				}
				if (arr[i][j].equals(arr[i][j + 1])) {
					g++;
				} else {
					cg = Math.max(cg, g);
					g = 1;
				}
				if (arr[j][i].equals(arr[j + 1][i])) {
					s++;
				} else {
					cs = Math.max(cs, s);
					s = 1;
				}
			}
		}
		result = Math.max(cg, cs);

		for (int i = 0; i < n; i++) {
			gsolution(i);
			ssolution(i);
		}
		bw.write(result+"");
		bw.flush();
	}
}
