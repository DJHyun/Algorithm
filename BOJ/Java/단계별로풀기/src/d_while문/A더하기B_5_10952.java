//baekjoon source = "https://www.acmicpc.net/problem/10952"
package d_while문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A더하기B_5_10952 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true){
			String[] st = br.readLine().split(" ");
			
			if (st[0].equals("0") && st[1].equals("0")) {
				break;
			}
			int a = Integer.parseInt(st[0]);
			int b = Integer.parseInt(st[1]);
			System.out.println(a+b);
		}
	}
}
