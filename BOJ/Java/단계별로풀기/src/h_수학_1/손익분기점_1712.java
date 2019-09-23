//baekjoon source = "https://www.acmicpc.net/problem/1712"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 손익분기점_1712 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String[] st = br.readLine().split(" ");
		long a = Long.parseLong(st[0]), b = Long.parseLong(st[1]), c = Long.parseLong(st[2]);

		c -= b;
		
		if (c <= 0) {
			bw.write(String.valueOf(-1));
		}else {
			bw.write(String.valueOf((long)(a/c)+1));
		}
		
		bw.flush();
		bw.close();
		
	}
}
