//baekjoon source = "https://www.acmicpc.net/problem/2557"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 숫자의합_11720 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String s = br.readLine();
		int result = 0;
		
		for(int i = 0; i<n;i++) {
			result += s.charAt(i)-'0';
		}
		
		bw.write(Integer.toString(result));
		bw.flush();
		bw.close();
	}
}
