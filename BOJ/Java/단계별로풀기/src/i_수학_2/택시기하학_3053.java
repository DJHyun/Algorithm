//baekjoon source = "https://www.acmicpc.net/problem/3053"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 택시기하학_3053 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int r = Integer.parseInt(br.readLine());
		bw.write(String.format("%.6f%n", Math.PI * Math.pow(r, 2)));
		bw.write(String.format("%.6f%n", 2 * Math.pow(r, 2)));
		bw.flush();
	}
}
