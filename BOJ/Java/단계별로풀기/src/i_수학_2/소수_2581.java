//baekjoon source = "https://www.acmicpc.net/problem/2581"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 소수_2581 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());

		int[] arr = new int[n + 1];
		for (int i = 2; i < n + 1; i++) {
			if (arr[i] == 0) {
				arr[i] = 1;
				int index = 2;
				while (i * index < n + 1) {
					arr[i * index] = 2;
					index++;
				}
			}
		}
		int result = 0, min = 0;
		for(int i = m; i<n+1; i++) {
			if (arr[i] == 1) {
				result += i;
				if (min == 0) {
					min = i;
				}
			}
		}
		if (result == 0) {
			bw.write(-1+"");
		}else {
			bw.write(result+"\n");
			bw.write(min+"");			
		}
		bw.flush();
	}
}
