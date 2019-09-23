//baekjoon source = "https://www.acmicpc.net/problem/2164"
package Å¥;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class _2164_Ä«µå2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		Queue<Integer> que = new LinkedList<Integer>();
		for(int i = 1; i<=n; i++) {
			que.add(i);
		}
		while (que.size() != 1) {
			que.poll();
			que.add(que.poll());
		}
		bw.write(que.peek()+"");
		bw.flush();
		
	}
}
