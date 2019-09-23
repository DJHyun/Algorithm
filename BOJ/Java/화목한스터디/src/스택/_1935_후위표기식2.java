//baekjoon source = "https://www.acmicpc.net/problem/1935"
package 스택;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class _1935_후위표기식2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		char[] s = br.readLine().toCharArray();
		Stack<Double> st = new Stack<>();
		Map<String, Double> map = new HashMap<>();

		char abc = 65;
		for (int i = 0; i < n; ++i) {
			map.put(String.valueOf(abc), Double.parseDouble(br.readLine()));
			abc++;
		}

		for (int i = 0; i < s.length; ++i) {
			if (s[i] != '*' && s[i] != '+' && s[i] != '-' && s[i] != '/') {
				st.add(map.get(Character.toString(s[i])));
			} else {
				Double a = st.pop();
				Double b = st.pop();
				switch (s[i]) {
				case '*':
					st.add(a * b);
					break;
				case '/':
					st.add(b / a);
					break;
				case '+':
					st.add(a + b);
					break;
				default:
					st.add(b - a);
				}
			}
		}
		bw.write(String.format("%.2f ", st.peek()));
		bw.flush();
	}
}
