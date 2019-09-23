
//baekjoon source = "https://www.acmicpc.net/problem/2628"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _2628_종이자르기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int y = Integer.parseInt(st.nextToken()), x = Integer.parseInt(st.nextToken());
		int[][] arr = new int[2 * x + 1][2 * y + 1];
		int n = Integer.parseInt(br.readLine());
		
		for(int [] i : arr) {
			System.out.println(Arrays.toString(i));
		}
		System.out.println();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			if (st.nextToken().equals("0")) {
				int a = Integer.parseInt(st.nextToken())*2;
				for(int j = 0; j<y*2+1; ++j) {
					arr[a][j] = 1;
				}
			}else {
				int a = Integer.parseInt(st.nextToken())*2;
				for(int j = 0; j<x*2+1; ++j) {
					arr[j][a] = 1;
				}
			}
		}
		for(int [] i : arr) {
			System.out.println(Arrays.toString(i));
		}
	}
}
