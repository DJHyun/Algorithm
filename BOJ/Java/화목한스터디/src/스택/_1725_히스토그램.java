//baekjoon source = "https://www.acmicpc.net/problem/1725"
package 스택;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class _1725_히스토그램 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		Stack<Integer> stack = new Stack<>();
		int max = Integer.MIN_VALUE;
		int check = 0;
		
		
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			int number = Integer.parseInt(st.nextToken());
			check = Math.max(check, number);
			if (stack.isEmpty()) {
				stack.add(number);
			}else {
				
			}
		}
		
		bw.flush();
	}
}
