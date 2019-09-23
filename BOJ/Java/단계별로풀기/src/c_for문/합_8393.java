//baekjoon source = "https://www.acmicpc.net/problem/8393"
package c_for¹®;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ÇÕ_8393 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		int result = 0;
		
		for(int i = 1; i<=n; i++) {
			result += i;
		}
		
		System.out.println(result);
	}
}
