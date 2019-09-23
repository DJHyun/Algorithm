//baekjoon source = "https://www.acmicpc.net/problem/10845"
package ť;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _10845_ť {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[] q = new int[10000];
		int top = -1, rear = -1;
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {

			StringTokenizer st = new StringTokenizer(br.readLine());
			switch (st.nextToken()) {
			case "push":
				q[++rear] = Integer.parseInt(st.nextToken());
				break;
			case "pop":
				bw.write((top == rear ? -1 : q[++top]) + "\n");
				break;
			case "size":
				bw.write(rear - top + "\n");
				break;
			case "empty":
				bw.write((top == rear ? 1 : 0) + "\n");
				break;
			case "front":
				bw.write((top == rear ? -1 : q[top + 1]) + "\n");
				break;
			case "back":
				bw.write((top == rear ? -1 : q[rear]) + "\n");
			}
		}
		bw.flush();
	}
}
