//baekjoon source = "https://www.acmicpc.net/problem/1152"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 단어의개수_1152 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] s = br.readLine().trim().split(" ");
		if(s.length == 1 && s[0].equals("")) {
			bw.write(String.valueOf(0));
		}else {
			bw.write(String.valueOf(s.length));
		}
		bw.flush();
		bw.close();
	}
}
