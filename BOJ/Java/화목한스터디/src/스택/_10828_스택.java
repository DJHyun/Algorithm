//baekjoon source = "https://www.acmicpc.net/problem/10828"
package 스택;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _10828_스택 {
	static int[] arr = new int[10001];
	static int top = -1;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static void push(int x) {
		arr[++top] = x;
	}

	static void pop() throws IOException {
		if (top == -1) {
			bw.write(-1 + "\n");
		} else {
			bw.write(arr[top] + "\n");
			top--;
		}
	}

	static void size() throws IOException {
		bw.write(top + 1 + "\n");
	}

	static void empty() throws IOException {
		bw.write((top == -1 ? 1 : 0) + "\n");
	}

	static void top() throws IOException {
		bw.write((top == -1 ? -1 : arr[top]) + "\n");
	}

	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			switch (st.nextToken()) {
			case "push":
				push(Integer.parseInt(st.nextToken()));
				break;
			case "pop":
				pop();
				break;
			case "size":
				size();
				break;
			case "empty":
				empty();
				break;
			default:
				top();
			}
		}
		bw.flush();
	}
}
