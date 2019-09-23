//baekjoon source = "https://www.acmicpc.net/problem/15552"
package c_for문;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 빠른A더하기B_15552 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(bf.readLine());

		for (int i = 0; i < t; i++) {
			String[] st = bf.readLine().split(" ");
			
			int a = Integer.parseInt(st[0]);
			int b = Integer.parseInt(st[1]);
			
			bw.write(a + b+"\n");
			
		}
		bw.flush();
		bf.close();
		bw.close();
	}
}
