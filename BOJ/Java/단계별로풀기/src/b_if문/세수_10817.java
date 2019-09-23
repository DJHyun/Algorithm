//baekjoon source = "https://www.acmicpc.net/problem/10817"
package b_if¹®;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class ¼¼¼ö_10817 {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] st = bf.readLine().split(" ");
		int[] result = new int[3];
		
		for(int i = 0; i< 3; i++) {
			result[i] = Integer.parseInt(st[i]);
		}
		Arrays.sort(result);
		
		System.out.println(result[1]);
	}
}
