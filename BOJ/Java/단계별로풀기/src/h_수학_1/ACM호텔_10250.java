//baekjoon source = "https://www.acmicpc.net/problem/10250"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class ACM호텔_10250 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			String[] st = br.readLine().split(" ");
			int h = Integer.parseInt(st[0]), w = Integer.parseInt(st[1]), n = Integer.parseInt(st[2]);

			int a = n / h;
			int b = n % h;

			if (b != 0) {
				if (a + 1 > 9) {
					bw.write(b +""+ (a + 1) + "\n");
				}else {
					bw.write(b + "0" + (a + 1) + "\n");
				}
			} else {
				if(a > 9) {
					bw.write(h +""+ a + "\n");	
				}else {
					bw.write(h + "0" + a + "\n");					
				}
			}
			bw.flush();
		}
	}
}
