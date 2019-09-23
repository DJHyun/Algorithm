//baekjoon source = "https://www.acmicpc.net/problem/2447"
package f_ÇÔ¼ö;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class º°Âï±â_10_2447 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
	
		int n = Integer.parseInt(br.readLine());
		String[][] visited = new String[n][n];
		boolean flag = true;
		for (int x = 0; x < n; x++) {
			for (int y = 0; y < n; y++) {
				flag = true;
				int a = x, b = y;
				while (a != 0 || b != 0) {
					if (a % 3 == 1 && b % 3 == 1) {
						flag = false;
						break;
					}
					a /= 3;
					b /= 3;
				}
				if (flag) {
					visited[x][y] = "*";
				}else {
					visited[x][y] = " ";
				}
			}
		}
		for(String[] i : visited) {
			for(String j : i) {
				bw.write(j);
			}
			bw.newLine();
		}
		bw.flush();
	}
}
