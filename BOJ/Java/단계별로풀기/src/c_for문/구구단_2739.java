//baekjoon source = "https://www.acmicpc.net/problem/2739"
package c_for문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 구구단_2739 {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		
		for(int i = 1; i< 10; i ++) {
			System.out.printf("%d * %d = %d%n",n,i,n*i);
		}
	}
}
