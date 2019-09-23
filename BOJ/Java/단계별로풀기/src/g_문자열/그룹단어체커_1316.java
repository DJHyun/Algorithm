//baekjoon source = "https://www.acmicpc.net/problem/1316"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class 그룹단어체커_1316 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int result = 0;
		
		for (int i = 0; i < n; i++) {
			String s = br.readLine();
			List<Character> list = new ArrayList<>();
			char c = ' ';
			boolean flag = true;
			for (int j = 0; j < s.length(); j++) {
				if(!list.contains(s.charAt(j))) {
					list.add(s.charAt(j));
					c = s.charAt(j);
				}else {
					if (s.charAt(j) != c) {
						flag = false;
						break;
					}
				}
			}
			if(flag) {
				result++;
			}
		}
		bw.write(String.valueOf(result));
		bw.flush();
	}
}
