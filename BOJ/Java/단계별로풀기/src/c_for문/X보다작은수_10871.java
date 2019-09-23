//baekjoon source = "https://www.acmicpc.net/problem/10871"
package c_for문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class X보다작은수_10871 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		int n = Integer.parseInt(st[0]);
		int x = Integer.parseInt(st[1]);
		st = br.readLine().split(" ");
		
		for(int i = 0; i<n; i++) {
			if (Integer.parseInt(st[i]) < x ) {
				if (i != n-1) {
					System.out.print(Integer.parseInt(st[i])+" ");
				}else {
					System.out.print(Integer.parseInt(st[i]));
				}
			}
		}
		
	}
}
