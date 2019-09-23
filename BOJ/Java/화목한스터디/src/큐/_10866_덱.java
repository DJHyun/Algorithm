//baekjoon source = "https://www.acmicpc.net/problem/10866"
package Å¥;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class _10866_µ¦ {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		Deque<Integer> deq = new LinkedList<Integer>();
		int n = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			switch (st.nextToken()) {
			case "push_back":
				deq.add(Integer.parseInt(st.nextToken()));
				break;
			case "push_front":
				deq.addFirst(Integer.parseInt(st.nextToken()));
				break;
			case "front":
				if (deq.isEmpty()) {
					sb.append(-1+"\n");
				}else {
					sb.append(deq.peek()+"\n");
				}
				break;
			case "back":
				if (deq.isEmpty()) {
					sb.append(-1+"\n");
				}else {
					sb.append(deq.peekLast()+"\n");
				}
				break;
			case "size":
				sb.append(deq.size()+"\n");
				break;
			case "empty":
				if (deq.isEmpty()) {
					sb.append(1+"\n");
				}else {
					sb.append(0+"\n");
				}
				break;
			case "pop_front":
				if (deq.size() == 0) {
					sb.append(-1+"\n");
				}else {
					sb.append(deq.pollFirst()+"\n");
				}
				break;
			case "pop_back":
				if (deq.size() == 0) {
					sb.append(-1+"\n");
				}else {
					sb.append(deq.pollLast()+"\n");
				}
				break;
			}
		}
		
		bw.write(sb+"\n");
		bw.flush();
	}
}
