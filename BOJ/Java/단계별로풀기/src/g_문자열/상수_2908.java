//baekjoon source = "https://www.acmicpc.net/problem/2908"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 상수_2908 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String[] st = br.readLine().split(" ");
		String a = st[0], b = st[1];
		String newA = "", newB = "";

		for (int i = 2; i > -1; i--) {
			newA += a.charAt(i);
			newB += b.charAt(i);
		}
		
		bw.write(String.valueOf(Math.max(Integer.parseInt(newA),Integer.parseInt(newB))));
		bw.flush();
		bw.close();

	}
}
