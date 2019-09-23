//baekjoon source = "https://www.acmicpc.net/problem/1918"
package 스택;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class _1918_후위표기식 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		char[] c = br.readLine().toCharArray();
		List<Character> check = new ArrayList<Character>();
		check.add('*');
		check.add('+');
		check.add('-');
		check.add('/');
		check.add('(');
		check.add(')');
		Stack<Character> st = new Stack<>();
		StringBuilder result = new StringBuilder();

		for (int i = 0; i < c.length; ++i) {
			if (!check.contains(c[i])) {
				result.append(c[i]);
			} else {
				if (st.isEmpty()) {
					st.add(c[i]);
				} else {
					switch (c[i]) {
					case '+':
						while (!st.isEmpty() && st.peek() != '(') {
							result.append(st.pop());
						} 
						st.add(c[i]);
						break;
					case '-':
						while (!st.isEmpty() && st.peek() != '(') {
							result.append(st.pop());
						} 
						st.add(c[i]);
						break;
					case '*':
						if (st.peek() == '*' || st.peek() == '/') {
							result.append(st.pop());
						}
						st.add(c[i]);
						break;
					case '/':
						if (st.peek() == '*' || st.peek() == '/') {
							result.append(st.pop());
						}
						st.add(c[i]);
						break;
					case '(':
						st.add(c[i]);
						break;
					case ')':
						while (st.peek() != '(') {
							result.append(st.pop());
						}
						st.pop();
						break;
					}
				}
			}
		}

		while (!st.isEmpty()) {
			result.append(st.pop());
		}

		bw.write(result + "");
		bw.flush();
	}
}
