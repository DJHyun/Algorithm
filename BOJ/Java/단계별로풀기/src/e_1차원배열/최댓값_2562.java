//baekjoon source = "https://www.acmicpc.net/problem/2562"
package e_1차원배열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 최댓값_2562 {
	public static void main(String[] args) throws IOException {
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int max = Integer.MIN_VALUE;
		int result = 0;
		for (int i = 0; i < 9; i++) {
			int check = Integer.parseInt(br.readLine());
			if (max < check) {
				max = check;
				result = i;
			}
		}
		System.out.println(max);
		System.out.println(result + 1);
	}
}
