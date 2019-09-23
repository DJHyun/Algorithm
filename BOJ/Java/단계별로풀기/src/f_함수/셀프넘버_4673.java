//baekjoon source = "https://www.acmicpc.net/problem/2557"
package f_함수;

public class 셀프넘버_4673 {
	public static void main(String[] args) {
		int[] visited = new int[10001];
		String j;
		for (int i = 1; i < 10001; i++) {
			if (visited[i] == 0) {
				System.out.println(i);
				j = Integer.toString(i);
				while (true) {
					int check = Integer.parseInt(j);
					for (int s = 0; s < j.length(); s++) {
						check += j.charAt(s) - '0';
					}
					if (check>10000) {
						break;
					}
					visited[check] = 1;
					j = Integer.toString(check);
				}
			}
		}
	}
}
