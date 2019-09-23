//baekjoon source = "https://www.acmicpc.net/problem/4153"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 직각삼각형_4153 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for (;;) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int[] a = new int[] { Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
					Integer.parseInt(st.nextToken()) };
			Arrays.sort(a);
			if (a[0] == 0) {
				break;
			}

			if (Math.pow(a[0], 2) + Math.pow(a[1], 2) == Math.pow(a[2], 2)) {
				bw.write("right");
			} else {
				bw.write("wrong");
			}
			bw.newLine();
		}
		bw.flush();
	}
}
