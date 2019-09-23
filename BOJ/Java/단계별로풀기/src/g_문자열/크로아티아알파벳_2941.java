//baekjoon source = "https://www.acmicpc.net/problem/2941"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 크로아티아알파벳_2941 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] check = new String[] { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
		String[] s = br.readLine().split("");
		int result = 0;

		for (int i = 0; i < s.length - 1; i++) {
			boolean flag = true;
			for (int j = 0; j < 8; j++) {
				if (i < s.length - 3 && (s[i] + s[i + 1] + s[i + 2]).equals(check[j])) {
					s[i] = "";
					s[i + 1] = "";
					s[i + 2] = "";
					result++;
					i += 2;
					flag = false;
					break;
				}
				
				if ((s[i] + s[i + 1]).equals(check[j])) {
					s[i] = "";
					s[i + 1] = "";
					result++;
					i += 1;
					flag = false;
					break;
				}
			}
			if (flag)
				result++;
		}

		if (!s[s.length - 1].equals("")) {
			result++;
		}

		bw.write(String.valueOf(result));
		bw.flush();
	}
}
