//baekjoon source = "https://www.acmicpc.net/problem/1436"
package j_브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _1436_영화감독숌 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[] result = new int[n];
		int top = -1;
		
		for(int i = 666; ;i++) {
			if (result[n-1] != 0) break;
			if(Integer.toString(i).contains("666")) result[++top] = i;
		}
		bw.write(result[n-1]+"");
		bw.flush();
	}
}
