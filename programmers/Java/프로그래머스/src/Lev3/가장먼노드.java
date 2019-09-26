//source = www.programmers.co.kr
package Lev3;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;

public class 가장먼노드 {

	public static int solution(int n, int[][] edge) {
		int answer = 0;
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();

		for (int i = 0; i < n + 1; i++) {
			list.add(new ArrayList<Integer>());
		}
		for (int i = 0; i < edge.length; i++) {
			int m = edge[i][0];
			int h = edge[i][1];
			list.get(m).add(h);
			list.get(h).add(m);
		}
		int[] visited = new int[n + 1];

		Deque<Integer> que = new LinkedList<>();
		que.add(1);
		visited[1] = 1;

		while (!que.isEmpty()) {
			answer = que.size();
			for (int i = 0; i < answer; ++i) {
				int t = que.pollFirst();
				for (int j = 0; j < list.get(t).size(); ++j) {
					if(visited[list.get(t).get(j)] == 0) {
						que.add(list.get(t).get(j));
						visited[list.get(t).get(j)] = 1;
					}
				}
			}
		}
		
		int cnt = 0;
		for (int i = 0; i <= n; ++i) {
			if (visited[i] == 1) {
				cnt++;
			}
		}
		if (cnt == 1) {
			answer = 0;
		}
		System.out.println("result" + " " + answer);
		return answer;
	}

	public static void main(String[] args) {
		solution(6, new int[][] { { 3, 6 }, { 4, 3 }, { 3, 2 }, { 1, 3 }, { 1, 2 }, { 2, 4 }, { 5, 2 } });
		solution(4, new int[][] { { 1, 2 }, { 1, 3 }, { 2, 4 } });
		solution(4, new int[][] { { 1, 2 }, { 1, 3 }, { 2, 4 }, { 3, 4 } });
		solution(2, new int[][] { { 1, 1 } });
		solution(6, new int[][] { { 1, 5 }, { 1, 6 }, { 1, 2 }, { 1, 3 }, { 1, 4 }, { 2, 3 }, { 3, 4 }, { 2, 5 },
				{ 2, 6 }, { 3, 5 }, { 4, 5 } });
	}
}
