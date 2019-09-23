//baekjoon source = "https://www.acmicpc.net/problem/2869"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 달팽이는올라가고싶다_2869 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String[] st = br.readLine().split(" ");
		int a = Integer.parseInt(st[0]), b = Integer.parseInt(st[1]), c = Integer.parseInt(st[2]);

		bw.write(String.valueOf((int)Math.ceil((double) (c - b) / (a - b))));
		bw.flush();
	}
}
