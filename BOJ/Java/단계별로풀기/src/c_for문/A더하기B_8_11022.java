//baekjoon source = "https://www.acmicpc.net/problem/11022"
package c_for문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A더하기B_8_11022 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for(int i = 0; i<t; i++) {
			String[] st = br.readLine().split(" ");
			int a = Integer.parseInt(st[0]);
			int b = Integer.parseInt(st[1]);
			
			System.out.printf("Case #%d: %d + %d = %d%n",i+1,a,b,a+b);
			
		}
	}
}
