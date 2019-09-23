//baekjoon source = "https://www.acmicpc.net/problem/2775"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 부녀회장이될테야_2775 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int t = Integer.parseInt(br.readLine());
		for (int T = 1; T <= t; T++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
			
			int [][] arr= new int[k+1][n+1];
			for(int i = 0; i<=n; i++) {
				arr[0][i] = i+1;
			}
			for(int i = 0; i<=k; i++) {
				arr[i][0] = 1;
			}
			boolean flag = false;
			for(int i = 1; i<=k; i++) {
				for(int j = 1; j<=n; j++) {
					arr[i][j] = arr[i-1][j] + arr[i][j-1];
					if (i == k && j ==(n-1)) {
						flag = true;
						break;
					}
				}
				if (flag) break;
			}
			
			bw.write(String.valueOf(arr[k][n-1])+"\n");
			bw.flush();
		}
	}
}
