//baekjoon source = "https://www.acmicpc.net/problem/11654"
package g_문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 아스키코드_11654 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char check = br.readLine().charAt(0);
		int result = (int)check;
		
		System.out.println(result);
	}
}
