//source = www.programmers.co.kr
package Lev3;

import java.util.Deque;
import java.util.LinkedList;

public class 네트워크 {
	static int answer;
	static int[] visited;
	
	public static void solve(int number, int[][] computers, int n) {
		Deque<Integer> dq = new LinkedList<>();
		visited[number] = 1;
		dq.add(number);
		
		while (!dq.isEmpty()) {
			System.out.println(dq);
			int q = dq.pollFirst();
			for (int i = 0; i < n; ++i) {
				if (q == i)	continue;
				if (computers[q][i] == 1 && visited[i] == 0 ) {
					visited[i] = 1;
					dq.add(i);
				}
			}
		}
	}
	
	
	public static int solution(int n, int[][] computers) {
		answer = 0;
		visited = new int[n];
		for(int i = 0; i<n; ++i) {
			if (visited[i] == 0) {
				solve(i,computers, n);
				answer++;
			}
		}
		System.out.println(answer);
		return answer;
	}

	public static void main(String[] args) {
		solution(3, new int[][] { { 1, 1, 0 }, { 1, 1, 0 }, { 0, 0, 1 } });
	}
}
