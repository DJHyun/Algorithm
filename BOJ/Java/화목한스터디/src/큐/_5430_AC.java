//baekjoon source = "https://www.acmicpc.net/problem/5430"
package ť;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class _5430_AC {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			char[] method;
			StringTokenizer st;
			st = new StringTokenizer(br.readLine());
			method = st.nextToken().toCharArray();
			Deque<String> deq = new LinkedList<String>();
			st = new StringTokenizer(br.readLine());
			st.nextToken();
			st = new StringTokenizer(br.readLine());
			String[] s = st.nextToken().replace('[', ' ').replace(']', ' ').trim().split(",");
			for (int i = 0; i < s.length; ++i) {
				if (s[i].equals("")) continue;
				deq.add(s[i]);
			}

			StringBuilder sb = new StringBuilder();
			boolean flag = true;

			for (int i = 0; i < method.length; i++) {
				if (method[i] == 'R') {
					flag = !flag;
				} else {
					if (deq.isEmpty()) {
						sb.append("error");
						break;
					}
					if (flag) {
						deq.pollFirst();
					} else {
						deq.pollLast();
					}
				}
			}
			if (!flag) {
				Collections.reverse((List<?>) deq);
			}
			if (sb.length() == 0) {
				sb.append('[');
				while(!deq.isEmpty()) {
					sb.append(deq.pollFirst());
					if (deq.size() != 0) {
						sb.append(',');
					}
				}
				sb.append(']');
			}
			bw.write(sb + "\n");
			bw.flush();
		}
	}
}
