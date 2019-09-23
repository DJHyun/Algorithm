//baekjoon source = "https://www.acmicpc.net/problem/11729"
package f_함수;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 하노이탑이동순서_11729 {
	static int result, n;
	static int[][] arr;

	static void solution(int a, int x, int y) {
		if (a == 0) {
			return;
		}
		solution(a - 1, x, 6 - x - y);
		arr[0][result] = x;
		arr[1][result] = y;
		result++;
		solution(a - 1, 6 - x - y, y);

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		arr = new int[2][1049000];
		solution(n, 1, 3);
		System.out.println(result);
		for (int i = 0; i < 1049000; i++) {
			if(arr[0][i] != 0) {
				bw.write(arr[0][i] + " "+arr[1][i]);
				bw.newLine();
			}else {
				break;
			}
		}
		bw.flush();
	}
}
