//baekjoon source = "https://www.acmicpc.net/problem/5622"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 다이얼_5622 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		
		int[] arr = new int[] { 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7,7, 8, 8, 8, 9, 9, 9, 9 };
		int[] time = new int[] { 0, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		int result = 0;
		
		for(int i = 0; i<s.length(); i++) {
			char c = s.charAt(i);
			int cNum = (int)c-65;
			result += time[arr[cNum]];
		}
		
		
		bw.write(String.valueOf(result));
		bw.flush();
		bw.close();
	}
}
