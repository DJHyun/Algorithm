//baekjoon source = "https://www.acmicpc.net/problem/9012"
package ½ºÅÃ;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class _9012_°ýÈ£ {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			Stack<Character> stack = new Stack<>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			String check = st.nextToken();
			for (int j = 0; j < check.length(); j++) {
				
				if (j == 0 || stack.size() == 0) {
					stack.add(check.charAt(j));
					continue;
				}
				if(stack.get(0).equals(')')) {
					break;
				}
				switch (check.charAt(j)) {
				case '(':
					if (stack.peek().equals(')')) {
						stack.pop();
					} else {
						stack.add('(');
					}
					break;
				default:
					if (stack.peek().equals('(')) {
						stack.pop();
					} else {
						stack.add(')');
					}
				}
			}
			bw.write((stack.size() == 0 ? "YES" : "NO")+"\n");
		}
		bw.flush();
	}
}

